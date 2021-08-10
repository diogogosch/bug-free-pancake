from model.db_models import OrderDB
from model.order_model import OrderModel
from app import session
from datetime import datetime


def add_order_to_db(order_class):
    # Adds a new order to the DB
    add_order = OrderDB(user_id=order_class.user_id,
                        item_description=order_class.item_description,
                        item_quantity=order_class.item_quantity,
                        item_price=order_class.item_price,
                        total_value=order_class.total_value)
    session.add(add_order)
    try:
        session.commit()
        return 'SUCCESS'
    except:
        session.rollback()
        return 'FAILED'


def get_all_orders():
    # Returns a list of all orders
    order_list = session.query(OrderDB).all()
    ret = {"orders": []}
    for order in order_list:
        ret["orders"].append(
            {
                "id": order.id,
                "user_id": order.user_id,
                "item_description": order.item_description,
                "item_quantity": order.item_quantity,
                "item_price": order.item_price,
                "total_value": order.total_value,
            }
        )
    return ret


def get_order_by_id(request_id):
    # Gets order from DB with a request ID
    order_list = session.query(OrderDB).filter(OrderDB.id == request_id)
    ret = {"orders": []}
    for order in order_list:
        ret["orders"].append(
            {
                "id": order.id,
                "user_id": order.user_id,
                "item_description": order.item_description,
                "item_quantity": order.item_quantity,
                "item_price": order.item_price,
                "total_value": order.total_value,
            }
        )
    return ret


def get_orders_by_user_id(request_user_id):
    # Returns a list of orders from the requested user ID
    order_list = session.query(OrderDB).filter(OrderDB.user_id == request_user_id)
    ret = {"orders": []}
    for order in order_list:
        ret["orders"].append(
            {
                "id": order.id,
                "user_id": order.user_id,
                "item_description": order.item_description,
                "item_quantity": order.item_quantity,
                "item_price": order.item_price,
                "total_value": order.total_value,
            }
        )
    return ret


def update_order_by_id(request_id, data):
    # Updates order by order ID
    order_to_update = session.query(OrderDB).get(request_id)
    order_user_id = data['user_id'] if data.get('user_id') else order_to_update.user_id
    order_item_description = data['item_description'] if data.get(
        'item_description') else order_to_update.item_description
    order_item_quantity = data['item_quantity'] if data.get('item_quantity') else order_to_update.item_quantity
    order_item_price = data['item_price'] if data.get('item_price') else order_to_update.item_price
    order_class = OrderModel(order_user_id, order_item_description, order_item_quantity, order_item_price)
    order_to_update.user_id = order_class.user_id
    order_to_update.item_description = order_class.item_description
    order_to_update.item_quantity = order_class.item_quantity
    order_to_update.item_price = order_class.item_price
    order_to_update.total_value = order_class.total_value
    order_to_update.updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
    session.commit()
    return 'Order with ID {} Updated'.format(request_id)


def delete_order_by_id(request_id):
    # Deletes order by the order ID
    order_to_delete = session.query(OrderDB).get(request_id)
    session.delete(order_to_delete)
    session.commit()
    return 'Order with ID {} deleted'.format(request_id)


