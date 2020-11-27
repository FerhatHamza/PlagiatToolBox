window.$ = window.jQuery = require('jquery')
const fs = require('fs')

var json = require('./t1.json'); 

const Handlebars = require("handlebars");

// const PythonShell = require('python-shell')
let {PythonShell} = require('python-shell')

/* ------------------------------ import pages to index.html   -------------------  */
    function getReady(){
        var link_html = $('link[rel="import"]');                                        //*
                                                                                        //*
        var home_tmp = link_html[0].import.querySelector('template');                   //*
        var home_clone = document.importNode(home_tmp.content, true);                   //*
        document.querySelector('#home-page').appendChild(home_clone);                   //*
                                                                                        //*
                                                                                        //*
        var plg_tmp = link_html[1].import.querySelector('template');                    //*
        var plg_clone = document.importNode(plg_tmp.content, true);                     //*
        document.querySelector('#Plagiat_check-page').appendChild(plg_clone);           //*
                                                                                        //*
                                                                                        //*
        var sett_tmp = link_html[2].import.querySelector('template');                   //*
        var sett_clone = document.importNode(sett_tmp.content, true);                   //*
        document.querySelector('#Settings_Methods-page').appendChild(sett_clone);       //*
    }
/* ------------------------------ end import pages to index.html -------------------*/

getReady()

// for Router :

$('[to]').click(function (e) {
    $('#home-parent').removeClass('uk-active')
    $('#Plagiat_check-parent').removeClass('uk-active')
    $('#Settings_Methods-parent').removeClass('uk-active')

    $('#page-title').empty() 

    e.preventDefault()
    var viewName = $(this).attr('to')

    if(viewName == "home-page") {
        $('#page-title').text("Text pretraitment")
    }else if(viewName == "Plagiat_check-page"){
        $('#page-title').text("Plagiarism check")
    }else if(viewName == "Settings_Methods-page"){
        $('#page-title').text("Settings methods")
    }

    showView(viewName)
    $(this).parent().addClass('uk-active')
    console.log('ok')
})


function showView(viewName) {
    console.log(viewName)
    $('.view').hide()
    $('#' + viewName).show()
    console.log('#' + viewName)
}


/* ------------------------- PYTHON FUNCTIONS */


function py7_1(txt){    
   
    let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        args: [txt]
    };
    


    PythonShell.run(__dirname +'/py7/Pross.py', options, function (err , results) { 
        console.log(results)
        showResult(json)
    });
    
 }
       
      


function showResult(jsonString){
    console.log(" ---- this is showResult function "+jsonString)
    var template = $('#tempalte').html() 
    var compile_template = Handlebars.compile(template); 
    var ourData = compile_template(jsonString)

    var resultUL = $('#result-Ul-1')
    resultUL.html(ourData)
}


/* --------------------------------- home  -- home_textarea_1, home_btn_1, home_result_uk_1 */
$('#btn-1').click( () => {
    fs.writeFileSync('./src/t1.json', '[]')
    $('#result-Ul-1').empty()
    $('#loading').empty()
    $('#loading').append('<span uk-spinner="ratio: 4.5"></span>')
    UIkit.notification({message: 'Processing ...', pos: 'bottom-left'})
    var txt = $('#textarea-1'). val()
    console.log('txt : '+ txt)
    py7_1(txt)
})

$('#refresh').click(() => {
    $('#loading').empty()
    var data = fs.readFileSync('./src/t1.json', 'utf8');
    var sjson = JSON.parse(data);
    showResult(sjson)
})




/* ----------------------------------- plagit check */
$('#textInput').show()
$('#fileInput').hide()

$('#file_input').click(() =>{
    $('#textInput').hide()
    $('#fileInput').show()
})

$('#text_input').click(() =>{
    $('#textInput').show()
    $('#fileInput').hide()
})

$('#page2-algorithm').change(()=> {
    var getVal = $('#page2-algorithm'). val();
    console.log(" value is : " +getVal); 
    getVal == 0 ? console.log('alg 1 ') : console.log('alg 2 ')
})

// textarea
$('#Plagiat_check_process').click(() =>{
    var text_page2 = $('#Plagiat_check_textarea'). val()
    console.log(text_page2)
})










/* ----------------------------------- settings methods */

$('#new-method-content').show()
$('#compare-content').hide()

$('#new-method').click(()=> {
    $('#new-method-content').show()
    $('#compare-content').hide()
})

$('#compare').click(()=> {
    $('#new-method-content').hide()
    $('#compare-content').show()
})

$('#myuuuu').hide()
$('#page3-select-1').change(()=> {
    var getVal = $('#page3-select-1'). val();
    console.log(" value is : " +getVal); 
    if(getVal == 4)
    {
        $('#myuuuu').show()
    }else{
        $('#myuuuu').hide()
    }
})


$('#page3-btn').click( () => {
    let myNotification = new Notification('Hamza Ferhat', {
        body: 'this feature is not available now'
      })
      
      myNotification.onclick = () => {
        console.log('Notification clicked')
      }

    $('#page3-result'). empty()
    console.log('ok you chose ')
    var m1 = $('#page3-method1'). val()
    var m2 = $('#page3-method2'). val()
    console.log('ok you chose '+ m1 + ' - ' + m2 )
    
})

















/*
// end router 
$('#fileInput').hide()

homebtn.click(()=> {
    console.log('ok its work this is home page. ')
})

aboutbtn.click(()=> {
    alert('about')
    console.log('ok its work this is about page. ')
})

text_input.click(()=> {
    $('#textInput').show()
    $('#fileInput').hide()

})

file_input.click(()=> {
    $('#textInput').hide()
    $('#fileInput').show()
})

/* -------------------------------------- Functions for all --------------------------
function removeLI(ul){
    var child = ul.lastElementChild;  
    while (child) { 
        e.removeChild(child); 
        child = e.lastElementChild; 
    } 
}

function CallPy7(text){
    console.log('call python ... ')
    var pyPath = __dirname+' /py7/Pross.py'
    let options = {
        mode: 'text',
        pythonPath: __dirname+'/py7',
        pythonOptions: ['-u'], // get print results in real-time
        args: [text]
    };
    
    PythonShell.run('Pross.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
        console.log('end call python')
    });
}

/* ---------------------------------------- home --------------------------------------

home_btn.click(() => { 
    //removeLI(home_ul_result)
    home_ul_result.empty()
    var text = home_textarea_text. val()
    console.log(text.substring(1))
    CallPy7(text)
    var list = text.split(" ")
    list.forEach(element => {
        createElement(element ,'noun')
    });
})

function createElement(word, type){
    home_ul_result.append('<li data-color="'+ type +'"> <span class="words stopWord"> '+ word +'</span></li>')
}


/*----------------------------------------- page2 -------------------------------------
page2_button.click(() =>{
    var text = page2_text. val()
    console.log(text)
    Plagiat_check_putText.append(text);
})


/*  ------------------------------------- page 3 --------------------------------------

$('#new-method-content').show()
$('#compare-content').hide()

new_method.click(()=> {
    $('#new-method-content').show()
    $('#compare-content').hide()
})

compare.click(()=> {
    $('#new-method-content').hide()
    $('#compare-content').show()
})

$('#myuuuu').hide()
select3.change(()=> {
    var getVal = select3. val();
    console.log(" value is : " +getVal); 
    if(getVal == 4)
    {
        $('#myuuuu').show()
    }else{
        $('#myuuuu').hide()
    }
})*/