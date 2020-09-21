class ShoppingCart():
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({'name': name, 'price': price})
            self.total += price
        return self.total
                   
    def mean_item_price(self):
        num_items = len(self.items)
        mean = self.total / num_items
        return mean

    def median_item_price(self):
        len_items = len(self.items)
        half_list = int(len_items / 2)
        even_middle = (half_list + (half_list - 1)) / 2
        if len_items % 2 == 1:
            return self.items[half_list]['price']
        elif len_items % 2 == 0:
            return self.items[even_middle]['price']
        else:
            return "Does not compute. (Waves robot arms)"

    def apply_discount(self):
        discount = self.employee_discount/100
        if self.employee_discount:
            return self.total - (self.total * discount)
        else: 
            return str("Sorry, there is no discount to apply to your cart. :(")

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']