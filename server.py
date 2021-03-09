from flask import Flask, render_template, request, redirect
from db_work import get_all

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', db=get_all())


if __name__ == '__main__':
    app.run()
