function getMonday(d) {
    d = new Date(d);
    var day = d.getDay(),
        diff = d.getDate() - day + (day == 0 ? -6:1);
    return new Date(d.setDate(diff));
  }
  
const day = getMonday('11/04/2023');
console.log(day)


const input = document.querySelector("#password")

document.querySelector("#show").addEventListener('click', function(){
input.type = "text"
})

document.querySelector("#hide").addEventListener('click', function(){
input.type = "password"
})

