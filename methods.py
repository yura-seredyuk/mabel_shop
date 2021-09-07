from logging import raiseExceptions
import psycopg2
import re
from settings import *
from connection import Connection
import datetime

def checkEmail(email:str):
    try:
        if isinstance(email, str):
            email_pattern = re.compile(r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$')
            matches = email_pattern.search(email)
            if matches:
                return email
            else:
                raise ValueError('Incorrect email for SuperAdmin!')
        else:
            raise TypeError('Incorrect email data type for SuperAdmin!')
    except Exception as e:
        print(e)

def checkPassword(password:str):
    try:
        if isinstance(password, str):
            password_pattern = re.compile(r'^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))$')
            matches = password_pattern.search(password)
            if matches:
                return password
            else:
                raise ValueError('Incorrect password for SuperAdmin!')
        else:
            raise TypeError('Incorrect password data type for SuperAdmin!')
    except Exception as e:
        print(e)

class SuperAdmin(Connection):

    def __init__(self, login:str, password:str):
        self.login = checkEmail(login)
        self.password = checkPassword(password)

    def add_admin(self, admin_data):
        table = 'users'
        result = self._postData(table, admin_data)
        return result

    def delete_admin(self, selector):
        table = 'users'
        selector = f"id = '{selector}'"
        result = self.deleteData(table,selector)
        return result

class Admin(Connection):

    def __init__(self, login:str, password:str):
        self.login = login
        self.password = password

    def login_self(self):
        return self.login_check(self.login,self.password)

    def get_order_info(self, category = '', selector = '', ):
        """
        category must be one of the item from the list:
        ['city_name','date_of_order', 'product_name']

        date format for selector: 2020-6-12
        """
        if self.login_self():
            categoryes = ['o.date_of_order', 'p.code']
            table = ('orders o',)
            fields = ("""o.id, o.date_of_order, concat(u.first_name,' ', u.last_name) as "customer", p.product_name as "product",  p.code as "product_id", o.price, o.count, o.discount """,)
            if category and category in categoryes and selector != '':
                selector = selector if isinstance(selector, bool) == bool else str(selector)
                where = f"""where {category} = '{selector}'"""
            else:
                where = ''
            selector = f""" left JOIN users u on u.id = o.customer_id 
                            left JOIN product p on p.id = o.product_id {where}"""
            result = self.getData(table, fields, selector)
            fieldNames = ["id", "date_of_order", "customer", "product_name", "product_id", "price", "count", "discount"]
            changeRes = []
            for item in result:
                cort = {}
                for index,element in enumerate(item):
                    cort[fieldNames[index]]=element
                changeRes.append(cort)
        else:
            changeRes = "Invalid loging!"
        return changeRes

    def add_pr_category(self, data):
        table = 'product_category'
        result = self._postData(table, data)
        return result

    def edit_pr_category(self, data, selector):
        table = 'product_category'
        result = self.updateData(table, data, selector)
        return result

    def delete_pr_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(table,selector)
        return result


if __name__ == '__main__':

    admin_1_data = [{
        "first_name":"Billssss",
        "last_name":"Bobb",
        "date_of_bitrth":"02.05.1684",
        "phone":"+803254",
        "address":"Streee1",
        "password":"123",
        "email":"opa@mail.dog",
        "role":"admin",
        "discount":"20"
    }]
    # admin_1 = Admin('Bad','BOB')
    # admin_1.add_admin(admin_1_data)

    admin_1 = SuperAdmin('opa@mail.dog', 'Sd111%11')
    # .add_admin(admin_1_data)

    admin_2 = Admin("opa@mail.dog","123")
    # admin_2.login_self()

    # rez = admin_2.get_order_info(category='o.date_of_order', selector="2021-09-02")
    # print(rez)
    data = {
            'category_name': "wardrobe"
        }
    # admin_2.add_pr_category(data)

    # edit = admin_2.edit_pr_category(data, "category_name = 'Water'")
    # print(edit)

    # dele = admin_2.delete_pr_category('wardrobe')
    # print(dele)
    
