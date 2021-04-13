DROP TABLE IF EXISTS detections;

CREATE TABLE detections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fullname TEXT NOT NULL,
    age INTEGER NOT NULL,
    cough INTEGER NOT NULL,
    fever INTEGER NOT NULL,
    sore_throat INTEGER NOT NULL,
    shortness_of_breath INTEGER NOT NULL,
    head_ache INTEGER NOT NULL,
    corona_result INTEGER NOT NULL,
    age_60_and_above INTEGER NOT NULL,
    gender INTEGER NOT NULL,
    test_indication INTEGER NOT NULL
);
