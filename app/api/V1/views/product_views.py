from flask import request, jsonify, Blueprint, json
from app.api.V1.models.product_model import Product, products

product = Blueprint('product', __name__, url_prefix='/api/v1')

product_info = Product('product_name', 'category', 'quantity', 'price', 'description')

#products routes
@product.route('/products',methods=['POST'])
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please insert data'})
    new_product = product_info.add_products()
    return jsonify({'message' : 'Product created', 'product' : new_product}), 201

   
@product.route('/products',methods=['GET'])
def get_all_products():
    """Gets all products"""
    response = jsonify(product_info.get_all_products())
    response.status_code = 200
    return response


@product.route('/products/<int:product_id>',methods=['GET']) 
def get_one_product():
    pass