from flask import request
from app import app
from models import UserModel
from services import add_to_db, get_all_users, get_user_by_id, \
    get_user_by_name, get_user_by_cpf, update_user_by_id, \
    delete_user_by_id


@app.route('/')
def index():
    return "Hello, World!"


@app.route("/create_user", methods=['POST', ])
def create_user():
    data_from_request = request.get_json(force=True)
    user = UserModel(data_from_request['name'],
                     data_from_request['cpf'],
                     data_from_request['email'],
                     data_from_request['phone_number'])
    status = add_to_db(user)

    return 'Operation finished, {}'.format(status)


@app.route("/all_users")
def view_all_users():
    return get_all_users()


@app.route("/user", methods=['POST', ])
def view_user():
    data_from_request = request.get_json(force=True)
    if 'id' in data_from_request:
        return get_user_by_id(data_from_request['id'])
    if 'cpf' in data_from_request:
        return get_user_by_cpf(data_from_request['cpf'])
    if 'name' in data_from_request:
        return get_user_by_name(data_from_request['name'])


@app.route("/update_user", methods=['POST', ])
def update_user():
    data_from_request = request.get_json(force=True)
    updated_user = UserModel(data_from_request['name'],
                             data_from_request['cpf'],
                             data_from_request['email'],
                             data_from_request['phone_number'])
    update_user_by_id(str(data_from_request['id']), updated_user)
    return 'User Updated'


@app.route("/delete_user", methods=['POST',])
def delete_user():
    data_from_request = request.get_json(force=True)
    delete_user_by_id(data_from_request['id'])
    return 'User deleted'
