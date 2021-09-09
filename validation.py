import re
import unittest
# from methods import SuperAdmin, Admin


# RegEX paterns
name_pattern =  r'^([a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+)\-?([a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+)$'
email_pattern =  r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$'
password_pattern =  r'^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))$'
phone_pattern =  r'^\+\d{12}$'
date_pattern =  r'^([0-3]?[0-9])([\.|\-|\/])([0-1]?[0-9])([\.|\-|\/])(\d{4})$'
address_pattern =  r"^[A-Za-z0-9'\.\-\s\,]{10,}$"
role_pattern =  r'^(admin|super|user)$'
number_pattern =  r'^\d+\.?[0-9]*$'

# models
USERS = {"id":[int, number_pattern], "first_name":[str,name_pattern], "last_name":[str,name_pattern],
        "date_of_bitrth":[str,date_pattern],"phone":[str,phone_pattern],"address":[str,address_pattern],
        "password":[str,password_pattern],"email":[str,email_pattern],"role":[str,role_pattern],"discount":[int,number_pattern]}

class Validate(unittest.TestCase):

    def validate(self, request, model, model_name):
        for key in request:
            self.assertIn(key, model, 
                                f'Field "{key}" is not in {model_name} model. Incorrect field name!')
            self.assertIsInstance(request[key], model[key][0], 
                                f'Field "{key}" has invalid data type for {model_name} model, it must been {model[key][0].__name__}. Type error!' )
            value = request[key].strip() if isinstance(request[key], str) else str(request[key])
            self.assertRegex(value, model[key][1], 
                                f'Field "{key}" has incorrect value for {model_name} model. Value error!')

if __name__ == '__main__':

    admin_1_data = [{
        "first_name":"Bob",
        "last_name":"Bobb",
        "date_of_bitrth":"2-5-1684",
        "phone":"+380123456789",
        "address":"Some  15 st. 17 app.",
        "password":"Qwewe123!3",
        "email":"opa@mail.dog",
        "role":"admin",
        "discount":'sfds'
    }]
    # admin_1 = Admin('Bad','BOB')
    # admin_1.add_admin(admin_1_data)
    # rez = re.search(re.compile(name_pattern), "Bob")
    # print(rez)

    # Validate().test_validate(admin_1_data[0], USERS, 'Users')
    # admin_1 = SuperAdmin('opa@mail.dog', 'Sd111%11')
    # admin_1.add_admin(admin_1_data)


    # for key in admin_1_data[0]:
    #     print(key)

    for  value in admin_1_data[0].items():
        print( value)

    