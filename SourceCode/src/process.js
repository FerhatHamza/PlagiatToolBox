const Handlebars = require("handlebars");

// ---------------------------- OTHER FUNCTIONS 


function showResult(jsonString){
    console.log(" ---- this is showResult function "+jsonString)
    var template = $('#tempalte').html() 
    var compile_template = Handlebars.compile(template); 
    var ourData = compile_template(jsonString)

    var resultUL = $('#result-Ul-1')
    resultUL.html(ourData)
}


function showResult_sentance(jsonString){
    console.log(" ---- this is showResult function "+jsonString)
    var template = $('#tempalte_page2').html() 
    var compile_template = Handlebars.compile(template); 
    var ourData = compile_template(jsonString)

    var resultUL = $('#result-p-1')
    resultUL.html(ourData)
}
// ------------------------------------- HOME PAGE

$('#btn-1').click( () => {
    $('#result-Ul-1').empty()
    $('#loading').empty()
    $('#loading').append('<span uk-spinner="ratio: 4.5"></span>')
    UIkit.notification({message: 'تتم المعالجة ...', status: 'warning'})
    
    var txt = $('#textarea-1'). val()
    console.log('txt : '+ txt)

    fetch('http://127.0.0.1:5000/queryText?method=1&text='+ txt)
        .then(response => response.json())
        .then(response => {
            $('#loading').empty()
            UIkit.notification.closeAll()
            UIkit.notification({message: 'انتهت المعالجة...', status: 'success'})
            console.log(response)
            showResult(response)
    });
})



/* ----------------------------------- plagit check */

// textarea
$('#Plagiat_check_process').click(() =>{
    var text_page2 = $('#Plagiat_check_textarea'). val()
    console.log(text_page2)
    $('#loading').empty()
    $('#loading').append('<span uk-spinner="ratio: 4.5"></span>')
    UIkit.notification({message: 'تتم المعالجة ...', status: 'warning'})
    
    fetch('http://127.0.0.1:5000/querySentance?method=1&text='+ text_page2) 
        .then(response => response.json())
        .then(response => {
            $('#loading').empty()
            UIkit.notification.closeAll()
            UIkit.notification({message: 'انتهت المعالجة...', status: 'success'})
            console.log("reponse:" + response)
            showResult_sentance(response)
        });
})


/* --------------------------------------- process*/

$('#btn--process-1').click(()=>{
    console.log('process page ')
    var txt = $('#textarea--process-1'). val()
    console.log('txt : '+ txt)

    fetch('http://127.0.0.1:5000/process?method=1&text='+ txt)
        .then(response => response.json())
        .then(response => {
            $('#loading').empty()
            UIkit.notification.closeAll()
            UIkit.notification({message: 'انتهت المعالجة...', status: 'success'})
            console.log(response)
            
    });
})