function initMap() {
    var lat = Number($('#lat').text());
    var lng = Number($('#lng').text());
    console.log(lng)
    console.log(lat)
    var center = {lat: lat, lng: lng };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: center,
        scrollwheel: false
    });
    var contentString = `
      <strong>{{campground.name}}<br />
      {{campground.location}}</strong>
      <p>{{ campground.description}}</p>
    `
    var infowindow = new google.maps.InfoWindow({
      content: contentString
    });
    var marker = new google.maps.Marker({
        position: center,
        map: map
    });
    marker.addListener('click', function() {
      infowindow.open(map, marker);
    });
  }