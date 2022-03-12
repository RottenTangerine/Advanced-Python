from flask import Flask
from flask import render_template
from datetime import timedelta

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def hello():
    return 'Hi!'


app.run(debug=True)
