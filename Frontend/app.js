
const url = './Data/covidValues.json'

const country = document.getElementById('country')
const cases = document.getElementById('cases')
const deaths = document.getElementById('deaths')

var table; 
    table = fetch(url).then(response => response.json())
                                    .then(data => table = data)
                                    .then(json =>{
                                        console.log(json)
                                    });

console.log(table)
