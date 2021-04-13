import pickle
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('databases/sqlite.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_detection(detection_id):
    conn = get_db_connection()
    detection = conn.execute(
        'SELECT * FROM detections WHERE id = ?', (detection_id,)
        ).fetchone()
    conn.close()
    if detection is None:
        abort(404)
    return detection

def model_predict(model, newdata):
    results = model.predict([newdata])
    if int(results[0]) == 1:
        return 1
    return 0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the_t_team'

@app.route('/')
def index():
    conn = get_db_connection()
    detections = conn.execute('SELECT * FROM detections ORDER BY created DESC').fetchall()
    conn.close()
    return render_template('index.html', detections=detections)

@app.route('/<int:detection_id>')
def detection(detection_id):
    detection = get_detection(detection_id)
    return render_template('detection.html', detection=detection)

@app.route('/detector', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fullname = request.form['fullname']
        age = request.form['age']
        cough = request.form['cough']
        fever = request.form['fever']
        sore_throat = request.form['sore_throat']
        shortness_of_breath = request.form['shortness_of_breath']
        head_ache = request.form['head_ache']
        if (int(age) - 60) >= 0:
            age_60_and_above = 1
        else:
            age_60_and_above = 0
        gender = request.form['gender']
        test_indication = request.form['test_indication']
        
        model = pickle.load(open("../machine_learning/model.pkl", 'rb'))
        newdata = [cough, fever, sore_throat, shortness_of_breath, head_ache, age_60_and_above, gender, test_indication]
        corona_result = model_predict(model, newdata)

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO detections (fullname, age, cough, fever, sore_throat, shortness_of_breath, \
            head_ache, corona_result, age_60_and_above, gender, test_indication) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fullname, age, cough, fever, sore_throat, shortness_of_breath, 
            head_ache, corona_result, age_60_and_above, gender, test_indication)
        )
        
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
