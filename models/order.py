from utils.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(50), unique=True, nullable=False)

    # order_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, order_number):
        self.order_number = order_number
        # self.order_date = order_date
