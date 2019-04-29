$(document).ready(function () {
    // $('.dropdown-trigger').dropdown();

    $('.sidenav').sidenav();

    $('.collapsible').collapsible();

    $('.modal').modal();
});

var nearest = false;
var nearestClick = 0;
$(".switch").on("click", function(e) {
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

$("#phoneField").mask("+7 (999) 999 - 99 - 99", {placeholder: "-" }); //Подключение маски

$(".collection-item").on("click", function () {
    var result = $(this).text().substring(12);
    var URL = "https://jino24.ru/clinic/send";
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    console.log(result);


    $.ajax({
        url: URL,
        type: "POST",
        data: {name: result},
        dataType: "text",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (response) {
            console.log("Success response" + " " + result);
        },
        error: function (response) {
            console.log("Error in method");
        }
    });
});


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
