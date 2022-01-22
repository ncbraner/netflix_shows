from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

import unittest
import random

import services.user_service as us


class UserTest(unittest.TestCase):

    def setUp(self):
        self.username = 'name' + str(random.randrange(1, 500, 3))
        self.password = 'secret'

    def test_register(self):
        # set our input
        form_data = OAuth2PasswordRequestForm(username=self.username, password=self.password, scope='')
        # Test we can create a user
        self.assertEqual(us.register_user(form_data), {'success': 'new user created'})

        # test that trying to create the same username again throws http exception
        with self.assertRaises(HTTPException):
            us.register_user(form_data)


if __name__ == '__main__':
    unittest.main()
