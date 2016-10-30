/**
 * Created by Casey on 10/27/2016.
 */

(function addTimer() {
    window.setInterval(geolocateUser, 10000);
})();

function fireLocationUpdate(position) {
    let coords = position.coords;
    let lat = position.coords.latitude;
    let long = position.coords.longitude;

    console.log("fireLocationUpdate");

    var myRequest = new XMLHttpRequest(),
        method = "POST",
        user = 1,
        url = "updatePos",
        urlString = url + "/" + user + "/" + lat + "/" + long;

    myRequest.open(method, urlString);
    myRequest.onreadystatechange = function () {
        if (myRequest.readyState == XMLHttpRequest.DONE && myRequest.status == 200) {
            console.log(myRequest.responseText);
        }
    }

    myRequest.send();
}

function fireXMLHTTPRequest() {
    console.log("fireXMLHttpRequest");
    var myRequest = new XMLHttpRequest(),
        method = "GET",
        url = "cjsTest2";

    myRequest.responseType = "text";
    myRequest.open(method, url);

    myRequest.onreadystatechange = function () {
        if (myRequest.readyState == XMLHttpRequest.DONE && myRequest.status == 200) {
            console.log(myRequest.responseText);
        }
    }

    myRequest.send();
}

function geolocateUser() {
    navigator.geolocation.getCurrentPosition(fireLocationUpdate);
}