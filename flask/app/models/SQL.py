from app import db


class Order(db.Model):
    __tablename__ = 'order'
    primary = db.Column(db.Integer, primary_key=True)  # 主鍵
    order_id = db.Column(db.Integer, unique=True, nullable=False)  # 訂單ID
    customer_name = db.Column(db.String(30), nullable=False)  # 顧客名字
    customer_id = db.Column(db.String(30), nullable=False)  # 顧客ID
    purchase_time = db.Column(db.DateTime)  # 購買時間

    def __init__(self, order_id, customer_name, customer_id, purchase_time):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.purchase_time = purchase_time


class Order_item(db.Model):
    __tablename__ = 'order_item'
    primary = db.Column(db.Integer, primary_key=True)  # 主鍵
    order_id = db.Column(db.Integer, unique=True, nullable=False)  # 訂單ID
    product_name = db.Column(db.String(30), nullable=False)  # 商品名字
    amount = db.Column(db.Integer, nullable=False)  # 數量
    product_id = db.Column(db.String(30), nullable=False)  # 商品ID
    price = db.Column(db.Integer, nullable=False)  # 價錢

    def __init__(self, order_id, product_name, amount, product_id, price):
        self.order_id = order_id
        self.product_name = product_name
        self.amount = amount
        self.product_id = product_id
        self.price = price
