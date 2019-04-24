$(document).ready(function(){
  $('.dropdown-trigger').dropdown();

  $('.sidenav').sidenav();

  $('.collapsible').collapsible();
});

$(".collection-item").on("click", function () {
  var result = $(this).text().substring(12);
  var striptURL = "https://jino24.ru/clinic/valid";
  console.log(result);

  $.ajax({
    url: scriptURL,
    type: "POST",
    dataType: "html",
    data: ({name: result}),
    success: function(response) {
      console.log(response);
    }
  });
});


$(".callBtn").on("click", function(e) {
  $(".popupSection").show();
});


var closeIconFlag = false;
var formFlag = false;

$(".popupSection").on("click", function() {
  if (formFlag) {
    if(closeIconFlag) {
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

$(".popupFormBlock").on("click", function() {
  formFlag = true;
});

$(".closeIcon").on("click", function() {
  closeIconFlag = true;
});
