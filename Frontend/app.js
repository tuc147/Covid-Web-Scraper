


const country = document.getElementById('country')
const cases = document.getElementById('cases')
const deaths = document.getElementById('deaths')
const table = document.getElementById('table') 
 

$.get('covidValues2.json')
    .done(data => {
        console.log(data[0].Country);
        console.log(document.getElementById('table').rows[0].cells[0].innerHTML)
        for (let x = 1; x <= 10; x++) {
            // var cell = document.getElementById('table-row-'+x);
            table.rows[0].cell[0]=data[x-1].Country
            table.rows[0].cell[1]=data[x-1].Cases
            table.rows[0].cell[2]=data[x-1].Deaths
            
        }

    });
$.ajax({
    url: 'covidValues2.json',
    dataType: 'json',
    type:'GET',
    cache:false,
    success: function(data){
        $(data.covidValues2).each(function(index,value){
            console.log("Yahtzee");
        });
    }

});