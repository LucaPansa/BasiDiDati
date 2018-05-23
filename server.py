from flask import Flask, render_template
from time import time
from random import randint

app = Flask(__name__) #creo un'applicazione flask, __name__ richiama il nome del file in modo da avere app e file con lo stesso nome


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
def supermarket:
    price = {'strawberry',}


app.run(debug=True) #Con debug mode off viene visualizzata la generica eccezione "Internal server error"