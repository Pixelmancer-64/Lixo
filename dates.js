function get_days_difference() {
    const d = properties.things2;
    const  day = d.getDay()
    const diff = d.getDate() - day + (day == 0 ? -6:1);
    const date = new Date(d.setDate(diff));
  
  
    return properties.thing2 - date
  }
  
  get_days_difference();
  