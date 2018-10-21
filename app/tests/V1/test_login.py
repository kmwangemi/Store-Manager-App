import unittest
import json
from run import app
from app.api.V1.views.product_views import product_info

import os

class LogintestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

        self.user = {
                    "username" : "kmwangemi", 
                    "password" : "123",
                    "fname" : "kelvin", 
                    "lname": "mwangemi"
                    }

        self.logins = {
                        "username" : "kmwangemi", 
                        "password" : "123"
                    }

        self.register = self.client().post('/api/v1/register', data=json.dumps(self.user),
                        content_type='application/json')

        self.login = self.client().post('/api/v1/login', data=json.dumps(self.logins),
                        content_type='application/json')

    def tearDown(self):
        """ clear data after every test"""
        user_info.users.clear()

    def test_user_can_login(self):
        """Test user can login to get access token"""
        login = self.client().post('/api/v1/login', data=json.dumps(self.logins),
                                   content_type= 'application/json')
        self.assertEqual(login.status_code, 200)
        self.assertIn("auth_token",str(login.data))

    def test_cannot_login_if_not_registered(self):
        """ Test that only registered users can login"""
        user_info.users.clear()  # clears users
        login = self.client().post('/api/v1/login', data=json.dumps(self.logins),
                                   content_type= 'application/json')
        self.assertEqual(login.status_code, 401)
        self.assertIn("Username not found!",str(login.data))

    def test_login_details_required(self):
        """Test that all login fields are required"""
        login = self.client().post('/api/v1/login', 
                        data=json.dumps({"username": "", "password": "23786"}),
                        content_type= 'application/json')
        self.assertEqual(login.status_code, 401)
        self.assertIn("login required!",str(login.data))

    def test_bad_request_with_empty_fields(self):
        """tests app will only accept required parameters"""
        login = self.client().post('/api/v1/login', data=json.dumps({"password": "23786"}),
                                   content_type= 'application/json')
        self.assertEqual(login.status_code, 400)
        self.assertIn("username empty",str(login.data))    