import uuid
from user import User

class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

    def check_order(self, order):
        print(f"Checking order {order.id}")
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                return order
        order.status = 'On hold'
        return order

    def approve_review(self, review):
        if review.status == 'Published':
            return review
        if review.rating >= 3:
            review.status = 'Published'
            return review