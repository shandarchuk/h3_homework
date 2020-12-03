import uuid


class Review:
    def __init__(self, customer, item, rating, text):
        self.id = uuid.uuid4()
        self.customer = customer
        self.item = item
        self.text = text
        self.rating = rating
        self.status = "Moderation"

    def __str__(self):
        return f"Review {self.id} - {self.item.title} \nRate: {self.rating} - {self.text}"

    def __repr__(self):
        return f"{self.id}: {self.rating} - {self.text}"

if __name__ == '__main__':
    from customer import Customer
    from item import Item

    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                  "guido@python.org", "09-09-1968")

    i1 = Item("Banana", "Better than ever before", 799.0,
                ("Golden", "Fresh Green"))
    r1 = Review(customer=c1, item=i1, rating=3, text="Item cool, but delivery - suck")
    print(r1)
