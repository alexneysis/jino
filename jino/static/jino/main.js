$(document).ready(function(){
  if ($(window).scrollTop() > 335) {
    var mar = $(window).scrollTop() - 100;
    $("#movedBlock").css("margin-top", mar+"px");
  };
  $(window).scroll(function(){
    if ($(this).scrollTop() > 335) {
      var mar = $(window).scrollTop() - 100;
      $("#movedBlock").css("margin-top", mar+"px");
    } else {
      $("#movedBlock").css("margin-top", "235px");
    }
  });
});

ymaps.ready(function() {
  var mapCenter = [ 58.005142, 56.239653 ]

  var perm_map = new ymaps.Map("map_contacts", {
    center: [mapCenter[0], mapCenter[1]],
    zoom: 16,
    controls: ["zoomControl", "geolocationControl"],
    behaviors: ["drag"]
  });
  var placemark = new ymaps.Placemark([58.005142, 56.239653]);
  perm_map.geoObjects.add(placemark);
});
