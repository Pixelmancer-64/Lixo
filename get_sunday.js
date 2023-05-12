function getSunday(d) {
    d = new Date(d);
    const day = d.getDay();
     const diff = d.getDate() - day;
    return new Date(d.setDate(diff));
  }
  
const res = getSunday(Date.now())
console.log(res)