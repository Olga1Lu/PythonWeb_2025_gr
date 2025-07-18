//скрипт sampl.js
/**********************
Здесь некоторые элементы языка
подробнее здесь:  https:/learn.javascript.ru
**********************************/
/*
//Функция
function sayHello(name) {
document.writeln("Вас зовут" + name);
}
// переменная var или let
/*let name = prompt("Ваше имя: ");
sayHello(name); */
//Массив
//let colors = ["Красный","Синий","Голубой"];

/* document.writeln("<h1>Цвета</h1><ul>");
//цикл for
    for(let i=0; i<colors.length; i++) {
document.writeln("<li>" + colors[i] + "</li>")
}
document.writeln("</ul>") */

//function changeColor() {
// document.getElementById('alive').style.color = 'red'
   /* const txt = document.getElementById('alive');
    if(txt.style.display === 'none') { //display - отображает элемент
    txt.style.display = block;
    } else {
    txt.style.display = 'none'; //скрывает элемент по нажатию
    }
}

//Подключаюсь к эл-ту DOM
const txt = document.getElementById('alive').onclick = clickFunc;
