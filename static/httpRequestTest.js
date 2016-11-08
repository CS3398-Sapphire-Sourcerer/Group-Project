/**
 * Created by Casey on 10/27/2016.
 */

function sendLocation(locationObj) {
    console.log("Getting to sendLocation");
    socket.emit('changeLocation', locationObj);
}
0
function geolocateUser(userID, locationObj) {
    console.log("geolocateUser");
    console.log("userID : ", userID);
    navigator.geolocation.getCurrentPosition(function (position) {
        locationObj.uid = userID;
        locationObj.latitude = position.coords.latitude;
        locationObj.longitude = position.coords.longitude;
        sendLocation(locationObj)
    });
}