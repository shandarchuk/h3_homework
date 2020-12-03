import uuid
from user import User
from logger import logger

class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()
        self.log = logger

        self.log.info(f"New admin in our system {self}")

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)

        self.log.info(f"Updated supply {self.supply}")

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

        self.log.info(f"Updated orders {self.orders}")

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