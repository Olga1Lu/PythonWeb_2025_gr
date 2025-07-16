//получить доступ к кнопке
const topBtn = document.querySelector(".go-top")

//скроллинг окна
window.addEventListener("scroll", trackScroll);
//реакция на нажатие
topBtn.addEventListener("click", goTop);

function trackScroll() {
// вычисляем положение от верхушки окна
const scrolled = window.pageYOffset;
//console.log(scrolled)  для отладки в браузере (f12)
//высота окна браузера
const wh = document.documentElement.clientHeight; // размер клиентской области окна браузера
//console.log(wh)
//если в прокрутке вышли за пределы одного экрана, то делаем:
if(scrolled > wh) {  //должна показаться кнопка
    /*topBtn.classList.add("go-top--show");*/
    topBtn.style.display = 'block'
    } else {
//или исчезает если прокрутили больше, чем один экран
        //topBtn.classList.remove("go-top--show");
        topBtn.style.display = 'none'
            }
}

function goTop() {
// пока не дошли до верха страницы
    if (window.pageYOffset > 0) {
// скроллим к верху
window.scrollBy(0, -50);  // по y на 50 пикселей вверх
setTimeout(goTop, 0)  //рекурсивный вызов самой себя через задержку во времени
    }
}
