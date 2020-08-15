from flask import Flask, request
from flask import render_template

from infer import agingTranslate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return 'test success'


@app.route('/fast-aging', methods=['POST'])
def fast_aging():
    input_base64 = request.get_json()['base64']
    if not input_base64:
        return bytes(b'no base64')
    return bytes(b'data:image/png;base64,') + agingTranslate(input_base64)


@app.route('/fast-aging-2', methods=['POST'])
def fast_aging_2():
    input_base64 = request.get_json()['base64']
    if not input_base64:
        return bytes(b'no base64')
    input_base64 = agingTranslate(input_base64)
    return bytes(b'data:image/png;base64,') + agingTranslate(input_base64)


def mockUp(input_base64):
    output_base64 = input_base64
    return output_base64
