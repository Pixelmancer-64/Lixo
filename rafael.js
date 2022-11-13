let xhr = new XMLHttpRequest();

xhr.open(metodo, url);
xhr.setRequestHeader("Content-Type", "aplication/json");
xhr.send(JSON.stringify(dados));

xhr.onreadystatechange = () => {
  if (xhr.readyState == 4) {
    if (!(xhr.status == 200 || xhr.status == 304))
      console.log("DEU ERRO AQUI!");
    else {
      let resposta = JSON.parse(xhr.responseText);
      console.log(resposta);
    }
  }
};

request(
  `${url}?limit=${document.getElementById("max").value}&offset=${
    document.getElementById("min").value - 1
  }`
)
  .then((data) => {
    const result = data.results.map(async (e) => request(e.url));

    let filter = Filters.verifyType();

    Promise.all(result).then((aux) =>
      aux.map((e) => {
        showPokemon(e, filter, Filters.verifyName);
      })
    );
  })

  .catch((e) => {
    console.log("Error " + e);
  });
