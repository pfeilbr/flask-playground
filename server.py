import os
import shutil
from flask import Flask, escape, request, url_for

app = Flask(__name__)

UPLOAD_DIRECTORY_NAME = "uploads"


def prepare_uploads_directory():
    shutil.rmtree(UPLOAD_DIRECTORY_NAME)
    os.mkdir(UPLOAD_DIRECTORY_NAME)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print(request.method)
    prepare_uploads_directory()

    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if file:
            print('file is', filename)
            file.save(os.path.join(UPLOAD_DIRECTORY_NAME, filename))
            # for browser, add 'redirect' function on top of 'url_for'
            return url_for('predict',
                           filename=filename)

    return f'predict called'
