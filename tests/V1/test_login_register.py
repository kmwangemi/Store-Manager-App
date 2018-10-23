import unittest
import json
from run import app
from app.api.V1.views.product_views import product_info

import os

class LoginRegistertestCase(unittest.TestCase):

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


    def test_user_creation(self):
        """Test API can create a user"""
        initial_count = len(user_info.users)
        res = self.client().post('/api/v1/register',
                                data=json.dumps(self.user),
                                content_type= 'application/json')
        final_count = len(user_info.users)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(final_count - initial_count, 1)

    def test_cannot_create_duplicate_user(self):
        """Tests that duplicate usernames cannot be created"""
        user1 = self.client().post('/api/v1/register',
                                data=json.dumps(self.user),
                                content_type='application/json')
        user2 = self.client().post('/api/v1/register', 
                                data=json.dumps(self.user),
                                content_type='application/json')
        self.assertIn('Sorry!! Username taken!', str(user2.data))    

    def test_details_missing(self):
        """test username and password required"""
        res = self.client().post('/api/v1/register', data=json.dumps({
                                        "username": " ",
                                        "password": " ",
                                        "fname": "kelvin",
                                        "lname": "mwangemi"
                                    }), content_type= 'application/json')
        self.assertIn('username or password missing' ,str(res.data))

    def test_bad_request(self):
        """test returns bad request if all fields not available"""
        res = self.client().post('/api/v1/register',
                    data=json.dumps({"username": "kmwangemi", "lname": "mwangemi"}),
                    content_type= 'application/json')
        self.assertEqual(res.status_code,400)
        self.assertIn("check you are sending correct information",str(res.data))
    
    def test_password_validation(self):
        """Test password must be 6-20 characters, alphanumeric"""
        res = self.client().post('/api/v1/register',
                    data=json.dumps({
                        "username": "kmwangemi",
                        "password":"123",
                        "fname": "kelvin",
                        "lname": "mwangemi"
                    }),
                    content_type= 'application/json')
        self.assertEqual(res.status_code, 406)
        self.assertIn("Password must be 6-20 Characters", str(res.data))    