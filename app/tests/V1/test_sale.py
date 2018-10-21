import unittest
import json
from run import app
from app.api.V1.views.sale_views import sale_info

import os

class SalestestCase(unittest.TestCase):

    def setUp(self):
        """will be called before every test"""
        self.client = app.test_client

        self.sale = {
                        "product_name" : "product_name",
                        "description" : "description",
                        "quantity" : "quantity",
                        "stock_quantity" : "stock_quantity",
                        "price" : "price",
                        "total" : "total",
                        "attendant" : "attendant"
                    }

        self.empty_sale = {
                            "product_name" : "",
                            "description" : "",
                            "quantity" : "",
                            "stock_quantity" : "",
                            "price" : "",
                            "total" : "",
                            "attendant" : ""
                            }

    def tearDown(self):
        """ clear data after every test"""
        sale_info.sales.clear()

    def test_sale_created_successfully(self):
        """Tests that a sale is created successfully"""
        initial_count = len(sale_info.sales)
        res = self.client().post('/api/v1/sales', data=json.dumps(self.sale), content_type='application/json')
        final_count = len(sale_info.sales)
        self.assertEqual(final_count - initial_count, 1)
        self.assertIn("Sale created", str(res.data))
    
    def test_cannot_create_duplicate_sales(self):
        """Tests that no two sales can exist with similar name"""
        name1 = self.client().post('/api/v1/sales',
                    data=json.dumps(self.sale), content_type='application/json')

        name2 = self.client().post('/api/v1/sales', data=json.dumps(self.sale), content_type='application/json')
    
        self.assertEqual(name2.status_code, 401)
        
        self.assertIn("Sorry!! Sale_name exists!",str(name2.data))

    def test_cannot_create_empty_sale(self):
        '''Tests that an empty sale cannot be created'''
        res = self.client().post('/api/v1/sales', data=json.dumps(self.empty_sale), content_type='application/json')
        
        self.assertIn("Sorry empty sale!",str(res.data))

    def test_can_get_all_sales(self):
        """test can get all sales"""
        self.client().post('/api/v1/sales', data=json.dumps(self.sale),
                           content_type= 'application/json')
        res = self.client().get('/api/v1/sales', content_type= 'application/json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(sale_info.sales), 1)
    
    def test_can_get_single_sale(self):
        '''Tests that one can get a single sale'''
        res = self.client().get('/api/v1/sales/saleId', content_type='application/json')
        self.assertEqual(res.status_code, 200)