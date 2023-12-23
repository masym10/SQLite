from flask import Flask, session
from random import randint
from sql_queries import get_question

def start_quiz():
    session["quiz"] = quiz.id
    session{"last_question"}

def index():
    session['counter'] = 0
    session['counter'] = randint(0, 1)
    return '<h1>Hello</h1><br><a href= "/test">Test</a>'

def test():
    data = get_question(session['counter'], session['counter'])
    session['counter'] += 1
    return f"<h1>Test Number {session['counter']}</h1><br><a href= '/'>return</a><br><h3>{str(data)}</h3>"

def result():
    return "<h1>Result</h1>"

app = Flask(__name__)
app.config["SECRET_KEY"] = "qweqwe123"
app.add_url_rule('/', 'home', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
app.run()
