from flask import request, jsonify, Blueprint, json

from app.api.V1.models.product_model import Product
product = Blueprint('product', __name__,url_prefix='/api/v1')

product_info = Product()

#products routes
@product.route('/products',methods=['POST'])
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please insert data'})
    new_product = product_info.add_products(product_name=data['product_name'],
                                            category=data['category'],
                                            quantity=data['quantity'],
                                            price=data['price'],
                                            description=data['description'])
    return jsonify({'message' : 'Product created', 'product' : new_product}), 201

   
@product.route('/products',methods=['GET'])
def get_all_products():
    pass

@product.route('/products/<int:product_id>',methods=['GET']) 
def get_one_product():
    pass