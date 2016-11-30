/**
 * Created by Casey on 11/3/2016.
 */
//this holds the home page map that is is found in index.html
//colors (hex):
// black:  #000000
// gold:   #ffd700
// maroon: #800000
//



function appMap () {
    console.group("appMap() [appMap.js]");

    var mapOptions = {
        center: new google.maps.LatLng(29.8893, -97.9402),
        disableDefaultUI : true,
        zoom: 18,
        scrollwheel: true,
        disableDoubleClickZoom: true,
        mapTypeId: google.maps.MapTypeId.roadmap
    };
    
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    google.maps.event.addListener(map, 'center_changed', function() {
        if (allowedBounds.contains(map.getCenter())) {
        // still within valid bounds, so save the last valid position
            lastValidCenter = map.getCenter();
            return; 
        }
        else {
            map.panTo(lastValidCenter);
        }
    });

    // not valid anymore => return to last valid position

    lastValidCenter = map.getCenter();
    console.log(lastValidCenter)

    console.groupEnd();
}

// bounds of the desired area

function addBuildings(obj) {
    console.group("addBuildings(obj) [appMap.js]");
    for (let i = 0; i < obj["buildings"].length; i++) {
        buildings.push({
            "buildingName":obj["buildings"][i].buildingName,
            "buildingTag":obj["buildings"][i].buildingTag,
            "coords":obj["buildings"][i].coordinates});
    }
    renderAllTheBuildings();
    console.groupEnd();
}

function renderAllTheBuildings() {
    console.group("renderAllTheBuildings() [appMap.js]");
    for (let i = 0; i < buildings.length; i++) {
        let buildingCoords = buildings[i].coords;
        var currentBuilding = new google.maps.Polygon({
            paths: buildingCoords,
            strokeColor: '#ffffff', //color: maroon
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#add8e6',
            fillOpacity: 0.55
        });
        currentBuilding.setMap(map);
        currentBuilding.buildingTag = buildings[i].buildingTag;
        buildingPolygons.push(currentBuilding);

        google.maps.event.addListener(currentBuilding, 'click', function (event) {
            alert(buildings[i].buildingName);
        });  
    }
    console.groupEnd();
}

function checkBuildingBounds(position) {
    console.group("checkBuildingBounds(position) [appMap.js]");
    for (let i = 0; i < buildingPolygons.length; i++) {
        console.log("position : ", position);
        console.log(".latitude : ", position.latitude);
        console.log(".longitude : ", position.longitude);
        console.log("buildingPolygons[i] : ", buildingPolygons[i]);
        console.log(google.maps.geometry.poly.containsLocation(
            new google.maps.LatLng(position.latitude, position.longitude), buildingPolygons[i]));
        if (google.maps.geometry.poly.containsLocation(
            new google.maps.LatLng(position.latitude, position.longitude), buildingPolygons[i])) {
            console.log(buildingPolygons[i].buildingTag);
            return buildingPolygons[i].buildingTag;
        }
    }
    return "";
    console.groupEnd();
}

function findVisiblePolygons(loc) {
    for (let i = 0; i < buildings.length; i++) {
    }
}

function updateMap(obj) {
    for (let i = 0; i < obj.length; i++) {
        /*
        let bldg = new google.maps.Polygon({
            paths :
        })
        */

    }
}





    /*

    .toLowerCase()
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

    */