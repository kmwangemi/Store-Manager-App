from flask import request, jsonify, Blueprint
from app.api.V1.models.sale_model import Sale

sale = Blueprint('sale', __name__, url_prefix='/api/v1')
sale_info = Sale('product_name', 'description', 'quantity', 'stock_quantity', 'price', 'total')


#sales routes

@sale.route('/sales', methods=['POST'])
def create_sale():
    """Creates a sale record"""
    data = request.get_json()
    if not data:
        return jsonify({'message' : 'Please enter sale'})
    new_sale = sale_info.add_sales()
    return jsonify({'message' : 'Sale created', 'sale' : new_sale}), 201
   
@sale.route('/products', methods=['GET'])
def get_all_sales():
    pass

@sale.route('/api/v1/sales/<saleId>', methods=['GET'])
def get_one_sale():
    pass





