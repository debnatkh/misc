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


replaceTextOnPage('Delusion88', 'Суринов Илья')
replaceTextOnPage('t.ravnushkin', 'Равнушкин Тимофей')
replaceTextOnPage('qin.', 'Шейкис Марк')
replaceTextOnPage('_MatMath_', 'Маевский Матвей')
replaceTextOnPage('YaNastya', 'Янко Анастасия')
replaceTextOnPage('dasha..zhilina', 'Жилина Дарья')
replaceTextOnPage('Illumina', 'Валиуллин Данис')
replaceTextOnPage('FedorKudashev', 'Кудашев Фёдор')
replaceTextOnPage('macneil', 'Макнил Александр')
replaceTextOnPage('YseraKon', 'Коновалов Ярослав')
replaceTextOnPage('Sokol080808', 'Сокольников Алексей')
replaceTextOnPage('molney', 'Ходыкин Тимофей')
replaceTextOnPage('_Astron', 'Щербаков Максим')
replaceTextOnPage('Significatio', 'Громыко Андрей')
replaceTextOnPage('artem__', 'Акулов Артём')
replaceTextOnPage('lunaTu', 'Левина Мария')
replaceTextOnPage('KoT_OsKaR', 'Шабаров Игорь')
replaceTextOnPage('RTashlanov', 'Ташланов Роман')
replaceTextOnPage('kolya13245', 'Гнусов Николай')
replaceTextOnPage('glooooby', 'Малышев Игорь')
replaceTextOnPage('vvzagorovskiy', 'Загоровский Владимир')
replaceTextOnPage('Margaret07', 'Зедгенизова Маргарита')
replaceTextOnPage('MrEssiorx', 'Иванов Семён')
replaceTextOnPage('xprezzzboi', 'Шабанов Тимофей')
replaceTextOnPage('vdxz', 'Черников Владислав')
