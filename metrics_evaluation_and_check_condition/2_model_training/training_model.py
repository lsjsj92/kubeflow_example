import argparse
import pandas as pd
import json
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
from io import StringIO
from tensorflow.python.lib.io import file_io

def load_data(data):
    d = StringIO(data)
    iris = pd.read_csv(d, sep=',')
    print(iris.shape)
    return iris

def get_train_test_data(iris):

    encode = LabelEncoder()
    iris.Species = encode.fit_transform(iris.Species)

    train , test = train_test_split(iris, test_size=0.2, random_state=0)
    print('shape of training data : ', train.shape)
    print('shape of testing data', test.shape)


    X_train = train.drop(columns=['Species'], axis=1)
    y_train = train['Species']
    X_test = test.drop(columns=['Species'], axis=1)
    y_test = test['Species']

    return X_train, X_test, y_train, y_test

def evaluation(y_test, predict):
    print("accuarcy : ", accuracy_score(y_test, predict))

    accuracy = accuracy_score(y_test, predict)
    #f1 = f1_score(y_test, predict)
    #precision = precision_score(y_test, predict)
    #recall = recall_score(y_test, predict)

    '''
    metrics = {
        'metrics': [{
            'name': 'accuracy-score',
            'numberValue': accuracy,
            'format': "PERCENTAGE",
        }
        , {
            'name': 'f1-score',
            'numberValue': f1,
            'format': "PERCENTAGE",
        }, {
            'name': 'precision-score',
            'numberValue': precision,
            'format': "PERCENTAGE",
        }, {
            'name': 'recall-score',
            'numberValue': recall,
            'format': "PERCENTAGE",
        }]
    }
    '''
    metrics = {
        'metrics': [{
            'name': 'accuracy-score',
            'numberValue': accuracy,
            'format': "PERCENTAGE",
        }]
    }
    with file_io.FileIO('/accuracy.json', 'w') as f:
        json.dump(accuracy, f)
    with file_io.FileIO('/mlpipeline-metrics.json', 'w') as f:
        json.dump(metrics, f)


if __name__ == "__main__":
    
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        '--data',
        type=str, 
        help="Input data csv"
    )

    args = argument_parser.parse_args()
    iris = args.data
    iris = load_data(iris)

    X_train, X_test, y_train, y_test = get_train_test_data(iris)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    predict = model.predict(X_test)
    print('\nevaluation : ')
    evaluation(y_test, predict)
    
    