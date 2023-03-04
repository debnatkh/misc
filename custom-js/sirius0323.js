try {
  document.querySelector('.standings tbody tr th:nth-of-type(2)').style.width='200px';
} catch (error) {
  console.error(error);
}

const dict = {
  "a.nasretdinov": "Насретдинов Амир",
  "AndreyPavlov": "Павлов Андрей",
  "kolomig0r": "Коломиец Игорь",
  "yaaarseny": "Ятчений Арсений",
  "T4M0FEY": "Ижицкий Тимофей",
  "H235": "Жеглов Александр",
  "IGlazkovI": "Глазков Илья",
  "UhahaUhaha": "Яшкин Роберт",
  "meowcneil": "Макнил Александр",
  "ArtemUstimenko": "Устименко Артём",
  "127.0.0.1": "Авдеев Дмитрий",
  "2020TAndr": "Тунёв Андрей",
  "nya.qin.": "Шейкис Марк",
  "Rodionno": "Кунакбаев Родион",
  "systy": "Возмилов  Георгий",
  "Son_of_Dijkstra": "Хамитов Хаким",
  "t.ravnushkin": "Равнушкин Тимофей",
  "tiom4eg": "Туревич Артём",
  "lerasimus": "Соболев Олег",
  "s1r_D": "Шакиров Идрис",
  "_shakespeare_": "Зарубин  Егор",
  "average_treap_enjoyer": "Балакин Владимир",
  "Sokol080808": "Сокольников Алексей",
  "akritovandrey": "Акритов Андрей",
  "yaroslav_n": "Ноздрин Ярослав",
  "makrav": "Кравченко Максим",
  "VolkovMA": "Волков Михаил",
  "zwezdinv": "Звездин Владимир",
  "Grigoreva-Irina": "Григорьева Ирина",
  "average_treap_enjoyer": "Балакин Владимир",
  "anadere": "Антонова Анна",
  "Prokhor08": "Иголкин Прохор",
  "molney": "Ходыкин Тимофей",
  "Mishazher": "Жерневский Михаил",
  "vdxz": "Черников Владислав",
  "_MatMath_": "Маевский Матвей",
  "zhiganov_v": "Жиганов Владислав",
  "Blinov_Artemii": "Блинов Артемий",
  "Georggg999": "Степанян Георгий",
  "pervuneckih.v.2025": "Первунецких Еремей",
  "Kapitar": "Ким Артём",
  "VAntonuk": "Антонюк Вадим",
  "Daughter_of_Dijkstra": "Желтовский Владислав",
  "sputn1k": "Свирид Егор",
  "ArSarapkin": "Сарапкин Артём",
  "KoT_OsKaR": "Шабаров Игорь",
  "vl342": "Бурмистров Владислав",
  "EnderMaster": "Шубин Матвей",
  "_dmitriy_makarov_": "Макаров Дмитрий",
  "MaxBalakirev": "Балакирев Максим",
  "Noinoiio": "Любин Михаил",
  "nek12312378": "Минасян Никита",
  "SugarDadGG": "Хамитов Галим",
  "lunaTu": "Левина Мария",
  "IvanD": "Девятьяров Иван",
  "sdyakonov": "Дьяконов Сергей",
  "alexvezh": "Вежновец Александр",
  "sirazeev": "Сиразеев Ильяс",
  "prosrun": "Солдатов Максим",
  "__Foam": "Голиков Егор",
  "Mr_Ell": "Гаврилов Максим",
  "Noobish_Monk": "Беляев Марк",
  "Mizev_Andrey": "Мизев Андрей",
  "glooooby": "Малышев Игорь",
  "xfloud": "Прыгунов Ярослав",
  "Tadfo": "Файзуллин Андрей",
  "makcvim": "Солдатов Максим",
  "polosatic": "Ожегов Леонид",
  "kiquxd": "Кобзев Андрей",
  "aone_A1": "Кононов Олег",
  "MaSkA05": "Скрипник Максим",
  "Hectonit": "Егоров Тимофей",
  "tch1cherin": "Чичерин Тимофей",
  "zog34bro": "Макаров Михаил",
  "_IVON_": "Пономарев Иван",
  "tikhon_grinev": "Гринев Тихон",
  "Margaret07": "Зедгенизова Маргарита",
  "cup_of_coffee": "Кудашев Фёдор",
  "EJIC_B_KEDAX": "Кузнецов Иван",
  "RomkaRS": "Шумилов Роман",
  "Pavarishko": "Мотыгуллин Карим",
  "GGFu87": "Пучков Пётр",
  "hero_of_math_and_magic": "Бацын Тимофей",
  "Nil2007": "Иванов Нил",
  "Timur2006": "Лузгов Тимур",
  "EvgenyUtkin": "Уткин Евгений",
  "Egakrut3": "Кривов Георгий",
  "HimerZERO": "Чернышов  Игнат",
  "goodbee": "Лещинский Артём",
  "iNNNo": "Сыздыков Константин",
  "Greg908": "Новгородцев Григорий",
  "arseny2606": "Порхунов Арсений",
  "hoshiii": "Хаев Булат",
  "Fedorshebanin": "Шебанин Фёдор",
  "YseraKon": "Коновалов Ярослав",
  "ventilator13": "Ильин Михаил",
  "bibikov1": "Бибиков Александр",
  "AntonMordakin": "Мордакин Антон",
  "Smurf_with_me": "Волков Алексей",
  "zhukovaliza": "Жукова Елизавета",
  "svorogaze": "Загоровский Владимир",
};

// Rename users
document.querySelectorAll('.rated-user').forEach(a => {
  const key = a.innerHTML.trim();
  if (key in dict) {
    a.innerHTML = dict[key];
  }
});

// Hide flag
document.querySelectorAll('.standings-flag').forEach(a => {
  a.remove();
});

// Hide to-practice
const aElements = document.querySelectorAll('.change-participant-type-link').forEach(a => {
  a.remove()
});
