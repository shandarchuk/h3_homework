import uuid


class Supply:
    def __init__(self, item, supplier, amount):
        self.id = uuid.uuid4()
        self.item = item
        self.suplier = supplier
        self.amount = amount

