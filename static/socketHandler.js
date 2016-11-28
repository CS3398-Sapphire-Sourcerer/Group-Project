/**
 * Created by Casey on 10/27/2016.
 */

socket.on('connect', function() {
    console.log("Connected")
});

socket.on('disconnect', function(){console.log("Disconnected")});

function requestState() {
    console.group("requestState() [socketHandler.js]");
    socket.emit("ready", {});
    console.groupEnd();
}

function updateLocation(position) {
    console.group("sendLocation(position) [socketHandler.js]");
    if (lastLocation == locationObj) return 
    else if (lastLocation != locationObj)
        lastLocation = locationObj;
        socket.emit("changeLocation", locationObj);
    console.groupEnd();
}

socket.on('enterBuilding', inBuilding);
function inBuilding(obj) {
    console.group("inBuilding(obj) [socketHandler.js][listener]");
    if (obj.building != -1) {
        console.log("Good building ID");

        var sendObj = {};
        sendObj.userID = userID;
        sendObj.buildingID = obj.building;

        socket.emit("generateQuestions", sendObj);
    }
    console.groupEnd();
}


socket.on('question', writeQuestionBar);
function writeQuestionBar(obj) {
    console.group("writeQuestionBar(obj) [socketHandler.js][listener]");
    console.log("Received : ", obj);

    document.getElementById("q_text_1").textContent = obj.question_data.question.questionText;
    document.getElementById("q_text_1").value = obj.question_data.question.questionID;


    for (var i = 0; i < obj.question_data.answer_list.length; i++) {
        document.getElementById("answer" + i).textContent = obj.question_data.answer_list[i].answerText;
        document.getElementById("answer" + i).value = obj.question_data.answer_list[i].answerID;
    }
    console.groupEnd();
}

socket.on('noMoreQuestions', alertQuestionBar);
function alertQuestionBar(obj) {
    console.group("alertQuestionBar(obj) [socketHandler.js][listener]");

    console.log("Alert User:");
    console.log("Received : ", obj);

    document.getElementById("q_text_1").textContent = obj.result;
    document.getElementById("q_text_1").value = 0;

    console.groupEnd();
}


socket.on('result', writeResult);
function writeResult(result) {
    console.group("writeResult(result) [socketHandler.js][listener]");
    alert (result);
    console.groupEnd();
}


function emitAnswer(buttonObj) {
    console.group("emitAnswer(buttonObj) [socketHandler.js]");

    var id = (document.getElementById(buttonObj).value).toString();
    var quid = (document.getElementById("q_text_1").value).toString();
    var submit = {
        "userAnswerId" : id,
        "questionId" : quid
    };
    //var userAnswerId = buttonObj.value;
    //var questionId = document.getElementById("q_text_1").value;

    socket.emit("answer", submit);
    console.groupEnd();
}

function testButtonValue(buttonObj) {
    alert(buttonObj.value);
}

socket.on('qLimit', function () {});

socket.on('stateFullUpdate', stateFullUpdate);
function stateFullUpdate(obj) {
    console.group("stateFullUpdate(obj) [socketHandler.js][listener]");
    console.log("Received state update");
    console.log(obj);
    addTimer();
    updateMap(obj.buildings);
    console.groupEnd();
}

socket.on('stateUpdate', function () {});