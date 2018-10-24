from flask import request, jsonify, Blueprint, json

from app.api.V1.models.sale_model import Sale
sale = Blueprint('sale', __name__,url_prefix='/api/v1')
sale_info = Sale()


#sales routes

@sale.route('/sales', methods=['POST'])
def create_sale():
    """Creates a sale record"""
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please insert data and submit'})
    new_sale = sale_info.add_sales(product=data['product'],
                                    description=data['description'],
                                    quantity=data['quantity'],
                                    stock_quantity=data['stock_quantity'],
                                    price=data['price'],
                                    total=data['total'],
                                    attendant=data['attendant'])
    return jsonify({'message' : 'Sale created', 'sale' : new_sale}), 201
   
@sale.route('/products', methods=['GET'])
def get_all_sales():
    pass

@sale.route('/api/v1/sales/<saleId>', methods=['GET'])
def get_one_sale():
    pass





