/**
 * Created by Casey on 10/27/2016.
 */



function enterBuilding(userID, buildingID) {
    let building = {'userID' : userID, 'buildingID' : buildingID};
    console.log(building);
}



/*
var io = require('socket.io')(80);

io.on('connection', function (socket) {
  socket.on('ferret', function (name, fn) {
    fn('woot');
  });
});
 */