from flask import Flask, request
from flask import render_template

from infer import agingTranslate

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/fastAging', methods=['POST'])
def fast_aging():
    input_base64 = request.get_json()['base64']
    if not input_base64:
        return bytes(b'no base64')
    return bytes(b'data:image/png;base64,') + agingTranslate(input_base64)
