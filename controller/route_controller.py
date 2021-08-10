from flask import request, redirect
from app import app
from model.user_model import UserModel
from model.order_model import OrderModel
from services.order_services import add_order_to_db, get_all_orders, \
    get_order_by_id, get_orders_by_user_id, update_order_by_id, \
    delete_order_by_id
from services.user_services import add_user_to_db, get_all_users, get_user_by_id, get_user_by_name, get_user_by_cpf, \
    update_user_by_id, delete_user_by_id


@app.route('/')
def index():
    return "Homepage API Users & Orders - Serasa-db"


@app.route("/user", methods=['POST', ])
def create_user():
    data_from_request = request.get_json(force=True)
    user = UserModel(data_from_request['name'],
                     data_from_request['cpf'],
                     data_from_request['email'],
                     data_from_request['phone_number'])
    add_user_to_db(user)
    return redirect("/")


@app.route("/all_users", methods=['GET', ])
def view_all_users():
    return get_all_users()


@app.route("/user", methods=['GET', ])
def view_user():
    data_from_request = request.get_json(force=True)
    if 'id' in data_from_request:
        return get_user_by_id(data_from_request['id'])
    if 'cpf' in data_from_request:
        return get_user_by_cpf(data_from_request['cpf'])
    if 'name' in data_from_request:
        return get_user_by_name(data_from_request['name'])


@app.route("/user", methods=['PUT', ])
def update_user():
    data_from_request = request.get_json(force=True)
    update_user_by_id(str(data_from_request['id']), data_from_request)
    return get_user_by_id(data_from_request['id'])


@app.route("/user", methods=['DELETE', ])
def delete_user():
    data_from_request = request.get_json(force=True)
    delete_user_by_id(data_from_request['id'])
    return redirect("/")


@app.route("/order", methods=['POST', ])
def create_order():
    data_from_request = request.get_json(force=True)
    new_order = OrderModel(data_from_request['user_id'],
                           data_from_request['item_description'],
                           data_from_request['item_quantity'],
                           data_from_request['item_price'])
    add_order_to_db(new_order)
    return redirect("/")


@app.route("/all_orders", methods=['GET'])
def view_all_orders():
    return get_all_orders()


@app.route("/order", methods=['GET', ])
def get_orders():
    data_from_request = request.get_json(force=True)
    if 'id' in data_from_request:
        return get_order_by_id(data_from_request['id'])
    if 'user_id' in data_from_request:
        return get_orders_by_user_id(data_from_request['user_id'])


@app.route("/order", methods=['PUT', ])
def update_order():
    data_from_request = request.get_json(force=True)
    update_order_by_id(str(data_from_request['id']), data_from_request)
    return get_order_by_id(data_from_request['id'])


@app.route("/order", methods=['DELETE', ])
def delete_order():
    data_from_request = request.get_json(force=True)
    delete_order_by_id(data_from_request['id'])
    return redirect("/")
