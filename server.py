from flask import Flask, render_template
from db_work import get_all


app = Flask(__name__)

products = []


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    for product in get_all():
        products.append({
            'src': product[0],
            'about': product[1],
            'size': product[2],
            'price': product[3],
            'link': product[4]
        })
    return render_template('index.html', db=products)


@app.route('/test', methods=['GET', 'POST'])
def index_test():
    for product in get_all():
        products.append({
            'src': product[0],
            'about': product[1],
            'size': product[2],
            'price': product[3],
            'link': product[4]
        })
    return render_template('index.html', db=products)


if __name__ == '__main__':
    app.run()
