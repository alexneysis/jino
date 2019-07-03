$(document).ready(function () {
    $('.sidenav').sidenav();

    $('.collapsible').collapsible();

    $('.modal').modal({
        //При закрытии формы изменить статус на 20 и обновить список
        onCloseEnd: function () {
            $.ajax({
                url: "https://jino24.ru/clinic/wait",
                type: "POST",
                data: {patientId: $("#patientModalId").val()},
                dataType: "text"
            });
            updateMessages;
        }
    });

    $('.carousel.carousel-slider').carousel({
        // fullWidth: true,
        indicators: true
    });
});

var nearest = false;
var nearestClick = 0;
$(".switch").on("click", function (e) {
    nearestClick++;
    if (nearestClick == 2) {
        console.log("НАЖАЛИ");
        nearest = !nearest;
        if (nearest) {
            $(".nearestField").show();
        } else {
            $(".nearestField").hide();
        }
        nearestClick = 0;
    }
});

try { //Выполняется функция, если maskedinput подеключен
    $("#phoneField").mask("+7 (999) 999 - 99 - 99", {placeholder: "-"}); //Подключение маски
} catch (e) {
    //Просто пропускается эта строка, если не подключен
}

$(".callBtn").on("click", function (e) {
    $(".popupSection").show();
});

var closeIconFlag = false;
var formFlag = false;

$(".popupSection").on("click", function () {
    if (formFlag) {
        if (closeIconFlag) {
            $(".popupSection").hide();
        } else {
            return 0;
        }
    } else {
        $(".popupSection").hide();
    }
    closeIconFlag = false;
    formFlag = false;
});

$(".popupFormBlock").on("click", function () {
    formFlag = true;
});

$(".closeIcon").on("click", function () {
    closeIconFlag = true;
});

$("#iframe1").




