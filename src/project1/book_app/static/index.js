console.log("loading document..."); 
document.addEventListener("DOMContentLoaded", () => {
  console.log("document loaded.");
  document.querySelector("#search_form").onsubmit = () => {
    const request = new XMLHttpRespose();
    const search = document.querySelector("#search_query").value; 
    console.log('search': search); 
    request.open('POST', '/search')
  
    request.onload = () => { 
      const data = JSON.parse(request.responseText); 
      document.querySelector('#result').innerHTML = data.books;
    }
    const data = new FormData();
    data.append('search_query', search);
    request.send(data); 
    return false; 
  }
}); 