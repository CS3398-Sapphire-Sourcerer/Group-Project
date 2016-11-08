/**
 * Created by Casey on 11/3/2016.
 */
//this holds the home page map that is is found in index.html
//colors (hex):
//black:  #000000
//gold:   #ffd700
// //maroon: #800000
//
// function appMap() {
//     var mapOptions = {
//         center: new google.maps.LatLng(29.8893, -97.9402),
//         zoom: 17,
//         scrollwheel: true,
//         disableDoubleClickZoom: true,
//         mapTypeId: google.maps.MapTypeId.HYBRID
//     };
//     var map = new google.maps.Map(document.getElementById("map"), mapOptions);
// };
// var drawingManager = new google.maps.drawing.DrawingManager({
//     drawingMode: google.maps.drawing.OverlayType.POLYGON,
//     drawingControl: true,
//     drawingControlOptions: {
//       position: google.maps.ControlPosition.RIGHT_CENTER,
//       drawingModes: ['marker', 'circle', 'polygon', 'polyline', 'rectangle']
//     },
//     markerOptions: {icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'},
//     circleOptions: {
//       fillColor: '#ffff00',
//       fillOpacity: 1,
//       strokeWeight: 5,
//       clickable: true,
//       editable: true,
//       zIndex: 1
//     }
//   });
//   drawingManager.setMap(map);
// }
//
// var derrickCoordinates = [
//     { lat:29.889579, lng:-97.942417 },
//     { lat:29.888962, lng:-97.942326 },
//     { lat:29.888970, lng:-97.942107 },
//     { lat:29.889264, lng:-97.942159 },
//     { lat:29.889313, lng:-97.941819 },
//     { lat:29.889646, lng:-97.941899 },
//     { lat:29.889579, lng:-97.942417 }
// ];
//
// var Derrick = new google.maps.Polygon({
//     paths: derrickCoordinates,
//     strokeColor: '#800000' //color: maroon
// });
//
// Derrick.setMap(map);

      // This example requires the Drawing library. Include the libraries=drawing
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=drawing">

      function appMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 8
        });

        var drawingManager = new google.maps.drawing.DrawingManager({
          drawingMode: google.maps.drawing.OverlayType.MARKER,
          drawingControl: true,
          drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            drawingModes: ['marker', 'circle', 'polygon', 'polyline', 'rectangle']
          },
          markerOptions: {icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'},
          circleOptions: {
            fillColor: '#ffff00',
            fillOpacity: 1,
            strokeWeight: 5,
            clickable: false,
            editable: true,
            zIndex: 1
          }
        });
        drawingManager.setMap(map);
      }