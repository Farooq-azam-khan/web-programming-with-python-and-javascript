document.addEventListener("DOMContentLoaded", () => {
  console.log("connected to webpage");
  // connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
  console.log('s:' + socket);
  
  // when connected, configure bottona
  socket.on('connect', () => {
    console.log("socket connected")
    // each button should emit a 'submit' vote
    document.querySelectorAll('button').forEach(button => {
      button.onclick = () => {
        console.log('button clicked')
        // yes, no, maybe
        const name = document.querySelector('#name').value;
        const message = document.querySelector('#message').value;
        const selection = button.dataset.vote;
        const data = {'name':name, 'message':message, 'selection':selection}
        socket.emit('submit vote', data); 
      }
    });
  });
  
  // when a new vote is announced, add to unordered list
  socket.on('announce vote', data => {
    console.log("annouce vote")
    const li = document.createElement('li');
    li.innerHTML = `${data.name} voted ${data.selection} because ${data.message}`; 
    document.querySelector('#votes').append(li);
  });
});