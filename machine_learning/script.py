# Library
import pandas as pd
from sklearn import svm
from sklearn.svm import SVC
import pickle

def read_dataset():
    # Dataset From https://www.kaggle.com/zhiruo19/covid19-symptoms-classification
    return pd.read_csv("data.csv") 

def model_train(test, result):
    model = SVC(C=1.0, kernel='linear', gamma='auto')
    model.fit(test, result)
    return model

def saving_model(model, filename):
    pkl_name = filename
    with open(pkl_name, 'wb') as file:
        pickle.dump(model, file)
    return True

def model_predict(model, data):
    results = model.predict([data])
    if(results[0] == 1):
        return True
    return False

if __name__ == "__main__":
    # Read Dataset
    data = read_dataset()

    # Making new Dataframe
    df = pd.DataFrame(columns=['processed_data','diagnosis'])
    for index, row in data.iterrows():
        temp = [row['fever'], row['bodypain'], row['age'], row['runnynose'], row['diffbreath']]
        df = df.append({'processed_data': temp, 'diagnosis': row['infected']}, ignore_index=True)

    # Modeling
    model = model_train(df['processed_data'].values.tolist(), df['diagnosis'].values.tolist())

    # Saving Model to Pickle
    saving_model(model, "model.pkl")

    # Prediction
    data_test = [15.34, 14.26, 102.5, 704.4, 0.1073]    # Result Expected : False
    res = model_predict(model, data_test)
    print(res)