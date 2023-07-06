const hour_up = document.querySelector('#hour-up')

const hour_down = document.querySelector('#hour-down')

const minute_up = document.querySelector('#minute-up')

const minute_down = document.querySelector('#minute-down')

const time_up = document.querySelector('#time-up')

const time_down = document.querySelector('#time-down')

const input_hour = document.querySelector('#hour-input')

const input_minute = document.querySelector('#minute-input')

const time_span = document.querySelector('#time-span')

/* EVENTS */

document.addEventListener('click', update_hour);

function update_hour(event){
  event.target.value = event.target.value++ % 12; 
}
