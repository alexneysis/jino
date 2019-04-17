$(document).ready(function(){
  $('.dropdown-trigger').dropdown();

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
