import unittest
import re
from methods import Admin, SuperAdmin
from connection import Connection

class SuperAdminTests(unittest.TestCase):
    # valid data
    VALID_EMAIL = 'Correct@email.com'
    VALID_PASSWORD = 'AQwe12!_'

    ADMIN_DATA = [{
        "first_name":"Bill",
        "last_name":"Bobb",
        "date_of_bitrth":"02.05.1684",
        "phone":"+803254",
        "address":"Streee1",
        "password":"123",
        "email":"opa@mail.dog",
        "role":"admin",
        "discount":"20"
    }]

    # invalid data
    INVALID_EMAIL = 'inorrect@@email.com'
    INVALID_PASSWORD = 12345678

    def setUp(self):
        # create SuperAdmin
        self.super_admin = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        # return super().setUp()
        pass

    def tearDown(self):
        selector = Connection().getNextId('users')-1
        self.super_admin.delete_admin(selector)
        return super().tearDown()
    
    def clear_record(self, table):
        selector = Connection().getNextId(table)-1
        self.super_admin.delete_admin(selector)

    def test_create_SuperAdmin(self):
        super_admin_val = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.assertIsInstance(super_admin_val, SuperAdmin)
        print('Test 1.1: pass.')

    def test_create_invalid_SuperAdmin(self):
        super_admin_inv = SuperAdmin(self.INVALID_EMAIL, self.INVALID_PASSWORD)
        # self.assertRaises(ValueError, msg='Incorrect email!')
        email_pattern = re.compile(r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$')

        self.assertNotRegex(self.INVALID_EMAIL, email_pattern, 'Incorrect email!')
        self.assertNotIsInstance(self.INVALID_PASSWORD, str, 
                            f'Incorect data type! It must been str but returned {type(self.INVALID_PASSWORD)}')
        self.assertIsInstance(super_admin_inv, SuperAdmin)
        print('Test 1.2: pass.')

    def test_add_admin(self):
        response = self.super_admin.add_admin(self.ADMIN_DATA)
        self.assertEqual(response, 'Insert done!')
        print('Test 1.3: pass.')
        # self.clear_record('users')

class AdminTests(unittest.TestCase):  
    pass      

        
        



    # def test_add_admin(self):
    #     admin_1 = SuperAdmin('Bad','BOB').add_admin(admin_1_data)

if __name__ == '__main__':
    unittest.main()
