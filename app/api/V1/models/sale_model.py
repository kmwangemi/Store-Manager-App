'''Sale model'''

sales = {}
class Sale(object):
    """sale model to store all sales data"""
    
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
        sales[id] = self.new_sale
        return sales[id]

    def get_all_sales(self):
        if None:
            return {"message" : "No sale found"}
        return sales