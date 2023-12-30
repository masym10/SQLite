from flask import Flask, session, request, redirect, url_for
from db_scripts import get_question_after, get_quises
 
def start_quis(quiz_id):
    session['quiz'] = quiz_id
    session['last_question'] = 0
 
def end_quiz():
    session.clear()
 
def quiz_form():
    html_beg = '''<html><body><h2>Виберіть вікторину:</h2><form method="post" action="index"><select name="quiz">'''
    frm_submit = '''<p><input type="submit" value="Вибрати"> </p>'''
 
 
    html_end = '''</select>''' + frm_submit + '''</form></body></html>'''
    options = ''' '''
    q_list = get_quises()
    for id, name in q_list:
        option_line = ('''<option value="''' +
                        str(id) + '''">''' +
                        str(name) + '''</option>
                      ''')
        options = options + option_line
    return html_beg + options + html_end
 
def index():

    if request.method == 'GET':
        start_quis(-1)
        return quiz_form()
    else:
        quest_id = request.form.get('quiz')
        start_quis(quest_id)
        return redirect(url_for('test'))
 
def test():
    '''повертає сторінку питання'''
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    else:
        result = get_question_after(session['last_question'], session['quiz'])
        if result is None or len(result) == 0:
            return redirect(url_for('result'))
        else:
            session['last_question'] = result[0]
            return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'
 
def result():
    end_quiz()
    return "that's all folks!"
 

app = Flask(__name__)  
app.add_url_rule('/', 'index', index)
app.add_url_rule('/index', 'index', index, methods=['post', 'get'])  
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'
 
if __name__ == "__main__":
    app.run()