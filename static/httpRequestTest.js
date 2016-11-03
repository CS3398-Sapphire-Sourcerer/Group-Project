/**
 * Created by Casey on 10/27/2016.
 */

function fireLocationUpdate(position, userID) {
    console.log(position);
    console.log(userID);
    let coords = position.coords;
    let lat = position.coords.latitude;
    let long = position.coords.longitude;

    console.log("fireLocationUpdate");

    var myRequest = new XMLHttpRequest(),
        method = "POST",
        //user = 1,
        url = "updatePos",
        urlString = url + "/" + userID + "/" + lat + "/" + long;

    console.log(userID);
    myRequest.open(method, urlString, true);
    myRequest.onreadystatechange = function () {
        if (myRequest.readyState == XMLHttpRequest.DONE && myRequest.status == 200) {
            console.log(myRequest.responseText);
        }
    }

    myRequest.send();
}

function geolocateUser(userID) {
    console.log("A field of lies");
    console.log("geolocateUser");
    console.log("userID : ", userID);
    navigator.geolocation.getCurrentPosition(function (position) {
        fireLocationUpdate(position, userID);
    });
}