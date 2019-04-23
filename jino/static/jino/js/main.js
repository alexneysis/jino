$(document).ready(function(){
  $('.dropdown-trigger').dropdown();

  $('.collapsible').collapsible();
});

$(".collection-item").on("click", function () {
  var result = $(this).text().substring(12);
  var URL = "https://jino24.ru/pool/send";
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  console.log(result);


  $.ajax({
    url: URL,
    type: "POST",
    data: {name: result},
    dataType: "text",
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    success: function(response) {
      console.log("Success response" + " " + result);
    },
    error: function (response) {
      console.log("Error in method");
    }
  });
});
