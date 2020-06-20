#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json, sys
from pprint import pprint

AUTH_KEY='OAuth XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

API='https://api.contest.yandex.net/api/public/v2/contests'

CONTEST_ID=10023

HEADERS = {
    'Authorization': AUTH_KEY,
    'Accept': '*/*',
}

STUDENTS = """
TOTAL
Глеб (181-1)
Виноградов Олег
Грибов Филипп Юрьевич
Деб Натх Максим -
Илюхов Алексей Евгеньевич
Искандаров Лев Андреевич
Ифанов Илья Андреевич
Конодюк Никита Евгеньевич
Николенко Даниил Юрьевич
Пак Ди Ун -
Проскурин Николай Вадимович
Романченко Полина Максимовна
Соколов Павел Павлович
Соколовский Алексей Константинович
Степанов Никита Сергеевич
TOTAL

Стас (181-2)
Абрамчик Владислав
Ашурбеков Замир Идрисович
Гороховский Максим Андреевич
Еленик Константин Ильич
Исаев Сергей Олегович
Калинин Никита Павлович
Карпов Владимир Евгеньевич
Матросов Артемий Валерьевич
Морозов Никита Витальевич
Павлов Вадим Алексеевич
Сахабиев Асхат Равилевич
Тертичный Дмитрий Евгеньевич
Фадеев Никита Алексеевич
Чайковский Илья Кириллович
Шамазов Карим Фаридович
TOTAL

Дима (183-1)
Ветров Андрей Александрович
Виноградова Дарья Сергеевна
Греков Илья Сергеевич
Григорьев Петр Владимирович
Залялов Александр Олегович
Зверев Игорь Евгеньевич
Иванов Семен Вадимович
Карташев Николай Геннадьевич
Колесников Георгий Сергеевич
Никитин Роман Александрович
Серикова Екатерина Вячеславовна
Солодовников Никита Александрович
Тушканов Евгений Николаевич
Шморгунов Александр Алексеевич
Ямбулатов Искандер Рафаэлевич
TOTAL

Иван (183-2)
Выродов Руслан Геннадьевич
Зуев Михаил Алексеевич
Корнейчик Марк Сергеевич
Коряков Алексей Витальевич
Лобанов Глеб Игоревич
Миронов Алексей Дмитриевич
Некрашевич Андрей Владимирович
Нуриев Айнур Зуфарович
Прокопенко Даниил Ильич
Сафиуллин Зуфар Гумарович
Сергеев Егор Алексеевич
Смирнов Тимофей Алексеевич
Старанцов Артём Алексеевич
Стержанова Екатерина Игоревна
Субхангулов Султан Шамилевич
Царева Юлия Сергеевна
TOTAL
Аабсолютный Максимум""".split('\n')


def get(req, **params):
    response = requests.get(API + "/{}".format(CONTEST_ID) + req, params=params, headers=HEADERS)
    if not response.ok:
        print>>sys.stderr, response.status_code, response.reason
        raise RuntimeError("Request failed: {}".format(req))
    return response.json()


def get_problem_name_mapping():
    problems = get("/problems")["problems"]
    return { problem["name"] : problem["shortName"] for problem in problems }



def get_submissions(page):
    print>>sys.stderr, "Requesting submissions from page {}".format(page)
    response = get("/submissions", page=page)
    return [(s["author"], s["problem"], s["id"]) for s in response["submissions"] if s["verdict"] == "OK"]


def get_all_submissions():
    res = []
    page = 1
    while True:
        new_subs = get_submissions(page)
        if not new_subs:
            return res
        res += new_subs
        page += 1
    return res


def is_submission_before_deadline(id, contest_duration):
    return get("/submissions/{}/full".format(id))["timeFromStart"] / 1000 < contest_duration 


def find_last_submission_after_deadline(ids, contest_duration):
    for i in range(len(ids) - 1):
        assert ids[i] > ids[i+1]
    if is_submission_before_deadline(ids[0], contest_duration):
        return ids[0]
    if not is_submission_before_deadline(ids[-1], contest_duration):
        return 0
    l, r = 0, len(ids) - 1
    while l + 1 < r:
        m = (l+r) / 2
        if is_submission_before_deadline(ids[m], contest_duration):
            r = m
        else:
            l = m
    return ids[r]


def get_full_student_name(name):
    res = None
    for student in STUDENTS:
        if name.encode("utf8").replace('ё', 'е') in student.replace('ё', 'е'):
            if res is not None:
                print>>sys.stderr, "'{}' matches multiple entries from the google sheet".format(name.encode("utf8"))
                return None
            res = student
    if res is None:
        print>>sys.stderr, "'{}' does not match any entry from the google sheet".format(name.encode("utf8"))
    return res


if __name__ == "__main__":
    print>>sys.stderr, "Consistency check: line {} in the google sheet must contain '{}'.".format(len(STUDENTS) - 2,  STUDENTS[-3])

    name_mapping = get_problem_name_mapping()
    print>>sys.stderr, "Problems:"
    for long, short in sorted(name_mapping.iteritems(), key=lambda x: x[1]):
        print>>sys.stderr, " {}: {}".format(short, long.encode("utf8"))

    subs = get_all_submissions()
    ids = [s[2] for s in subs]
    contest_duration = get("")["duration"]
    print>>sys.stderr, "Contest duration is {}:{:02d}:{:02d}.".format(contest_duration/3600, contest_duration/60%60, contest_duration%60)
    last_id = find_last_submission_after_deadline(ids, contest_duration)
    print>>sys.stderr, "Last submission before deadline has id {}.".format(last_id)

    scores = {}

    for s, p, id in subs:
        student = get_full_student_name(s)
        problem = name_mapping.get(p)
        if student is None or problem is None:
            print>>sys.stderr, "Failed to process entry ({}, {}, {})".format(s.encode("utf8"), p.encode("utf8"), id)
            continue
        score = 1 if id <= last_id else 0.5
        if student not in scores:
            scores[student] = {}
        scores[student][problem] = score

    res = ""
    for name in STUDENTS[3:-1]:
        sc = scores.get(name, {})
        first = True
        for letter in sorted(name_mapping.values()):
            if first:
                first = False
            else:
                res += '\t'
            res += str(sc.get(letter, ''))
        res += '\n'
    sys.stdout.write(res)
    print>>sys.stderr, "Now paste it to the google sheet starting with row 4!"