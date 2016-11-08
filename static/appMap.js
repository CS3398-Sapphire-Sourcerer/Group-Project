/**
 * Created by Casey on 11/3/2016.
 */
//this holds the home page map that is is found in index.html
//colors (hex):
//black:  #000000
//gold:   #ffd700
// //maroon: #800000
//

function appMap () {
    var mapOptions = {
        center: new google.maps.LatLng(29.8893, -97.9402),
        zoom: 17,
        scrollwheel: true,
        disableDoubleClickZoom: true,
        mapTypeId: google.maps.MapTypeId.roadmap
    };
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var derrickCoordinates = [
        { lat:29.889579, lng:-97.942417 },
        { lat:29.888962, lng:-97.942326 },
        { lat:29.888970, lng:-97.942107 },
        { lat:29.889264, lng:-97.942159 },
        { lat:29.889313, lng:-97.941819 },
        { lat:29.889646, lng:-97.941899 },
        { lat:29.889579, lng:-97.942417 }
    ];

    var alkekCoordinates = [
        { lat:29.88844371604545, lng:-97.94277459383011},
        { lat:29.889341342614987, lng:-97.94293016195297},
        { lat:29.889294833664863, lng:-97.9433861374855},
        { lat:29.888397206676533, lng:-97.94323056936264},
        {lat: 29.88844371604545,lng: -97.94277459383011}
    ];

    var Derrick = new google.maps.Polygon({
        paths: derrickCoordinates,
        strokeColor: '#800000', //color: maroon
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#800000',
        fillOpacity: 0.65
    });

    var Alkek = new google.maps.Polygon({
        paths: alkekCoordinates,
        strokeColor: '#000000', //color: maroon
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#ffd700',
        fillOpacity: 0.65
    });

    Derrick.setMap(map);
    Alkek.setMap(map);
}





