const all = document.querySelector('#all'), signBtn = document.querySelector('.signBtn');


function allCheck(event){
    console.log(event.target);
    if( $('#all').is(':checked') ){
        $("input[name=else]").prop("checked", true);
    } else {
        $("input[name=else]").prop("checked", false);
    }
}

function sign(event){
    if ( $('input:checkbox[name="else"]:checked').length == 3){
        prompt("비밀번호를 입력해주세요")
    } else {
        alert("모든 약관에 동의해주세요.")
    }
}

function init(){
    all.addEventListener("click", allCheck);
    signBtn.addEventListener("click", sign);
}

init();