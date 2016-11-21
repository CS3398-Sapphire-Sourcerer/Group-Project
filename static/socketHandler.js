/**
 * Created by Casey on 10/27/2016.
 */

socket.on('connect', function() {
    console.log("Connected")
});


socket.on('disconnect', function(){console.log("Disconnected")});

function requestState() {
    console.log(" === requestState === ")
    socket.emit("ready", {});
}

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

    var sendObj = obj;

    document.getElementById("q_text_1").textContent = obj.question_data.question.questionText;
    document.getElementById("q_text_1").value = obj.question_data.question.questionID;


    for (var i = 0; i < obj.question_data.answer_list.length; i++) {
        document.getElementById("answer" + i).textContent = obj.question_data.answer_list[i].answerText;
        document.getElementById("answer" + i).value = obj.question_data.answer_list[i].answerID;
    }
}


socket.on('result', writeResult);
function writeResult(result) {
    alert (result);
}

function emitAnswer(buttonObj) {
    console.log("emitAnswer");

    var id = (document.getElementById(buttonObj).value).toString();
    var quid = (document.getElementById("q_text_1").value).toString();
    var submit = {
        "userAnswerId" : id,
        "questionId" : quid
    }
    //var userAnswerId = buttonObj.value;
    //var questionId = document.getElementById("q_text_1").value;

    socket.emit("answer", submit);
}

function testButtonValue(buttonObj) {
    alert(buttonObj.value);
}

// This will be the target of a click handler in a form or however we
// decide to do it for submitting your answer
function sendAnswer(ans) {
    socket.emit("answer", ans);
}

socket.on('result', function () {});
socket.on('qLimit', function () {});

socket.on('stateFullUpdate', stateFullUpdate);
function stateFullUpdate(obj) {
    console.log("Received state update");
    console.log(obj);
    addTimer();
    updateMap(obj.buildings);
}

socket.on('stateUpdate', function () {});