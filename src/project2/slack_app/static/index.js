document.addEventListener("DOMContentLoaded", () => {
  console.log('connected to dom');
  var socket = io.connect(location.protocol+'//'+document.domain+':'+location.port);
  console.lo/g('s:' + socket);
  
  socket.on('connect', () => {
    document.querySelector('#send_message').onclick = () => {
      const name = document.querySelector('#name').value;
      const message = document.querySelector('#message').value;
      const data = {'name':name, 'message':message}
      socket.emit('submit message', data);
      // return false; 
    }
  });
  
  let row_num = 0;
  socket.on('announce message', data => {
    // console.log('data: ' + data);
    
    const table = document.querySelector('#message_board');
    const table_row = table.insertRow(row_num);
    row_num++; 
    const row_name = table_row.insertCell(0); 
    row_name.innerHTML = data.name; 
    const row_message = table_row.insertCell(1);
    row_message.innerHTML = data.message;     
    
  })  
});