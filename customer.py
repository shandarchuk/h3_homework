import uuid

from user import User
from order import Order
from review import Review
from logger import logger

class Customer(User):
    def __init__(self, username, userpass, first_name, last_name, phone,
                email, date_of_birth):
        super().__init__(username, userpass, email)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.bonus_amount = 0
        self.orders = list()
        self.reviews = list()
        self.log = logger

        self.log.info(f"Amazing it's new customer in orm {self}")

    def __str__(self):
        return f"Customer {self.id}: {self.username} ({self.first_name} {self.last_name})"

    def create_order(self, item, amount):
        new_order = Order(self, item, amount)
        self.orders.append(new_order)

        self.log.info(f"Customer {self} created new order {new_order}")

        return new_order


    def create_review(self, item, rating, text):
        new_review = Review(self, item, rating, text)
        self.reviews.append(new_review)

        self.log.info(f"Customer {self} created new review {new_review}")

        return new_review


if __name__ == '__main__':
    from item import Item

    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever before", 799.0,
                ("Golden", "Fresh Green"))
    c1.create_order(i1, 3)

    c1.create_review(i1, 4, "Saw better in the Rozetka")
