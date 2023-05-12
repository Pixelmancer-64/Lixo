function dates(current) {
    new Date()
    let week= []; 
    current.setDate((current.getDate() - current.getDay()));
    for (var i = 0; i < 7; i++) {
        week.push(
            new Date(current)
        ); 
        current.setDate(current.getDate() +1);
    }
    return week; 
}

console.log(dates(new Date()))