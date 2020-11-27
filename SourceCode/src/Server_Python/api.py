import flask 
import os
from flask import request, jsonify, render_template
 
from py7.Pross import break_into_sentences, single_list, text_Process, sentance_Process

from py7.traitement2 import Process 

app = flask.Flask(__name__)

# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1> Hello i'm running process </p>"


@app.route('/hmaza', methods=['GET'])
def hamza():
    return "<h1> hello i'm hamza  </p>"




@app.route('/queryText')
def queryText():
    method = request.args.get('method') 
    text = request.args.get('text') 
    # w = text_Process(text)
    w = Process(text)
    return w.text_Process()
    # return '''<h1>The text value is: {}</h1>'''.format(text)

@app.route('/removetashkeel')
def removetashkeel():
    method = request.args.get('method') 
    text = request.args.get('text')
    w = Process(text)
    return w.removetashkeel()

@app.route('/removeharaka')
def removeharaka():
    method = request.args.get('method') 
    text = request.args.get('text')
    w = Process(text)
    return w.removeHarakat()


@app.route('/removetatweel')
def removetatweel():
    method = request.args.get('method') 
    text = request.args.get('text')
    w = Process(text)
    return w.removeTatweel()

@app.route('/words')
def words():
    method = request.args.get('method') 
    text = request.args.get('text')
    w = Process(text)
    return w.break_into_words()



@app.route('/process')
def process():
    method = request.args.get('method') 
    text = request.args.get('text') 
    # return "hello" + method+ " - " + text
    w = Process(text)
    return w.Lemmatisation()

@app.route('/querySentance')
def querySentance():
    method = request.args.get('method') 
    text = request.args.get('text') 
    # w = sentance_Process(text)
    w = Process(text)
    return w.sentance_Process()

app.run()

