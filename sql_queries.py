import sqlite3

conn = sqlite3.connect("Quiz.sqlite")

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS quiz')
cursor.execute('DROP TABLE IF EXISTS question')
cursor.execute('DROP TABLE IF EXISTS quiz_content')
conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY, name VARCHAR)
''')

conn.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS question (id INTEGER PRIMARY KEY, question VARCHAR, answer VARCHAR, wrong_answer1 VARCHAR, wrong_answer2 VARCHAR, wrong_answer3 VARCHAR)
''')

conn.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz_content (
               id INTEGER PRIMARY KEY, 
               quiz_id INTEGER, 
               question_id INTEGER,
               FOREIGN KEY (quiz_id) REFERENCES quiz (id),
               FOREIGN KEY (question_id) REFERENCES question (id)
               )
''')

conn.commit()

questions = [
    ("Який переклад слова blue правельний?", 'синій', 'блуе', 'щось на англійській', 'незадоволення'),
    ("Який переклад слова magazine правельний?", 'журнал', 'магазин', 'ринок', 'мапа')
]

cursor.executemany('''INSERT INTO question (question, answer, wrong_answer1, wrong_answer2, wrong_answer3) VALUES (?, ?, ?, ?, ?)''', questions)

conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz(
               id INTEGER PRIMARY KEY,
               id quiz INTEGER,
               name quiz VARCHAR
)
               ''')

quziz = [
    ('English words translate',),
    ('Mystery_Galaxy',)
]

cursor.executemany('''INSERT INTO quiz (name) VALUES (?) ''', quziz)
conn.commit()

cursor.execute('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?) ''', [1, 1])
conn.commit()

cursor.execute('''SELECT * FROM question, quiz_content 
               WHERE question.id == quiz_content.question_id 
               AND quiz_content.quiz_id == ?''', [1])

data = cursor.fetchall()
print(data)