import unittest
import json
from run import app
from app.api.V1.views.product_views import product_info

#import os

class ProductstestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

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

    '''Tests for product creation'''
    def test_product_created_successfully(self):
        """Tests that a product is created successfully"""
        res = self.client().post('/api/v1/products', data=json.dumps(self.product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)
        self.assertIn("Product created", str(res.data))
    
    def test_product_cannot_create_with_invalid_details(self):
        """Tests that a product cannot be created with empty fields"""
        res = self.client().post('/api/v1/products', data=json.dumps(self.empty_product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)

    '''Tests for getting created products'''
    def test_successfully_gets_product_created(self):
        """Tests that api gets all created products"""
        res = self.client().get('/api/v1/products', data=json.dumps(self.product), headers = {"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Products", str(res.data))

   

    
  
    