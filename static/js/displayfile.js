function set_loop() {
    var video = document.getElementById('video-wrapper');
    var videobtn = document.getElementById('video-loop-btn');
    if (typeof video.loop == 'boolean') {
        if (video.loop) {
            video.loop = false;
            videobtn.removeAttribute('style');
        } else {
            video.loop = true;
            videobtn.style.backgroundColor = "rgba(255,254,254,0.82)";
            videobtn.style.color = "black";
            videobtn.style.borderColor = "black"
        }
    } else { // loop property not supported
        video.addEventListener('ended', function () {
            this.currentTime = 0;
            this.play();
        }, false);
    }
}

function set_fullscreen() {
    var video = document.getElementById('video-wrapper');
    if (video.requestFullscreen) {
        video.requestFullscreen();
    } else if (video.webkitRequestFullscreen) {
        video.webkitRequestFullscreen();
    } else if (video.msRequestFullscreen) {
        video.msRequestFullscreen();
    }

}