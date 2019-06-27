const loginButton = document.querySelector(".loginButton");

function menuPage(event){
    console.log(event.target);
    location.replace("./menu.html")
}

function init(){
    loginButton.addEventListener("click", menuPage);
}

init();