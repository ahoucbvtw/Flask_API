from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models.SQL import Order, Order_item
from app import db, app

api_page = Blueprint('Api', __name__)


@api_page.route('/endpoint1', methods=['GET'])
def getAdsData():
    return "welcome to test"


@api_page.route('/order/add', methods=['POST'])
def addOrderData():
    request_data = request.get_json()  # 接收資料
    date_string = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S:%f')
    date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S:%f')

    new_order = {
        "order_id": int(request_data["order_id"]),
        "customer_name": request_data["customer_name"],
        "customer_id": request_data["customer_id"],
        "purchase_time": date_string,
        "product_name": request_data["product_name"],
        "amount": int(request_data["amount"]),
        "product_id": request_data["product_id"],
        "price": int(request_data["price"])
    }

    # 寫入資料庫
    order_add = Order(new_order["order_id"], new_order["customer_name"],
                      new_order["customer_id"], date)

    orderitem_add = Order_item(new_order["order_id"], new_order["product_name"],
                               new_order["amount"], new_order["product_id"], new_order["price"])

    add_data = [order_add, orderitem_add]
    db.session.add_all(add_data)
    db.session.commit()

    return jsonify(new_order)


@api_page.route('/order/modify', methods=['POST'])
def modifyOrderData():
    request_data = request.get_json()  # 接收資料

    update_data = {
        "order_id": int(request_data["order_id"]),
        "update_data": request_data["update_data"]
    }

    # 按照提供的orderID搜尋訂單
    query = Order_item.query.filter_by(order_id=update_data["order_id"]).first()

    # 依序將要更改的訂單內容作變更
    for i in update_data["update_data"].keys():
        if i == "product_name":
            query.product_name = update_data["update_data"]["product_name"]
        if i == "amount":
            query.amount = update_data["update_data"]["amount"]
        if i == "product_id":
            query.product_id = update_data["update_data"]["product_id"]
        if i == "price":
            query.price = update_data["update_data"]["price"]

        db.session.commit()

    return "更新完畢"


@api_page.route('/createdatabase', methods=['GET'])
def CreateDatabase():

    return "createdatabase"




