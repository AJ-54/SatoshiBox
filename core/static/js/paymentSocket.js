var csrftoken = document.querySelector("input[name=csrfmiddlewaretoken]").value
var socket = new WebSocket("wss://www.blockonomics.co/payment/"+ address);


const paymentStatusUpdate = (status)=>{
  (async()=>{
    const websiteUrl = "http://fileshop.online"; //Change this for your website
    let payment_id=data["payment_id"];
    try{
    const response = await fetch(websiteUrl + data.url,{
      "method":"POST",
      "body":JSON.stringify({status,payment_id}),
      "headers": {
            "Accept": "application/json , text/plain ,*/*",
            "Content-type": "application/json",
              "X-CSRFToken": csrftoken
          },
      })
    
    if(response.redirected&&accept_payments)
    {
        window.location.assign(response.url);
    }
    }catch(err){
       console.log("err",err)
    }
   }
  )();

}



socket.onmessage = function(event){
    response = JSON.parse(event.data);
    if (parseInt(response.status) >=0&&accept_payments){
      console.log("Sending request")
       setTimeout(paymentStatusUpdate(response.status), 1000);  
    } 
}