from flask import request, jsonify, Blueprint
from app.api.V1.models.product_model import Product

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
    response = product_info.get_all_products()
    return jsonify({'Products' : response}), 200


@product.route('/products/<product_id>', methods=['GET']) 
def get_one_product(product_id):
    """Gets one product"""
    response = product_info.get_one_product(product_id)
    return jsonify({'Product' : response}), 200