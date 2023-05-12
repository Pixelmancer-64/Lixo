const inputRange = document.querySelector(".rangeSlider");
const emoji = document.querySelector(".emoji");

inputRange.addEventListener("input", function (e) {
  document.documentElement.style.setProperty("--range", `${this.value}%`);
  showEmoji(this.value);
  moveEmoji(this.value);
});

// inputRange.addEventListener("mouseup", function () {
//   // hideEmoji();
// });

function showEmoji(range) {
  if (range > 0) {
    return (emoji.style.opacity = 1);
  }
  return (emoji.style.opacity = 0);
}

function moveEmoji(range) {
  const min_size = 20
  const size = ((40 - min_size)/100 * range) + min_size
  emoji.style.setProperty('left', `calc(${range}% - ${size/8}px - ${(size/2 + size/8)/100 * range}px)`);
  emoji.style.marginTop = `-${range / 50}%`;
  emoji.style.width = `${size}px`;
  emoji.style.height = `${size}px`;
}

function hideEmoji() {
  inputRange.disabled = true;
  emoji.classList.add("emoji-hide");
  emoji.style.opacity = 0;
}

function applyClass(name,element,doRemove){
  if(typeof element.valueOf() == "string"){
      element = document.getElementById(element);
  }
  if(!element) return;
  if(doRemove){
      element.className = element.className.replace(new RegExp("\\b" + name + "\\b","g"));
  }else{      
      element.className = element.className + " " + name;
  }
}


const input = document.querySelector('.rangeSlider');

applyClass(`.${input.id}`, input, `-- emoji: url('hugo')`)