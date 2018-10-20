'''Sale model'''
class Sale(object):
    """sale model to store all sales data"""
    def __init__(self):
        """ Initializes empty sales list"""
        self.sales = []
 
    def add_sales(self, date_created, product, description, quantity, stock_quantity, price, total, attendant):
        """Adds a new sale to the sales list"""
        self.new_sale = {}
        self.new_sale['id'] = str(len(self.new_sale)+1)
        self.new_sale['date_created'] = date_created
        self.new_sale['product'] = product
        self.new_sale['description'] = description
        self.new_sale['quantity'] = quantity
        self.new_sale['stock_quantity'] = stock_quantity
        self.new_sale['price'] = price
        self.new_sale['total'] = total
        self.new_sale['attendant'] = attendant
        self.sales[id] = self.new_sale
        return {"message" : "{} added successfully".format(id)}