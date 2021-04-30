var bottom_line = document.querySelector('#bottom_line');
let intervalId;

function startTimer(duration, display) {
    var start = Date.now(),
        diff,
        minutes,
        seconds;
    
    if(last_order){
        //reduce the 10 minutes duration by the time at which the given order was put in session
        duration-=((start-(new Date(parseInt(last_order)*1000)))/1000 | 0);
    }
    
    intervalId=setInterval(timer, 1000);

    function timer() {
    
        diff = duration - (((Date.now() - start) / 1000) | 0);
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + " minutes " + seconds+ " seconds"; 

        if(diff<=0)
        {
            display.style.color="red";
            accept_payments=false;
            bottom_line.textContent = "Please refresh the page to initiate payment again if you have already paid ,please wait till payment is processed"; 
            clearInterval(intervalId);
        }    
    }
    timer();
}
