'''Product model'''
class Product(object):
    """product model to store all products data"""
    def __init__(self):
        """ Initializes empty products list"""
        self.products = {}

    def add_products(self, product_name, category, quantity, price, description):
        """Adds a new product to the products list"""
        self.new_product = {}
        self.new_product['id'] = str(len(self.new_product)+1)
        self.new_product['product_name'] = product_name
        self.new_product['category'] = category
        self.new_product['quantity'] = quantity
        self.new_product['price'] = price
        self.new_product['description'] = description
        self.products[id] = self.new_product
        return self.products[id]