#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json, sys
from pprint import pprint

AUTH_KEY='OAuth XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

API='https://api.contest.yandex.net/api/public/v2/contests'

CONTEST_ID=18595

HEADERS = {
    'Authorization': AUTH_KEY,
    'Accept': '*/*',
}

STUDENTS = """
TOTAL
Глеб (191-1)
Амеличев Константин Вадимович
Аржанцев Алексей Иванович
Иваник Даниил Иванович
Исмагилов Артем Ниязович
Макоян Артем Каренович
Мустафин Александр
Погодин Михаил Александрович
Пятько Даниил Владимирович
Романов Владимир Олегович
Случ Дмитрий Борисович
Фридман Иван Владимирович
Че Андрей
Чечин Богдан Сергеевич
Ширма Кирилл Олегович
Катунькин Михаил Андреевич
TOTAL
Стас (191-2)
Акулов Дмитрий Александрович
Ахметшин Кирилл Данилевич
Барышников Антон Константинович
Волгин Даниил Эдуардович
Гудзь Михаил Евгеньевич
Зинченко Данила Сергеевич
Ичалов Леонид Евгеньевич
Колодезный Александр Анатольевич
Кондратьев Захар Михайлович
Перевышин Алексей Константинович
Плотникова Анастасия Ивановна
Сапожников Денис Сергеевич
Упирвицкий Алексей Николаевич
Шишков Алексей Алексеевич
Сизов Кирилл Игоревич
TOTAL
Гриша (193-1)
Аъзам Бехруз Хусан угли
Балюк Игорь Алексеевич
Беляков Савелий Валерьевич
Бобень Вячеслав Александрович
Гутров Егор Дмитриевич
Казанцев Даниил Андреевич
Кулдошин Алексей Дмитриевич
Лукомский Вячеслав Игоревич
Максимов Алексей Николаевич
Никулин Олег Алексеевич
Рязанов Даниил Алексеевич
Стрекаловская Наталья Андреевна
Тренин Александр Александрович
Шабат Дмитрий Васильевич
Шрайнер Данил Павлович
TOTAL
Иван (193-2)
Васильев Даниил Алексеевич
Голенков Алексей Николаевич
Голубь Алексей Олегович
Леванков Егор Сергеевич
Лоптев Сергей Евгеньевич
Новицкий Иван Александрович
Новичков Александр Юрьевич
Переведенцев Артём Евгеньевич
Петров Дамир Петрович
Притуляк Илья Николаевич
Сизов Илья Игоревич
Сысоева Ярослава Евгеньевна
Таныгин Антон Сергеевич
Филиппов Андрей Владимирович
Шатов Олег Викторович
TOTAL
Святослав (195-1)
Богданов Александр Дмитриевич
Буримский Семён Андреевич
Вернигор Алиса Игоревна
Воронин Андрей Андреевич
Голобородько Ирина Денисовна
Жуманиезов Эльбек Алишерович
Козлов Денис Михайлович
Козлова Ольга Алексеевна
Орлов Александр Юрьевич
Рофин Марк Петрович
Смородинникова Анастасия
Степанов Семён Евгеньевич
Сушков Артем Олегович
Шепелин Дмитрий Константинович
Шныпко Василий Дмитриевич
TOTAL
Никита (195-2)
Акимов Александр Дмитриевич
Басалаев Максим
Беляев Иван Алексеевич
Березовский Валерий Сергеевич
Воуба Архип Валерьевич
Ершов Кирилл Геннадьевич
Лобода Максим Юрьевич
Лущ Иван
Мальков Дмитрий Олегович
Мошков Иван Владимирович
Насонков Никита Владимирович
Орешонок Елизавета Андреевна
Рыжов Артемий Викторович
Степанов Семён Степанович
Чуканов Илья Валерьевич
TOTAL""".split('\n')


def get(req, **params):
    response = requests.get(API + "/{}".format(CONTEST_ID) + req, params=params, headers=HEADERS)
    if not response.ok:
        print(response.status_code, response.reason, file=sys.stderr)
        raise RuntimeError("Request failed: {}".format(req))
    return response.json()


def get_problem_name_mapping():
    problems = get("/problems")["problems"]
    return { problem["name"] : problem["shortName"] for problem in problems }



def get_submissions(page):
    print("Requesting submissions from page {}".format(page), file=sys.stderr)
    response = get("/submissions", page=page)
    return [s for s in response["submissions"]]


def get_all_submissions():
    res = []
    page = 1
    while True:
        new_subs = get_submissions(page)
        if not new_subs:
            break
        res += new_subs
        page += 1
    return [(s["author"], s["problem"], s["id"]) for s in res if s["verdict"] == "OK"]


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
        m = (l+r) // 2
        if is_submission_before_deadline(ids[m], contest_duration):
            r = m
        else:
            l = m
    return ids[r]


def get_full_student_name(name):
    res = None
    for student in STUDENTS:
        if name.replace('ё', 'е') in student.replace('ё', 'е'):
            if res is not None:
                print("'{}' matches multiple entries from the google sheet".format(name.encode("utf8")), file=sys.stderr)
                return None
            res = student
    if res is None:
        print("'{}' does not match any entry from the google sheet".format(name.encode("utf8")), file=sys.stderr)
    return res


if __name__ == "__main__":
    print("Consistency check: line {} in the google sheet must contain '{}'.".format(len(STUDENTS) - 2,  STUDENTS[-3]), file=sys.stderr)

    name_mapping = get_problem_name_mapping()
    print("Problems:", file=sys.stderr)
    for int, short in sorted(iter(name_mapping.items()), key=lambda x: x[1]):
        print(" {}: {}".format(short, int.encode("utf8")), file=sys.stderr)

    subs = get_all_submissions()
    ids = [s[2] for s in subs]
    contest_duration = get("")["duration"]
    print("Contest duration is {}:{:02d}:{:02d}.".format(contest_duration//3600, contest_duration//60%60, contest_duration%60), file=sys.stderr)
    last_id = find_last_submission_after_deadline(ids, contest_duration)
    print("Last submission before deadline has id {}.".format(last_id), file=sys.stderr)

    scores = {}

    for s, p, id in subs:
        student = get_full_student_name(s)
        problem = name_mapping.get(p)
        if student is None or problem is None:
            print("Failed to process entry ({}, {}, {})".format(s.encode("utf8"), p.encode("utf8"), id), file=sys.stderr)
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
    print("Now paste it to the google sheet starting with row 4!", file=sys.stderr)