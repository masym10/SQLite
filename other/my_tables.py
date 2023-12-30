import sqlite3

conn = sqlite3.connect('School.sqlite')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("DROP TABLE IF EXISTS teacher")
cursor.execute("DROP TABLE IF EXISTS register")
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, name VARCHAR, mark INTEGER)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS teacher(id INTEGER PRIMARY KEY, 
name VARCHAR, subject VARCHAR)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS register(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    mark_id INTEGER, 
    subject_id INTEGER, 
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (mark_id) REFERENCES marks (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id),
    FOREIGN KEY (teacher_id) REFERENCES teacher (id)
    )
    ''')

conn.commit()

students = [("Іван Гаврило", 10), ("Діана Ярамчук", 11), ("Юлія Ткаченко", 7), ("Данило Ковальчук", 4)]

cursor.executemany('''INSERT INTO student (name, mark) VALUES (?, ?)''', students)
conn.commit()

teachers = [("Василь Сикгомлинський", "Математика"), 
("Антон Макаренко", "Фізика"), 
("Леся Українка","Українська література і мова"),
("Іван Франко", "Зарубіжна література"), 
("Михайло Грушевський", "Історія"), 
("Богдан Хмельницький", "Фізкультура"), 
("Тарас Шевченко", "Інформатика"), 
("Іван Мазепа", "Хімія"), 
("Іван Котляревський", "Технології")]
 
cursor.executemany('''
 INSERT INTO teacher(name, subject) VALUES (?, ?)
 ''', students)
 
conn.commit()

cursor.execute('''
 INSERT INTO register(student_id, mark_id, teacher_id, subject_id) VALUES (?, ?, ?, ?)
 ''', [2,2,2,2])
conn.commit()

cursor.execute('''SELECT * FROM student, register 
WHERE student.id == register.student_id AND register.mark_id == ?''', [2])

data = cursor.fetchall()
print(data)