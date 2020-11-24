import time, hashlib, json, os, warnings, cgi, re, csv, random
import requests
from collections import defaultdict
from httplib2 import Http
from bs4 import BeautifulSoup

session = requests.Session()

group_id = input('Номер группы:')  # 15589
tokens = dict()
tokens["INF_LOGIN"] = input("Login:")
tokens["INF_PASSWORD"] = input("Password:")

url = "https://informatics.msk.ru/login/index.php"
data = {'username': tokens['INF_LOGIN'], 'password': tokens['INF_PASSWORD']}
session.get(url)
session.post(url, data)

logins = []
lg = input("Логины по одному в строке. Окончание - 3 восклицательных знака.\n")
while lg != "!!!":
    if lg.strip() != "":
        logins.append(lg.strip())
    else:
        print('Not correct', lg)
    lg = input()
cnt = 0
for name in logins:
    url = "https://informatics.msk.ru/moodle/ajax/ajax.php?sid=&objectName=group&objectId=all&selectedName=users&action=list"
    data = {
        "start": "0",
        "limit": "100",
        "sort": "lastname",
        "dir": "ASC",
        "filter[0][field]": "username",
        "filter[0][data][type]": "string",
        "filter[0][data][value]": name,
    }

    r = session.post(url, data=data)
    time.sleep(1)
    y = json.loads(r.text)
    finded = False
    us = ''
    for u in y['users']:
        try:
            if u['username'].lower() == name.lower():
                finded = True
                us = u
                break
        except Exception:
            print("Fail!!! {0}   {1}   {2}".format(name, u, Exception))
    if not finded:
        print("Not found!!! {0} {1} ".format(name, y))
        continue
    print(name, us, y)

    url = "https://informatics.msk.ru/moodle/ajax/ajax.php?sid=&objectName=group&objectId=" + str(group_id) + "&selectedName=users&action=add"

    data = {
        "addParam": str(us).replace('"', '\\"').replace('\'', "\""),
        "group_id": "",
        "session_sid": "",
    }

    print(name, data)

    r = session.post(url, data=data)
    if str(r) != '<Response [200]>':
        print("Fail add!!! {0}   *{1}* ".format(name, r))
        continue
    cnt += 1
    time.sleep(0.25)

print('Finded {0} from {1}.'.format(cnt, len(logins)))
