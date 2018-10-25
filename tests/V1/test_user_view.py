import unittest
import json
from run import app
from app.api.V1.views.user_views import user_info


class UserstestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

        self.user = {
                        "fname" : "fname",
                        "lname" : "lname",
                        "username" : "username",
                        "password" : "password",
                        "admin" : "admin"
                        }

        self.empty_user = {
                            "fname" : "",
                            "lname" : "",
                            "username" : "",
                            "password" : "",
                            "admin" : ""
                            }

    '''Tests for user creation'''
    def test_user_created_successfully(self):
        """Tests that a user is created successfully"""
        res = self.client().post('/api/v1/users', data=json.dumps(self.user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)
        self.assertIn("User created", str(res.data))
    
    def test_user_cannot_be_created_with_invalid_details(self):
        """Tests that a user cannot be created with empty fields"""
        res = self.client().post('/api/v1/users', data=json.dumps(self.empty_user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)

    '''Tests for getting successfully created users'''
    def test_gets_successfully_created_users(self):
        """Tests that api gets all created users"""
        res = self.client().get('/api/v1/users', data=json.dumps(self.user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Users", str(res.data))

    '''Tests for getting one user'''
    def test_gets_one_successfully_created_user(self):
        """Tests that api gets one successfully created user"""
        res = self.client().get('/api/v1/users/<userId>', data=json.dumps(self.user), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("User", str(res.data))


   

    
  
    