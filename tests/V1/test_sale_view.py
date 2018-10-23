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


    def test_sale_created_successfully(self):
        """Tests that a sale is created successfully"""
        pass
        
    
   
   
