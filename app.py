from flask import Flask, redirect, url_for, request, render_template
import os
import core

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods =['POST', 'GET'])
def click():
    if request.method == 'POST':
        choice = request.form['choice']
        if (choice.isnumeric() == False):
            return render_template("index.html", properchoice = False)
        if (int(choice) > 3) or (int(choice) < 1 ):
            return render_template("index.html", properchoice = False)
        query = request.form['query']
        choice = int(choice) - 1
        print(choice, query)
        datalist = core.linkof(query, choice)
        print(datalist)
        if(datalist == []):
            return render_template("index.html", dataset = datalist, clicked = True, propersearch = False, kaase = choice)
        return render_template("index.html", dataset = datalist, clicked = True, kase = choice)



