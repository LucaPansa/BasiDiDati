from flask import Flask, render_template, request
from time import time
from random import randint
import sqlite3



app = Flask(__name__) #creo un'applicazione flask, __name__ richiama il nome del file in modo da avere app e file con lo stesso nome

@app.route('/init_db')
def init_db():
    #Creazione DB
    connection = sqlite3.connect('bdweb.db')
    connection.execute('DROP TABLE IF EXISTS notes;')
    connection.execute('CREATE TABLE notes (data VARCHAR);')
    connection.commit()
    connection.close()
    return "DATABASE CREATED"


@app.route('/') #Reindirizzamento alla pagina index tramite questo "decoratore", faccio una sorta di instradamento, di fatto rendo la funzione index un controller
def index(): #Sostanzialmente creo un controller
    return 'hello world!'


@app.route('/bye')
def goodbye():
    return 'Bye!'


@app.route('/error')
def error():
    return '%d' % (1/0)


@app.route('/template')
def template():
    return render_template('template.html')


@app.route('/template_variable')
def template_variable():
    timestamp = time()
    return render_template('template_variable.html', timestamp=timestamp)

@app.route('/template_if')
def template_if():
    voto = randint(0,32)
    return render_template('template_if.html', voto=voto)

@app.route('/template_for')
def template_for():
    todoList = ['prova1', 'prova2', 'prova3']
    return render_template('template_for.html', todoList=todoList, len=len(todoList))

@app.route('/supermarket')
def supermarket():
    price = {'strawberry': 2.0, 'lemon':1.0, 'Ciapo':-43214234224332422.0 } #dizionario, associa chiave a valore mediante i ":"
    return render_template("supermarket.html", prices=price)

@app.route('/hello/<name>')
def hello(name):
    return "hello, %s!" % name

@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    return str(x + y)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    x = int(request.form.get('x', 0) or 0)
    y = int(request.form.get('y', 0) or 0)
    return render_template('calculator.html', x=x, y=y)



@app.route('/notes', methods=['GET', 'POST'])
def notes():
    note = request.form.get('note') #stesso nome dell'input tag
    connection = sqlite3.connect('bdweb.db')
    cursor = connection.cursor()
    if note:
        cursor.execute("INSERT INTO notes VALUES (?)", [note])
        connection.commit()

    cursor.execute('SELECT data FROM notes')
    notelist = cursor.fetchall()

    return render_template('notes.html', notelist=notelist)



app.run(debug=True) #Con debug mode off viene visualizzata la generica eccezione "Internal server error"