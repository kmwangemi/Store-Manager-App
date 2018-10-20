import unittest
import json
from run import app
from app.api.V1.views import product_info

import os

class ProductstestCase(unittest.TestCase):

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

        self.product = {
                        "product_name" : "product_name",
                        "category" : "category",
                        "quantity" : "quantity",
                        "price" : "price",
                        "description" : "description"
                        }

        self.empty_product = {
                                "product_name" : "",
                                "category" : "",
                                "quantity" : "",
                                "price" : "",
                                "description" : ""
                            }

       
        self.register = self.client().post('/api/v1/register', data=json.dumps(self.user),
                        content_type='application/json')

        self.login = self.client().post('/api/v1/login', data=json.dumps(self.logins),
                        content_type='application/json')

     
    def tearDown(self):
        """ clear data after every test"""
        product_info.products.clear()

    

    def test_product_created_successfully(self):
        """Tests that a product is created successfully"""
        initial_count = len(product_info.products)
        res = self.client().post('/api/v1/request', data=json.dumps(self.product), content_type='application/json')
        final_count = len(product_info.products)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(final_count - initial_count, 1)
        self.assertIn("Product created", str(res.data))
    '''
    def test_cannot_create_duplicate(self):
        """Tests that no two requests can exist with similar title"""
        title1 = self.client().post('/api/v1/request',
                    data=json.dumps(self.request),
                    headers={
                        "content-type": "application/json",
                        "access-token": self.token
                    })
        title2 = self.client().post('/api/v1/request', data=json.dumps(self.request),
                                  headers={"content-type": "application/json", "access-token": self.token})
        self.assertEqual(title2.status_code, 401)
        
        self.assertIn("Sorry!! Name taken!",str(title2.data))

    def test_cannot_create_with_name(self):
        """Tests that request title, location and body must be provided to create an new request"""
        res = self.client().post('/api/v1/request', data=json.dumps(self.empty_request),
                                 headers={"content-type": "application/json", "access-token": self.token})
        
        self.assertIn("Name cannot be empty!",str(res.data))

  '''  
    