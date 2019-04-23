$(document).ready(function(){
  $('.dropdown-trigger').dropdown();

  $('.sidenav').sidenav();

  $('.collapsible').collapsible();
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
