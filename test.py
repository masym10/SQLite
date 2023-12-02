import sqlite3

conn = sqlite3.connect('Artistc.db')

cursor = conn.cursor()

#m1 = input("What do you choice? a - search for birth year")
    #if m1 == 'a':
        #a = input('Search for birth year (1753-1964)')

       # cursor.execute('SELECT nationality FROM artists WHERE "birth year" == (?)' , [a])
        #data = cursor.fetchall()

        #print(data)
        #print(len(data))

cursor.execute('INSERT INTO artists ("Artist id", Name, Nationality, Gender, "Birth Year")'
               +' VALUES (547, "Aizen", "Japan", "Male", 1009)')

conn.commit()
cursor.execute('SELECT * FROM artists WHERE Name == "Yura"')

data = cursor.fetchall()
print(data)