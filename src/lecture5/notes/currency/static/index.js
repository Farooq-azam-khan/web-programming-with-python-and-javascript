console.log('hi')
document.addEventListener('DOMContentLoaded', () => {
  document.write("htis is me writing");
//   console.log("content loaded");
//   // when form is submitted
//   document.querySelector('#form').onsubmit = () => {
// 
//     // ceate an object that makes an http ajax request
//     const requet = new XMLHttpRequest(); 
//     // get the value of currency text field
//     const currency = document.querySelector('#currency').value; 
//     // initalize new request
//     request.open('POST', '/convert');
// 
//     // when request is done 
//     request.onload = () => {
//       const data = JSON.parse(request.responseText); 
//       if (data.success) {
//         const contents = `1 USD is equal to ${data.rate} ${currency}`; 
//         document.querySelector('#result').innerHTML = contents; 
//       } else {
//         document.querySelector('#result').innerHTML = 'There was a error.';
//       }
//       return false; 
//     }
//   }
});