import unittest
import json
from run import app
from app.api.V1.views.product_views import product_info

import os

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

    def tearDown(self):
        """ clear data after every test"""
        product_info.products.clear()

    
    def test_product_created_successfully(self):
        """Tests that a product is created successfully"""
        initial_count = len(product_info.products)
        res = self.client().post('/api/v1/products', data=json.dumps(self.product), content_type='application/json')
        final_count = len(product_info.products)
        self.assertEqual(final_count - initial_count, 1)
        self.assertIn("Product created", str(res.data))
    
    def test_cannot_create_duplicate(self):
        """Tests that no two products can exist with similar name"""
        name1 = self.client().post('/api/v1/products',
                    data=json.dumps(self.product), content_type='application/json')

        name2 = self.client().post('/api/v1/products', data=json.dumps(self.product), content_type='application/json')
    
        self.assertEqual(name2.status_code, 401)
        
        self.assertIn("Sorry!! Product_name taken!",str(name2.data))

    def test_cannot_create_without_product_details(self):
        '''Tests that all details must be provided to create an new product'''
        res = self.client().post('/api/v1/products', data=json.dumps(self.empty_product), content_type='application/json')
        
        self.assertIn("Fields cannot be empty!",str(res.data))

    
  
    