import sqlite3
from os import path

ROOT = path.dirname(path.realpath(__file__))


# Достаем данные из бд
def get_all():
    products_web = sqlite3.connect(path.join(ROOT, 'product.db'))
    return products_web.execute("SELECT * FROM products;")


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

# Ввод данных в бд
# ___Дописать___
