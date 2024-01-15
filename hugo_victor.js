/* console.log(
  "Abacate verde é uma merda vai retornar abacate"
    .split(" ")
    .map((e) => {
      e = e.toLowerCase();

      let counter = {};
      let letter = e[0];

      e.split("").forEach((e) => {
        counter[e] = !counter[e] ? 1 : counter[e] + 1;

        if (counter[letter] < counter[e]) letter = e;
      });

      return [e, letter, counter[letter]];
    })
    .reduce(
      (prev, current) => (current[2] > prev[2] ? current : prev),
      [0, 0, 0]
    )
); */

const string = "hugo é muito fodaaaaaa";
const string_array = string.split(" ")

for(let i =0; i < string_array.length; i++){

  let counter = {}
  let best_letter = string_array[i].charAt(0);
  string_array[i] = string_array[i].toLowerCase();

  for(let j=0; j < string_array[i].length; j++){

    let current_letter = string_array[i].charAt(j);

    counter[current_letter] = !counter[current_letter] ? 1 : counter[current_letter] + 1;

    if (counter[best_letter] < counter[current_letter]) best_letter = current_letter;
  }

  console.log(string_array[i], best_letter, counter[best_letter])
}