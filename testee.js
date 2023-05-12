let input = document.querySelector("#password_input")  

input.addEventListener("keyup", (e) => {
     if (e.key === 'Enter' || e.keyCode === 13) {
        document.querySelector('#submit').click()
   }
  });