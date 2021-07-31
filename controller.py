from flask import request
from app import app
from models import User
from services import add_to_db


@app.route("/create_user", methods=['POST', ])
def create_user():
    data_from_request = request.get_json(force=True)
    print(type(data_from_request))
    print(data_from_request['name'])
    user = User(data_from_request['name'],
                data_from_request['cpf'],
                data_from_request['email'],
                data_from_request['phone_number'])
    print(user.name)
    status = add_to_db(user)

    return 'Operação finalizada, {}'.format(status)


@app.route('/')
def index():
    return "Hello, World!"
