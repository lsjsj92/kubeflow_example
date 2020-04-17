import sys
import argparse
import boto3
import pandas as pd
from io import StringIO

def get_data(BUCKET_NAME, ACCESSKEY, SECRETKEY, REGION_NAME, data_key):
    s3 = boto3.client('s3'
                    ,aws_access_key_id = ACCESSKEY
                    ,aws_secret_access_key = SECRETKEY
                    ,region_name = REGION_NAME)
    s3_object = s3.get_object(Bucket=BUCKET_NAME, Key = data_key)
    return pd.read_csv(s3_object['Body'])
    

def upload_data(BUCKET_NAME, ACCESSKEY, SECRETKEY, REGION_NAME, save_key, preprocessing_data):
    s3 = boto3.client('s3',
                       aws_access_key_id = ACCESSKEY,
                       aws_secret_access_key = SECRETKEY,
                       region_name = REGION_NAME)

    string_io = StringIO()
    preprocessing_data.to_csv(string_io, header=True, index=False)
    s3.put_object(Bucket = BUCKET_NAME, Body = string_io.getvalue(), Key = save_key)


def preprocessing(data):
    print("something preprocessing")
    features = ["Pclass", "Sex"]
    preprocessing_data = pd.get_dummies(data[features]) 
    preprocessing_data["Survived"] = data['Survived']
    return preprocessing_data


if __name__ == "__main__":
    print("start data preprocessing about titanic data")

    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        '--bucket_name', 
        type=str,
        help="Input bucket_name"
    )

    argument_parser.add_argument(
        '--ACCESSKEY', 
        type=str,
        help="Input ACCESSKEY"
    )

    argument_parser.add_argument(
         '--SECRETKEY',
        type=str,
        help="Input SECRETKEY"
    )

    argument_parser.add_argument( 
        '--region_name',
        type=str,
        help="Input region_name" 
    )

    argument_parser.add_argument( 
        '--data_key',
        type=str,
        help="Input data_key" 
    )

    argument_parser.add_argument( 
        '--save_key',
        type=str,
        help="Input save_key"
    )

    args = argument_parser.parse_args()

    data = get_data(args.bucket_name, args.ACCESSKEY, args.SECRETKEY, args.region_name, args.data_key)

