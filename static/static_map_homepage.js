//this holds the home page map that is is found in index.html

function myMap() {
    var mapOptions = {
        center: new google.maps.LatLng(29.8893, -97.9402),
        zoom: 17,
        scrollwheel: false,
        disableDoubleClickZoom: true,
        mapTypeId: google.maps.MapTypeId.HYBRID
    }
var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}