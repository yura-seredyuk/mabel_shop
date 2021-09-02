import psycopg2
from settings import *

connection = psycopg2.connect(user = USER, password = PASSWORD,
                                host = HOST, port = PORT, 
                                database = 'mebli_db')

cursor = connection.cursor()

# users = """CREATE TABLE users(
#     id SERIAL PRIMARY KEY,
#     first_name varchar(50) NOT NULL,
#     last_name varchar(50) NOT NULL,
#     date_of_bitrth DATE NOT NULL,
#     phone varchar(12) NOT NULL,
#     address varchar(250) NOT NULL,
#     password varchar(32) NOT NULL,
#     email varchar(32) NOT NULL,
#     role varchar(10) NOT NULL
# )"""
# cursor.execute(users)
# connection.commit()

# category = """CREATE TABLE product_category(
#     id SERIAL PRIMARY KEY,
#     category_name varchar(50) NOT NULL
# )"""
# cursor.execute(category)
# connection.commit()

sub_category = """CREATE TABLE product_subcategory(
    id SERIAL PRIMARY KEY,
    subcategory_name varchar(50) NOT NULL,
    category_name INT REFERENCES product_category(id)
)"""
cursor.execute(sub_category)
connection.commit()

product = """CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    code varchar(6) NOT NULL,
    product_name varchar(50) NOT NULL,
    unit_price real NOT NULL,
    count INT NOT NULL,
    description varchar(500) NOT NULL,
    img varchar(200) NOT NULL,
    sub_category_id INT REFERENCES product_subcategory(id)
)"""
cursor.execute(product)
connection.commit()

orders = """CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    date_of_order DATE NOT NULL,
    customer_id  INT REFERENCES users(id),
    product_id  INT REFERENCES product(id),
    price REAL NOT NULL
)"""
cursor.execute(orders)
connection.commit()

cursor.close()
connection.close()