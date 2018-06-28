document.addEventListerner('#DOMContentLoaded', () => {
  const request = new XMLHttpRedirect();
  document.querySelector('#form_message').onsubmit = () => {
    // emit message to all users 
    return false; 
  }
});