window.$ = window.jQuery = require('jquery')
const fs = require('fs')

var json = require('./t1.json');                // $('#vekjnkejrbn') -- document.getElementById('#kdfjbdkfjb')

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


        var pros_tmp = link_html[3].import.querySelector('template');                   //*
        var pros_clone = document.importNode(pros_tmp.content, true);                   //*
        document.querySelector('#pros-page').appendChild(pros_clone);       //*
    }
/* ------------------------------ end import pages to index.html -------------------*/
getReady()



// for Router :

$('[to]').click(function (e) {
    $('#home-parent').removeClass('uk-active')
    $('#Plagiat_check-parent').removeClass('uk-active')
    $('#Settings_Methods-parent').removeClass('uk-active')
    $('#pros-parent').removeClass('uk-active')

    $('#page-title').empty() 

    e.preventDefault()
    var viewName = $(this).attr('to')

    if(viewName == "home-page") {
        $('#page-title').text("Text pretraitment")
    }else if(viewName == "Plagiat_check-page"){
        $('#page-title').text("Plagiarism check")
    }else if(viewName == "Settings_Methods-page"){
        $('#page-title').text("Settings methods")
    }else if(viewName == "pros-page"){
        $('#page-title').text("process page")
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





