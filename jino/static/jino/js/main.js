$(document).ready(function () {
    $('.dropdown-trigger').dropdown();

    $('.sidenav').sidenav();

    $('.collapsible').collapsible();
});

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
