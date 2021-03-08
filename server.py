from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from db_work import get_all

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(5), nullable=False)
    about = db.Column(db.Text, nullable=False)
    size = db.Column(db.String(50), nullable=False)
    src = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    isActive = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return self.title


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
    items = Item.query.all()  # Можно добавить сортировку .order_by(Item.name).
    return render_template('test.html', data=items)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        about = request.form['about']
        size = request.form['size']
        src = request.form['src']
        link = request.form['link']

        item = Item(title=title, price=price, about=about, size=size, src=src, link=link)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/test')

        except Warning:
            return "Something is going wrong"

    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run()
