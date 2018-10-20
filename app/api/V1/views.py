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
from app.api.V1.models.sale_model import Sale
from app.api.V1.models.user_model import User

user_info = User()
product_info = Product()
sale_info = Sale()

'''
#products routes

@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
return ''

@app.route('/api/v1/products/<productId>', methods=['GET'])
def get_one_product():
return ''

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product.add_products(id, name=data['name'], password=hashed_password, admin=False)
    return jsonify({'message' : 'New user created', {'user' : 'new_user'})
return ''

@app.route('/api/v1/products/<productId>', methods=['PUT'])
def update_product():
return ''

@app.route('/api/v1/products/<productId>', methods=['DELETE'])
def delete_product():
return ''

'''
'''
@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
  all_users = []
  for user in user_data.users:
      all_users.append(user)
return jsonify({'users' : all_users}), 201

@app.route('/api/v1/users/<userId>', methods=['GET'])
def get_one_user(userId):
    if userId in user_data.users:
        data = user_data.users[userId]
    return jsonify({"message" : "user not found"), 401

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = user_data.add_users(id, name=data['name'], password=hashed_password, admin=False)
    return jsonify({'message' : 'New user created', {'user' : 'new_user'})

@app.route('/api/v1/users/<userId>', methods=['PUT'])
def promote_user(userId):
    if userId in user_data.users:
        userId.admin = True
        return jsonify({"message" : "user has been promoted"), 201
    return jsonify({"message" : "user not found"), 401
  

@app.route('/api/v1/users/<userId>', methods=['DELETE'])
def delete_user(userId):
    if userId in user_data.users:
        del user_data.users[userId]
        return jsonify({"message" : "user has been deleted"), 201
    return jsonify({"message" : "user not found"), 401

'''





