try {
  document.querySelector('.standings tbody tr th:nth-of-type(2)').style.width='200px';
} catch (error) {
  console.error(error);
}

const dict = {
  "Sokol080808": "[Н15] Сокольников Алексей",
  "zwezdinv": "[Н15] Звездин Владимир",
  "molney": "[Н15] Ходыкин Тимофей",
  "Mishazher": "[Н17] Жерневский Михаил",
  "makcvim": "[Н18] Солдатов Максим",
  "T4M0FEY": "[Н17] Ижицкий Тимофей",
  "tiom4eg": "[Н17] Туревич Артём",
  "Prokhor08": "[Н17] Иголкин Прохор",
  "tch1cherin": "[Н15] Чичерин Тимофей",
  "zhukovaliza": "[Н17] Жукова Елизавета",
  "a.nasretdinov": "[Н18] Насретдинов Амир",
  "makrav": "[Н15] Кравченко Максим",
  "zhiganov_v": "[Н15] Жиганов Владислав",
  "_dmitriy_makarov_": "[Н18] Макаров Дмитрий",
  "UhahaUhaha": "[Н18] Яшкин Роберт",
  "Grigoreva-Irina": "[Н15] Григорьева Ирина",
  "Noinoiio": "[Н17] Любин Михаил",
  "polosatic": "[Н18] Ожегов Леонид",
  "MaSkA05": "[Н18] Скрипник Максим",
  "_IVON_": "[Н18] Пономарев Иван",
  "hero_of_math_and_magic": "[Н15] Бацын Тимофей",
  "AndreyPavlov": "[Н17] Павлов Андрей",
  "Rodionno": "[Н18] Кунакбаев Родион",
  "systy": "[Н17] Возмилов  Георгий",
  "nek12312378": "[Н18] Минасян Никита",
  "IvanD": "[Н17] Девятьяров Иван",
  "Tadfo": "[Н15] Файзуллин Андрей",
  "yaaarseny": "[Н17] Ятчений Арсений",
  "_shakespeare_": "[Н17] Зарубин  Егор",
  "VolkovMA": "[Н17] Волков Михаил",
  "anadere": "[Н17] Антонова Анна",
  "_MatMath_": "[Н16] Маевский Матвей",
  "Mr_Ell": "[Н15] Гаврилов Максим",
  "Mizev_Andrey": "[Н15] Мизев Андрей",
  "kiquxd": "[Н18] Кобзев Андрей",
  "RomkaRS": "[Н17] Шумилов Роман",
  "Timur2006": "[Н18] Лузгов Тимур",
  "Egakrut3": "[Н16] Кривов Георгий",
  "goodbee": "[Н18] Лещинский Артём",
  "bibikov1": "[Н17] Бибиков Александр",
  "Smurf_with_me": "[Н18] Волков Алексей",
  "svorogaze": "[Н16] Загоровский Владимир",
  "kolomig0r": "[Н18] Коломиец Игорь",
  "2020TAndr": "[Н18] Тунёв Андрей",
  "Blinov_Artemii": "[Н17] Блинов Артемий",
  "MaxBalakirev": "[Н16] Балакирев Максим",
  "__Foam": "[Н17] Голиков Егор",
  "aone_A1": "[Н18] Кононов Олег",
  "zog34bro": "[Н15] Макаров Михаил",
  "Pavarishko": "[Н18] Мотыгуллин Карим",
  "GGFu87": "[Н18] Пучков Пётр",
  "Nil2007": "[Н16] Иванов Нил",
  "EvgenyUtkin": "[Н18] Уткин Евгений",
  "Greg908": "[Н18] Новгородцев Григорий",
  "YseraKon": "[Н16] Коновалов Ярослав",
  "Son_of_Dijkstra": "[Н16] Хамитов Хаким",
  "pervuneckih.v.2025": "[Н15] Первунецких Еремей",
  "Kapitar": "[Н16] Ким Артём",
  "ArSarapkin": "[Н16] Сарапкин Артём",
  "vl342": "[Н17] Бурмистров Владислав",
  "lunaTu": "[Н15] Левина Мария",
  "Noobish_Monk": "[Н16] Беляев Марк",
  "iNNNo": "[Н18] Сыздыков Константин",
  "hoshiii": "[Н18] Хаев Булат",
  "meowcneil": "[Н16] Макнил Александр",
  "ArtemUstimenko": "[Н15] Устименко Артём",
  "127.0.0.1": "[Н17] Авдеев Дмитрий",
  "t.ravnushkin": "[Н16] Равнушкин Тимофей",
  "akritovandrey": "[Н18] Акритов Андрей",
  "yaroslav_n": "[Н17] Ноздрин Ярослав",
  "Daughter_of_Dijkstra": "[Н16] Желтовский Владислав",
  "SugarDadGG": "[Н16] Хамитов Галим",
  "Margaret07": "[Н15] Зедгенизова Маргарита",
  "HimerZERO": "[Н18] Чернышов  Игнат",
  "Fedorshebanin": "[Н18] Шебанин Фёдор",
  "ventilator13": "[Н17] Ильин Михаил",
  "H235": "[Н17] Жеглов Александр",
  "average_treap_enjoyer": "[Н15] Балакин Владимир",
  "vdxz": "[Н16] Черников Владислав",
  "Georggg999": "[Н17] Степанян Георгий",
  "VAntonuk": "[Н16] Антонюк Вадим",
  "EnderMaster": "[Н15] Шубин Матвей",
  "xfloud": "[Н18] Прыгунов Ярослав",
  "IGlazkovI": "[Н17] Глазков Илья",
  "nya.qin.": "[Н16] Шейкис Марк",
  "lerasimus": "[Н17] Соболев Олег",
  "KoT_OsKaR": "[Н16] Шабаров Игорь",
  "alexvezh": "[Н16] Вежновец Александр",
  "sirazeev": "[Н15] Сиразеев Ильяс",
  "Hectonit": "[Н15] Егоров Тимофей",
  "cup_of_coffee": "[Н15] Кудашев Фёдор",
  "arseny2606": "[Н16] Порхунов Арсений",
  "_Mister_Doctor": "[Н16] Бессолицын Максим",
  "sputn1k": "[Н16] Свирид Егор",
  "sdyakonov": "[Н15] Дьяконов Сергей",
  "glooooby": "[Н16] Малышев Игорь",
  "tikhon_grinev": "[Н17] Гринев Тихон",
  "EJIC_B_KEDAX": "[Н15] Кузнецов Иван",
  "average_treap_enjoyer": "[Н15] Балакин Владимир",
  "AntonMordakin": "[Н17] Мордакин Антон",
  "s1r_D": "[Н16] Шакиров Идрис"
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
