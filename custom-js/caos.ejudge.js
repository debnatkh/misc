var regex = new RegExp("(kr0*)|(sm02-5)|(ku0[1-6])", );

var elements = document.getElementsByClassName('probOk');

for (var i = 0; i < elements.length; i++){
    elements[i].style.display = 'none';
}


elements = document.getElementsByClassName('probBad');
for (var i = 0; i < elements.length; i++){
    if (regex.test(elements[i].innerText)){
        elements[i].style.display = 'none';
    } 
}

elements = document.getElementsByClassName('probEmpty');
for (var i = 0; i < elements.length; i++){
    if (regex.test(elements[i].innerText)){
        elements[i].style.display = 'none';
    } 
}
