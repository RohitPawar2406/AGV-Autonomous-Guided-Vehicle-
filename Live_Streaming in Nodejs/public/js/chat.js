
const socket = io()


socket.on('Sending',(message1)=>{
    console.log("Welcome to Chat Application")
    document.getElementById("img1").src="data:image/jpeg;base64,"+message1;
})

var controls = {vt:0 , hz:0}

const animate = function () {
    requestAnimationFrame( animate );
    socket.emit('input',controls)
    console.log(controls)
};

animate();

// Forward And Backward Direction. 
function fwOnDown(params) {
    controls.vt = 1;
}
function fwOnUp(params) {
    controls.vt=0;
}

function bkOnDown(params) {
    controls.vt = -1;
}

function bkOnUp(params) {
    controls.vt = 0;
}

// Left And Right Direction
function RightOnRight(params) {
    controls.hz = 1;
}
function RightOnNeutral(params) {
    controls.hz=0;
}

function LeftOnLeft(params) {
    controls.hz = -1;
}

function LeftOnNeutral(params) {
    controls.hz = 0;
}
/*
socket.on('Count-Updated', (count)=>{
    console.log('The Count has been Updated!!!',count)
})
*/
