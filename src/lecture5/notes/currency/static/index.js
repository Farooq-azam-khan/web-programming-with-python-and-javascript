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
})

// document.addEventListener('DOMContentLoaded', () => {
//   console.log("content loaded");
//   // when form is submitted
//   document.querySelector('#form').onsubmit = () => {
//     return false; 
//     // ceate an object that makes an http ajax request
//     // const request = new XMLHttpRequest(); 
//     // console.log('req: ' + request)
//     // // get the value of currency text field
//     // const currency = document.querySelector('#currency').value; 
//     // console.log('currency: ' + currency);
//     // // initalize new request
//     // request.open('POST', '/convert');
//     // 
//     // // when request is done 
//     // request.onload = () => {
//     //   const data = JSON.parse(request.responseText); 
//     //   // update the result div
//     //   if (data.success) {
//     //     const contents = `1 USD is equal to ${data.rate} ${currency}`; 
//     //     document.querySelector('#result').innerHTML = contents; 
//     //   } else {
//     //     document.querySelector('#result').innerHTML = 'There was a error.';
//     //   }
//     // } 
//     // 
//     // const data = new FormData();
//     // data.append('currency', currency); 
//     // 
//     // // send request
//     // request.send(data);
//     // return false; 
//   }
// });