from flask import Flask

app = Flask(__name__)


@app.route('/')
def hellow_world():
    return 'Hello World'


@app.route('/hello')
def hello():
    return 'Hi!'


app.run()
