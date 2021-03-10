import sqlite3
from os import path

ROOT = path.dirname(path.realpath(__file__))

products = []


# Достаем данные из бд
def get_all():
    for product in sqlite3.connect(path.join(ROOT, 'product.db')).execute("SELECT * FROM products;"):
        products.append({'src': product[0], 'about': product[1],
                         'size': product[2], 'price': product[3],
                         'link': product[4]})
    return products

print(get_all())
# # Создание таблицы
# conn = sqlite3.connect('product.db')
# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS products(
#    src TEXT,
#    about TEXT,
#    size TEXT,
#    price TEXT,
#    link TEXT);
# """)
#
# # Запись данных существующих данных в дб
# for i in db:
#     to_db = [i['src'], i['about'], i['size'], i['price'], i['link']]
#     cur.execute("INSERT INTO products VALUES(?, ?, ?, ?, ?);", to_db)
#     to_db.clear()
#
# conn.commit()
