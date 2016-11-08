/**
 * Created by Casey on 10/27/2016.
 */

socket.on('connect', function() {console.log("Connected")});


socket.on('disconnect', function(){console.log("Disconnected")});

function sendLocation(position) {
    socket.emit("changeLocation", locationObj);
}

socket.on('enterBuilding', inBuilding);
function inBuilding(obj) {
    console.log("In inBuilding");
    if (obj.building != -1) {
        console.log("Good building ID");

        var sendObj = {};
        sendObj.userID = userID;
        sendObj.buildingID = obj.building;

        socket.emit("generateQuestions", sendObj);
    }
}


socket.on('question', writeQuestionBar);
function writeQuestionBar(obj) {
    console.log("writeQuestionBar");
    console.log("Received : ", obj);
}

// This will be the target of a click handler in a form or however we
// decide to do it for submitting your answer
function sendAnswer(ans) {
    socket.emit("answer", ans);
}

socket.on('result', function () {});
socket.on('qLimit', function () {});
socket.on('stateUpdate', function () {});