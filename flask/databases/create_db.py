import sqlite3

connection = sqlite3.connect('sqlite.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO detections (title, fever, bodypain, age, runnynose, diffbreath, infected) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("Harry Potter", 99.32986249, 0, 26, 1, -1, 0)
            )

connection.commit()
connection.close()
