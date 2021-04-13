import sqlite3

connection = sqlite3.connect('sqlite.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO detections (fullname, age, cough, fever, sore_throat, shortness_of_breath, \
    head_ache, corona_result, age_60_and_above, gender, test_indication) \
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    ("Harry Potter", 25, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

connection.commit()
connection.close()
