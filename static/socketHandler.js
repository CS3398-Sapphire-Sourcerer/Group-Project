/**
 * Created by Casey on 10/27/2016.
 */


socket.on('inBuilding', inBuilding);
function inBuilding(obj) {
    console.log("In inBuilding");
    let building = obj;
    console.log(building);
}


socket.on('connect', function() {console.log("Connected")});

socket.on('disconnect', function(){console.log("Disconnected")});

socket.on('questions', function () {});

socket.on('answerReturn', function () {});
