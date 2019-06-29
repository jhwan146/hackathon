const Step1 = document.querySelector(".Step"), Step2 = document.querySelector(".Step2"), Step3 = document.querySelector(".Step3");


function NextPage(event){
    console.log(event.target);
    location.replace("./../loading/");
}

function insertTable(event) {
    Step3.style.visibility="visible";
    var s3p = document.createElement("p");
    s3p.innerHTML = "STEP 03. &nbsp&nbsp메뉴를 선택해주세요"
    var s3table = document.createElement("table");
    var s3tr = document.createElement("tr");
    var s3title = ["&nbsp&nbsp대출기한연장", "&nbsp&nbsp개인대출&nbsp금리인하요구권(별 빚이 내린다!)", 
    "&nbsp&nbsp대출한도감액", "&nbsp&nbsp대출한도해지", 
    "&nbsp&nbsp자동기한연장&nbsp동의", "&nbsp&nbsp금리신청내역서&nbsp조회"]
    for (i = 0; i < s3title.length; i++) {
        var name = "s3tr" + i;
        var name2 = "s3td" + i;
        var name = document.createElement("tr");
        var name2 = document.createElement("td");
        name2.innerHTML = s3title[i];
        name.appendChild(name2);
        s3table.appendChild(name);
    }
    console.log(s3table);
    
    Step3.appendChild(s3p);
    Step3.appendChild(s3table);

    s3table.addEventListener("click", NextPage);
}


function Step2Table() {
    var table2 = document.getElementById("insertTable");
    var tr = document.createElement("tr");
    var td1 = document.createElement("td");
    td1.innerHTML = "조회";
    var td2 = document.createElement("td");
    td2.innerHTML = "신청";
    var td3 = document.createElement("td");
    td3.innerHTML = "입금";

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);

    var tr2 = document.createElement("tr");
    var td4 = document.createElement("td");
    td4.innerHTML = "상환";
    var td5 = document.createElement("td");
    td5.innerHTML = "관리";
    var td6 = document.createElement("td");
    td6.innerHTML = "진행현황";

    tr2.appendChild(td4);
    tr2.appendChild(td5);
    tr2.appendChild(td6);

    table2.appendChild(tr);
    table2.appendChild(tr2);

    td5.addEventListener("click", insertTable);
}



