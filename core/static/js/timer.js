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

        document.getElementById("progressBar").value = 600 - (600 - diff);

        display.textContent = minutes + ":" + seconds + " min"; 

        if(diff<=0)
        {
            display.style.color="red";
            accept_payments=false;
            clearInterval(intervalId);
            document.getElementById("bnomics-order-expired-wrapper").style.display = "block";
            document.getElementById("bnomics-order-wrapper").style.display = "none";
        }    
    }
    timer();
}
