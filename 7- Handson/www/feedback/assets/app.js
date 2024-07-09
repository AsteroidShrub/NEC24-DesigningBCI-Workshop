'use strict';

var audio = new Audio('assets/satie.mp3');
audio.addEventListener('ended', function() {
    this.currentTime = 0;
    this.play();
}, false);
audio.play();

// Connect to socket
let io = new IO();

// Subscribe to data stream
io.subscribe('relaxlevel');

io.on('relaxlevel', (data) => {
    if(data[0] == 1){
        audio.volume += 0.1 
    }
});
