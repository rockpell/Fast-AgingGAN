from flask import Flask, request, render_template
from infer import agingTranslate

app = Flask(__name__)


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fast-aging', methods=['POST'])
def fast_aging():
    input_base64 = request.get_json()['base64']
    if not input_base64:
        return bytes(b'no base64')
    return bytes(b'data:image/png;base64,') + agingTranslate(input_base64)


def mockUp(input_base64):
    output_base64 = input_base64
    return output_base64


if __name__ == '__main__':
    from waitress import serve

    serve(app, host='0.0.0.0', port=80)
