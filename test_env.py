import os
from flask import Flask
import boto3

key = os.getenv("KEY_FOR_PY")
val = os.getenv("VALUE_FOR_PY")
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_ACCESS_KEY")

s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,)
obj = s3.Object('shaygefbucket','data.json')

app = Flask(__name__)

@app.route('/test')
def test():
    return f"test:{key}\nand:{val}"

@app.route('/get')
def get():
    Get_data = obj.get()['Body'].read().decode("utf-8")
    return Get_data

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=2999)