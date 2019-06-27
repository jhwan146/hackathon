const house = document.querySelector(".house");

function menuPage(event){
    console.log(event.target);
    location.replace("./menu.html")
}


function init(){
    house.addEventListener("click", menuPage);
}

init();