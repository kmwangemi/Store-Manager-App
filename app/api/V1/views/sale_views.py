from flask import request, jsonify, Blueprint, json

from app.api.V1.models.sale_model import Sale
sale = Blueprint('sale', __name__,url_prefix='/api/v1')
sale_info = Sale()


#sales routes

@sale.route('/products', methods=['POST'])
def create_sale():
    return ""
   
@sale.route('/products', methods=['GET'])
def get_all_sales():
    return ""

@sale.route('/api/v1/sales/<saleId>', methods=['GET'])
def get_one_sale():
    return ""





