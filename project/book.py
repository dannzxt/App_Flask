from project import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)

    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price
