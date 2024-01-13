from flask import Flask, session,render_template, request, redirect, url_for
from random import randint
from sql_queries import get_question, get_quises

def index():
    if request.method == "GET":
        quizz= get_quises()
        return render_template("index.html", quizz=quizz, title='Title')
    else:
        session["quiz_id"] = request.form.get('quiz')
        session["question_id"] = 1
        return redirect(url_for("test"))
    
def test():
    if request.method == "POST":
        session['counter'] += 1
    question = get_question(session["quiz_id"], session["question_id"])
    answers = ['a', 'b', 'c', 'd']
    return render_template("test.html", question=question, answers=answers)

def result():
    return render_template("result.html")

app = Flask(__name__, template_folder='', static_folder='')
app.config["SECRET_KEY"] = "qweqwe123"

app.add_url_rule('/', 'index', index)
app.add_url_rule('/index', 'index', index, methods=["POST", "GET"])

app.add_url_rule('/test', 'test', test, methods=["POST", "GET"])

app.add_url_rule('/result', 'result', result)

app.run(debug=False, port=5007)
