from flask import Flask, render_template
from db import db


app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', db=db)


@app.route('/test', methods=['GET', 'POST'])
def index_test():
    return render_template('test.html', db=db)


app.run()
