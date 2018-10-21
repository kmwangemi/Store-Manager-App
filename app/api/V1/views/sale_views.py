from flask import request, jsonify, make_response
from functools import wraps
from app import app
import os
import datetime
import jwt

from app.api.V1.models.sale_model import Sale

sale_info = Sale()


#sales routes

@app.route('/api/v1/sales', methods=['POST'])
def create_sale():
    return ""
   
@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    return ""

@app.route('/api/v1/sales/<saleId>', methods=['GET'])
def get_one_sale():
    return ""





