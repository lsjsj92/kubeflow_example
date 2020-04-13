import sys
import argparse
import boto3
import pandas as pd
from io import StringIO

def get_data(bucket_name, ACCESSKEY, SECRETKEY, region_name, data_key):
    print(bucket_name)
    return "00"



if __name__ == "__main__":
    print("start data preprocessing about titanic data")

    argument_parser = argparse.ArgumentParser()
    args = argument_parser.parse_args()

    data = get_data(args.bucket_name, args.ACCESSKEY, args.SECRETKEY, args.region_name, args.data_key)

