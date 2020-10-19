'use strict'

{
  const button = document.querySelector('#humberger');

  document.querySelector("body > div > div.balloon").style.visibility = "visible";
  document.querySelector("#user").style.visibility = "hidden";

  button.onclick = function() {

    const hi = document.querySelector("body > div > div.balloon")
    const user = document.querySelector("#user")

    if(hi.style.visibility == "visible"){
      hi.style.visibility = "hidden";
      user.style.visibility = "visible";
    }else{
      hi.style.visibility = "visible";
      user.style.visibility = "hidden";
    };

  };
}
