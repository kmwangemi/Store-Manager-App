'''Sale model'''

sales = []

class Sale(object):
    """sale model to store all sales data"""

    def __init__(self, product_name, description, quantity, stock_quantity, price, total):
        self.product_name = product_name
        self.description = description
        self.quantity = quantity
        self.stock_quantity = stock_quantity
        self.price = price
        self.total = total
        
    def add_sales(self):
        """Adds a new sale to the sales list"""
        new_sale = {}
        new_sale['id'] = str(len(new_sale)+1)
        new_sale['product_name'] = self.product_name
        new_sale['description'] = self.description
        new_sale['quantity'] = self.quantity
        new_sale['stock_quantity'] = self.stock_quantity
        new_sale['price'] = self.price
        new_sale['total'] = self.total
        sales.append(new_sale)
        return new_sale
        
    def get_all_sales(self):
        return sales

    def get_one_sale(self, id):
        if id in sales:
            return sales[id]
        return {"message": "Sale not found"}
    