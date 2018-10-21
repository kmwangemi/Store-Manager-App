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

    def test_can_get_all_products(self):
        """test can get all products"""
        self.client().post('/api/v1/products', data=json.dumps(self.product),
                           content_type= 'application/json')
        res = self.client().get('/api/v1/products', content_type= 'application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(product_info.products), 1)
    
    def test_can_get_single_product(self):
        '''Tests that one can get a single product'''
        res = self.client().get('/api/v1/products/productId', content_type='application/json')
        self.assertEqual(res.status_code, 200)    