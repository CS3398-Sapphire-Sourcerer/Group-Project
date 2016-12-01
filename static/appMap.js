/**
 * Created by Casey on 11/3/2016.
 */
//this holds the home page map that is is found in index.html
//colors (hex):

/* DATABASE ORDER : 1, 2, 3 */
// maroon: #800000
// black:  #000000
// gold:   #ffd700


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


// maroon: #800000
// black:  #000000
// gold:   #ffd700
function getAssociatedColor(teamID) {
    // This prints a hundred billion times. No. Not right now. Uncomment if 
    // you are worried about this function
    //console.group("getAssociatedColor(teamID) [appMap.js]");
    //console.groupEnd();
    return ( teamID == 1 ? '#800000' : 
        teamID == 2 ? '#000000' :
        teamID == 3 ? '#ffd700' : 
        '#add8e6' );
}

function updateMap(obj) {
    console.group("updateMap(obj) [appMap.js]");
    for (let i = 0; i < obj.buildings.length; i++) {
        let index = buildingPolygons.findIndex(function (element) {
            return (element.buildingTag == obj.buildings[i].buildingTag)
        });
        //console.log(index);
        //console.log(obj.buildings[i]);
        //console.log(obj.buildings[i].buildingOwner);
        //console.log(typeof (obj.buildings[i].buildingOwner));
        let color = getAssociatedColor(obj.buildings[i].buildingOwner);
        //console.log("color : ", color);
        buildingPolygons[index].strokeColor = color;
        buildingPolygons[index].fillColor = color;
        buildingPolygons[index].fillOpacity = color == '#add8e6' ? 0.55 : 80;
        buildingPolygons[index].setMap(map);
    }
    console.groupEnd();
}

/*
function isBigEnough(element) {
  return element >= 15;
}

[12, 5, 8, 130, 44].find(isBigEnough);
*/

