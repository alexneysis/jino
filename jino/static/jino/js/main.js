$(".toothBtn").on("click", function() {
  $(".formContainer").show();
  $(".formBlock").css("display", "flex");
});
$(".subLink").on("click", function() {
  $(".subFormContainer").show();
  $(".formBlock").css("display", "flex");
});
var notClose = 0;
$(".formBlock").on("click", function() {
  if (notClose == 1) {
    notClose = 0;
  } else {
    $(".sendFormBlock input").val("");
    $(this).hide();
    $(".subFormContainer").hide();
    $(".formContainer").hide();
    notClose = 0;
  }

});
$(".formContainer").on("click", function() {
  notClose = 1;
});
$(".subFormContainer").on("click", function() {
  notClose = 1;
});

$("#telephone").mask("+7 (999) 99 - 99 - 999", {placeholder: "-" });