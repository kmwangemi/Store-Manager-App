'''Product model'''

products = []

class Product(object):
    """product model to store all products data"""

    def __init__(self, product_name, category, quantity, price, description):
        self.product_name = product_name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.description = description

    def add_products(self):
        """Adds a new product to the products list"""
        new_product = {}
        new_product['id'] = str(len(products)+1)
        new_product['product_name'] = self.product_name
        new_product['category'] = self.category
        new_product['quantity'] = self.quantity
        new_product['price'] = self.price
        new_product['description'] = self.description
        products.append(new_product)
        return new_product

    def get_all_products(self):
        return products

    def get_one_product(self, id):
        if id in products:
            return products[id]
        return {"message": "Product not found"}
