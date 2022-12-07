async function read(){
    const response = await fetch('urls.txt')
    console.log(response)
    const data = await response.text()
    const array = data.split('\n')

    array.forEach(element => {
        const a = document.createElement('a')        
        a.innerText = element
        a.href = element
        document.querySelector('body').appendChild(a)
    });
}

read()