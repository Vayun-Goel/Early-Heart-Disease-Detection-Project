document.addEventListener("DOMContentLoaded", function() {
    const heart_button = document.querySelector("#vayunbutton1");
    var heart_card = document.getElementsByClassName("div_card_mine_heart")[0];
    var form_name = document.getElementsByClassName("form_for_heart")[0];
    const home_button=document.querySelector("#homebutton");

    heart_button.onclick = gotoform;

    home_button.onclick=reset_settings;

    function gotoform() {
        heart_card.style.display = "none";
        form_name.style.display = "block";
    }

    function reset_settings(){
        heart_card.style.display = "block";
        form_name.style.display = "none";
        console.log("Hello");
    }
});
