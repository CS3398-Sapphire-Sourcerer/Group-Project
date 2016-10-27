/**
 * Created by Casey on 10/27/2016.
 */



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

/*
function addRequestHandler() {
    console.log("addRequestHandler");
    var el = document.getElementById("fireRequest");
    if (el.addEventListener)
        el.addEventListener("click", fireXMLHTTPRequest, false);
}
*/