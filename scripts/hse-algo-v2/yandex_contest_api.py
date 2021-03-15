#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from typing import NamedTuple, List

import requests


class Problem(NamedTuple):
    short: str
    long: str
    link: str


class ContestStandings(NamedTuple):
    name: str
    results: List[List[str]]
    problems: List[Problem]


class YandexContestAPI:
    def __init__(self, auth_key, contest_id):
        self.API_ENDPOINT = 'https://api.contest.yandex.net/api/public/v2/contests'
        self.contest_id = contest_id
        self.HEADERS = {
            'Authorization': auth_key,
            'Accept': '*/*',
        }

    def get(self, req, **params):
        response = requests.get(self.API_ENDPOINT + "/{}".format(self.contest_id) + req, params=params,
                                headers=self.HEADERS)
        if not response.ok:
            logging.info(response.status_code, response.reason)
            raise RuntimeError("Request failed: {}".format(req))
        return response.json()

    def get_problem_name_mapping(self, ):
        problems = self.get("/problems")["problems"]
        return {problem["name"]: problem["alias"] for problem in problems}

    def get_submissions(self, page):
        logging.info(f"Requesting submissions from page {page}")
        response = self.get("/submissions", page=page)
        return [s for s in response["submissions"]]

    def get_all_submissions(self, ):
        res = []
        page = 1
        while True:
            new_subs = self.get_submissions(page)
            if not new_subs:
                break
            res += new_subs
            page += 1
        return [(s["author"], s["problemAlias"], s["id"]) for s in res if s["verdict"] == "OK"]

    def is_submission_before_deadline(self, submission_id, contest_duration):
        return self.get(f"/submissions/{submission_id}/full")["timeFromStart"] / 1000 < contest_duration

    def find_last_submission_after_deadline(self, ids, contest_duration):
        for i in range(len(ids) - 1):
            assert ids[i] > ids[i + 1]
        if self.is_submission_before_deadline(ids[0], contest_duration):
            return ids[0]
        if not self.is_submission_before_deadline(ids[-1], contest_duration):
            return 0
        left, right = 0, len(ids) - 1
        while left + 1 < right:
            med = (left + right) // 2
            if self.is_submission_before_deadline(ids[med], contest_duration):
                right = med
            else:
                left = med
        return ids[right]

    @staticmethod
    def get_full_student_name(name, students: List[str]):
        res = None
        for student in students:
            if name.replace('ё', 'е') in student.replace('ё', 'е'):
                if res is not None:
                    logging.info(f"'{name.encode('utf8')}' matches multiple entries from the google sheet")
                    return None
                res = student
        if res is None:
            logging.info(f"'{name.encode('utf8')}' does not match any entry from the google sheet")
        return res

    def generate_standings(self, students):
        name_mapping = self.get_problem_name_mapping()
        problems: List[Problem] = []
        for long_name, short_name in sorted(iter(name_mapping.items()), key=lambda x: x[1]):
            problems.append(
                Problem(short_name, long_name,
                        f"https://official.contest.yandex.ru/contest/{self.contest_id}/problems/{short_name}"))

        logging.info(f'Problems in contest {self.contest_id} (total {len(problems)})')
        for problem in problems:
            logging.info(problem)
        logging.info("")

        subs = self.get_all_submissions()
        ids = [s[2] for s in subs]
        contest_duration = self.get("")["duration"]
        logging.info(
            "Contest duration is {}:{:02d}:{:02d}.".format(contest_duration // 3600, contest_duration // 60 % 60,
                                                           contest_duration % 60))
        last_id = self.find_last_submission_after_deadline(ids, contest_duration)
        logging.info(f"Last submission before deadline has id {last_id}.")

        scores = {}

        for s, p, submission_id in subs:
            student = self.get_full_student_name(s, students)
            problem = p
            if student is None or problem is None:
                logging.info(f"Failed to process entry ({s}, {p}, {submission_id})")
                continue
            score = 1 if submission_id <= last_id else 0.5
            if student not in scores:
                scores[student] = {}
            scores[student][problem] = score

        table = []
        for name in students[:-1]:
            res = []
            sc = scores.get(name, {})
            for letter in sorted(name_mapping.values()):
                res.append(sc.get(letter, ''))
            table.append(res)
        return ContestStandings(self.get('')['name'], table, problems)
