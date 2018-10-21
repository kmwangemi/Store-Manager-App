from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from app import app
import os
import datetime
import jwt
import re
import uuid

from app.api.V1.models.product_model import Product
from app.api.V1.models.user_model import User

user_info = User()
product_info = Product()


#products routes

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    data = request.get_json()

    if not data or not data['product_name'].strip():
        return jsonify({"message": "Fields cannot be empty!"}), 401
    for pro in product_info.products.values():
        if data['product_name'].strip() == pro['product_name']:
            return jsonify({"message": "Sorry!! Product_name taken!"}), 401

    new_product = product_info.add_products(product_name=data['product_name'],
                                            category=data['category'],
                                            quantity=data['quantity'],
                                            price=data['price'],
                                            description=data['description'])
    return jsonify({'message' : 'Product created', 'product' : new_product})

   
@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    return ""

@app.route('/api/v1/products/<productId>', methods=['GET'])
def get_one_product():
    return ""


