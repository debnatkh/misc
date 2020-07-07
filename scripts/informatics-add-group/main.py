import time, json
import requests
from httplib2 import Http

session = requests.Session()


config = dict()
config["INF_LOGIN"] = "****************"
config["INF_PASSWORD"] = "****************"
config["GROUP_ID"] = "15587"
names = ["a.stepanov2005", "breadway", "daniil.bentsa", "ekaterina2018", "Limo56", "thematdev", "paul.kalug", "vladglazkov", "Ilya.kligunov", "kirill.kligunov", "ShinigamiCHOP", "lohuas", "IT56", "gerasikov.fml31", "artem3605", "d.sosunov", "gerasikov.fml31", "glebustim", "r.mouse.05", "amirnas", "fetis04@mail.ru", "sobachka", "newest7", "ilyakrasnovv", "post1107", "Oslik2006", "timurxan", "alex.kudrayshov", "lesnikgera", "SerZak", "vdv09", "aafiul", "mashapakkanen", "niktop", "igolkin.fml31", "avdeev2006", "khodak-gg@mail.ru", "ilinmisha13042006", "savvaw5", "yarykin.zhen", "GrishaRed", "dushenkov", "danya11", "Tm-A-T", "kseniashkuleva", "aleks.art", "meggra", "ivan18062006", "krylykov", "DimaTomsk", "Levsovga", "EvgenyUtkin", "ximer931", "suleimanova.xenia", "igor.malyshev07@gmail.com", "MrEssiorx", "AndrewSap", "akelv", "max1108", "btikirov", "nikita7777", "andrmizev", "avolkov2023", "timur20061", "artemtur", "ivanovnil2007@gmail.com", "exvita@yandex.ru", "alino4ka92", "robert2006", "Nikita2006Yashin", "n-ant", "kostylev.a.2023", "pervuneckih.v.2025"]

url = "https://informatics.msk.ru/login/index.php"
data = {'username': config['INF_LOGIN'], 'password': config['INF_PASSWORD']}
session.get(url)
session.post(url, data)


for name in names:
	url = "https://informatics.msk.ru/moodle/ajax/ajax.php?sid=&objectName=group&objectId=all&selectedName=users&action=list"
	data = {
		"start": "0",
		"limit": "25",
		"sort": "lastname",
		"dir": "ASC",
		"filter[0][field]": "username",
		"filter[0][data][type]": "string",
		"filter[0][data][value]": name,
	}

	r = session.post(url, data=data)
	time.sleep(0.5)
	y = json.loads(r.text)
	print(y)

	url = "https://informatics.msk.ru/moodle/ajax/ajax.php?sid=&objectName=group&objectId=" + config["GROUP_ID"] + "&selectedName=users&action=add"

	data = {
		"addParam": str((y['users'][0])).replace('\'', "\""),
		"group_id": "",
		"session_sid": "", 
	}

	print(data)

	r = session.post(url, data=data)
	time.sleep(0.5)
