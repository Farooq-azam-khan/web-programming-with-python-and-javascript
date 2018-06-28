document.addEventListener("DOMContentLoaded", () =>{
  document.querySelector("#form").onsubmit = () => {
    // making ajax request for
    const request = new XMLHttpRequest();
    // getting value of currency
    const currency = document.querySelector('#currency').value; 
    console.log('getting exchange rate for ' + currency)
    // console.log(request)
    // initalize new request
    request.open('POST', '/convert');
    
    // when request is done
    request.onload = () => {
      const data = JSON.parse(request.responseText); 
      console.log(data)
      document.querySelector('#result').innerHTML = 'Fake data recieved: ' + data.rate
    }
    const data = new FormData();
    data.append('currency', currency); 
    // send req
    request.send(data); 
    return false; 
  }
}); 