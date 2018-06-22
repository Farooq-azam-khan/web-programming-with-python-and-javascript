document.addEventListener("DOMContentLoaded", () =>{
  // const li = document.createElement("li")
  // li.innerHTML = 'text of an li'
  // document.querySelector("#add_Li").append(li);
  //
  let num = 0
  document.querySelector("#form").onsubmit = () => {
    const li = document.createElement('li');
    console.log(`${num}`);
    li.innerHTML = `${num}th item`;
    document.querySelector("#add_Li").append(li)
    num++; 
    return false; 
  }
  // console.log(document.querySelector("#ref").disable ) // = true;
  
  
})