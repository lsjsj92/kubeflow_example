import argparse
import boto3
import pandas as pd
from io import StringIO
import joblib
import tempfile
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def get_preprocessing_data(ACCESSKEY, SECRETKEY, REGIONNAME, BUCKETNAME, DATAKEY):
    s3 = boto3.client('s3',
                        aws_access_key_id = ACCESSKEY,
                        aws_secret_access_key=SECRETKEY,
                        region_name = REGIONNAME)
    s3_object = s3.get_object(Bucket=BUCKETNAME, Key = DATAKEY)
    return pd.read_csv(s3_object['Body'])

def training(data):
    train = data.sample(frac=0.8)
    test = data.drop(train.index)

    y_train = train['Survived']
    X_train = train.drop(['Survived'], axis = 1)
    
    y_test = test['Survived']
    X_test = test.drop(["Survived"], axis = 1)

    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)
    print('Score : ', model.score(X_train, y_train))

    return model, X_test, y_test


def evaluation(model, X_test, y_test):
    predict = model.predict(X_test)
    print("confusion matrix ")
    print(confusion_matrix(y_test, predict))
    print("\nclassification report")
    print(classification_report(y_test, predict))


def upload_model_to_s3(BUCKETNAME, ACCESSKEY, SECRETKEY, REGIONNAME, MODELKEY, model):
    s3 = boto3.client('s3',
                    aws_access_key_id=ACCESSKEY,
                    aws_secret_access_key=SECRETKEY,
                    region_name = REGIONNAME)

    with tempfile.TemporaryFile() as fp:
        joblib.dump(model, fp)
        fp.seek(0)
        s3.put_object(Body=fp.read(), Bucket=BUCKETNAME, Key = MODELKEY)

    print("model upload done")


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--bucket_name',
        type=str,
        help='input bucket name'
    )

    argument_parser.add_argument(
        '--ACCESSKEY',
        type=str,
        help='inpurt ACCESSKEY'
    )

    argument_parser.add_argument(
        '--SECRETKEY',
        type=str,
        help='input SECRETKEY'
    )

    argument_parser.add_argument(
        '--region_name',
        type=str,
        help='input region name'
    )

    argument_parser.add_argument(
        '--model_key',
        type=str,
        help="input model path"
    )

    argument_parser.add_argument(
        '--data',
        type=str,
        help = "input data csv"
    )

    args = argument_parser.parse_args()

    print("get clean data")
    clean_data = get_preprocessing_data(args.ACCESSKEY, args.SECRETKEY, args.region_name, args.bucket_name, args.data)

    print("training model")
    model, X_test, y_test = training(clean_data)

    print("evaluation model")
    evaluation(model, X_test, y_test)

    print("upload model")
    upload_model_to_s3(args.bucket_name, args.ACCESSKEY, args.SECRETKEY, args.region_name, args.model_key, model)

    print("done")

