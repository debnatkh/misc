function replaceTextOnPage(from, to){
  getAllTextNodes().forEach(function(node){
    node.nodeValue = node.nodeValue.replace(new RegExp(quote(from), 'g'), to);
  });
  function getAllTextNodes(){
    var result = [];
    (function scanSubTree(node){
      if(node.childNodes.length) 
        for(var i = 0; i < node.childNodes.length; i++) 
          scanSubTree(node.childNodes[i]);
      else if(node.nodeType == Node.TEXT_NODE) 
        result.push(node);
    })(document);
    return result;
  }
  function quote(str){
    return (str+'').replace(/([.?*+^$[\]\\(){}|-])/g, "\\$1");
  }
}

try {
  document.querySelector('.standings tbody tr th:nth-of-type(2)').style.width='200px';
} catch (error) {
  console.error(error);
}


replaceTextOnPage('a.nasretdinov', 'Насретдинов Амир')
replaceTextOnPage('AndreyPavlov', 'Павлов Андрей')
replaceTextOnPage('kolomig0r', 'Коломиец Игорь')
replaceTextOnPage('yaaarseny', 'Ятчений Арсений')
replaceTextOnPage('T4M0FEY', 'Ижицкий Тимофей')
replaceTextOnPage('H235', 'Жеглов Александр')
replaceTextOnPage('IGlazkovI', 'Глазков Илья')
replaceTextOnPage('UhahaUhaha', 'Яшкин Роберт')
replaceTextOnPage('meowcneil', 'Макнил Александр')
replaceTextOnPage('ArtemUstimenko', 'Устименко Артём')
replaceTextOnPage('127.0.0.1', 'Авдеев Дмитрий')
replaceTextOnPage('2020TAndr', 'Тунёв Андрей')
replaceTextOnPage('nya.qin.', 'Шейкис Марк')
replaceTextOnPage('Rodionno', 'Кунакбаев Родион')
replaceTextOnPage('systy', 'Возмилов  Георгий')
replaceTextOnPage('Son_of_Dijkstra', 'Хамитов Хаким')
replaceTextOnPage('t.ravnushkin', 'Равнушкин Тимофей')
replaceTextOnPage('tiom4eg', 'Туревич Артём')
replaceTextOnPage('lerasimus', 'Соболев Олег')
replaceTextOnPage('s1r_D', 'Шакиров Идрис')
replaceTextOnPage('_shakespeare_', 'Зарубин  Егор')
replaceTextOnPage('average_treap_enjoyer', 'Балакин Владимир')
replaceTextOnPage('Sokol080808', 'Сокольников Алексей')
replaceTextOnPage('akritovandrey', 'Акритов Андрей')
replaceTextOnPage('yaroslav_n', 'Ноздрин Ярослав')
replaceTextOnPage('makrav', 'Кравченко Максим')
replaceTextOnPage('VolkovMA', 'Волков Михаил')
replaceTextOnPage('zwezdinv', 'Звездин Владимир')
replaceTextOnPage('Grigoreva-Irina', 'Григорьева Ирина')
replaceTextOnPage('average_treap_enjoyer', 'Балакин Владимир')
replaceTextOnPage('anadere', 'Антонова Анна')
replaceTextOnPage('Prokhor08', 'Иголкин Прохор')
replaceTextOnPage('molney', 'Ходыкин Тимофей')
replaceTextOnPage('Mishazher', 'Жерневский Михаил')
replaceTextOnPage('vdxz', 'Черников Владислав')
replaceTextOnPage('_MatMath_', 'Маевский Матвей')
replaceTextOnPage('zhiganov_v', 'Жиганов Владислав')
replaceTextOnPage('Blinov_Artemii', 'Блинов Артемий')
replaceTextOnPage('Georggg999', 'Степанян Георгий')
replaceTextOnPage('pervuneckih.v.2025', 'Первунецких Еремей')
replaceTextOnPage('Kapitar', 'Ким Артём')
replaceTextOnPage('VAntonuk', 'Антонюк Вадим')
replaceTextOnPage('Daughter_of_Dijkstra', 'Желтовский Владислав')
replaceTextOnPage('sputn1k', 'Свирид Егор')
replaceTextOnPage('ArSarapkin', 'Сарапкин Артём')
replaceTextOnPage('KoT_OsKaR', 'Шабаров Игорь')
replaceTextOnPage('vl342', 'Бурмистров Владислав')
replaceTextOnPage('EnderMaster', 'Шубин Матвей')
replaceTextOnPage('_dmitriy_makarov_', 'Макаров Дмитрий')
replaceTextOnPage('MaxBalakirev', 'Балакирев Максим')
replaceTextOnPage('Noinoiio', 'Любин Михаил')
replaceTextOnPage('nek12312378', 'Минасян Никита')
replaceTextOnPage('SugarDadGG', 'Хамитов Галим')
replaceTextOnPage('lunaTu', 'Левина Мария')
replaceTextOnPage('IvanD', 'Девятьяров Иван')
replaceTextOnPage('sdyakonov', 'Дьяконов Сергей')
replaceTextOnPage('alexvezh', 'Вежновец Александр')
replaceTextOnPage('sirazeev', 'Сиразеев Ильяс')
replaceTextOnPage('prosrun', 'Солдатов Максим')
replaceTextOnPage('__Foam', 'Голиков Егор')
replaceTextOnPage('Mr_Ell', 'Гаврилов Максим')
replaceTextOnPage('Noobish_Monk', 'Беляев Марк')
replaceTextOnPage('Mizev_Andrey', 'Мизев Андрей')
replaceTextOnPage('glooooby', 'Малышев Игорь')
replaceTextOnPage('xfloud', 'Прыгунов Ярослав')
replaceTextOnPage('Tadfo', 'Файзуллин Андрей')
replaceTextOnPage('makcvim', 'Солдатов Максим')
replaceTextOnPage('polosatic', 'Ожегов Леонид')
replaceTextOnPage('kiquxd', 'Кобзев Андрей')
replaceTextOnPage('aone_A1', 'Кононов Олег')
replaceTextOnPage('MaSkA05', 'Скрипник Максим')
replaceTextOnPage('Hectonit', 'Егоров Тимофей')
replaceTextOnPage('tch1cherin', 'Чичерин Тимофей')
replaceTextOnPage('zog34bro', 'Макаров Михаил')
replaceTextOnPage('_IVON_', 'Пономарев Иван')
replaceTextOnPage('tikhon_grinev', 'Гринев Тихон')
replaceTextOnPage('Margaret07', 'Зедгенизова Маргарита')
replaceTextOnPage('cup_of_coffee', 'Кудашев Фёдор')
replaceTextOnPage('EJIC_B_KEDAX', 'Кузнецов Иван')
replaceTextOnPage('RomkaRS', 'Шумилов Роман')
replaceTextOnPage('Pavarishko', 'Мотыгуллин Карим')
replaceTextOnPage('GGFu87', 'Пучков Пётр')
replaceTextOnPage('hero_of_math_and_magic', 'Бацын Тимофей')
replaceTextOnPage('Nil2007', 'Иванов Нил')
replaceTextOnPage('Timur2006', 'Лузгов Тимур')
replaceTextOnPage('EvgenyUtkin', 'Уткин Евгений')
replaceTextOnPage('Egakrut3', 'Кривов Георгий')
replaceTextOnPage('HimerZERO', 'Чернышов  Игнат')
replaceTextOnPage('goodbee', 'Лещинский Артём')
replaceTextOnPage('iNNNo', 'Сыздыков Константин')
replaceTextOnPage('Greg908', 'Новгородцев Григорий')
replaceTextOnPage('arseny2606', 'Порхунов Арсений')
replaceTextOnPage('hoshiii', 'Хаев Булат')
replaceTextOnPage('Fedorshebanin', 'Шебанин Фёдор')
replaceTextOnPage('YseraKon', 'Коновалов Ярослав')
replaceTextOnPage('ventilator13', 'Ильин Михаил')
replaceTextOnPage('bibikov1', 'Бибиков Александр')
replaceTextOnPage('AntonMordakin', 'Мордакин Антон')
replaceTextOnPage('Smurf_with_me', 'Волков Алексей')
replaceTextOnPage('zhukovaliza', 'Жукова Елизавета')
replaceTextOnPage('svorogaze', 'Загоровский Владимир')
