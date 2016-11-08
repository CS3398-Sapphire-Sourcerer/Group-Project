/**
 * Created by Casey on 10/27/2016.
 */

socket.on('connect', function() {console.log("Connected")});


socket.on('disconnect', function(){console.log("Disconnected")});


socket.on('inBuilding', inBuilding);
function inBuilding(obj) {
    console.log("In inBuilding");
    if (obj.buildingID != -1) {
        console.log("Good building ID");
        socket.emit("generateQuestions", {"buildingID": obj.buildingID});
    }
}


socket.on('question', function () {});
socket.on('answerReturn', function () {});
socket.on('stateUpdate', function () {});