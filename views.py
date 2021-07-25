from flask import request
from app import app, db
from models import User, UserDB


@app.route("/create_user", methods=['POST', ])
def create_user():
    data_from_request = request.get_json(force=True)
    print(type(data_from_request))
    print(data_from_request['name'])
    user = User(data_from_request['name'],
                data_from_request['cpf'],
                data_from_request['email'],
                data_from_request['phone_number'])
    add_user = UserDB(name=user.name,
                      cpf=user.cpf,
                      email=user.email,
                      phone_number=user.phone_number)
    db.session.add(add_user)
    db.session.commit()
    return 'Usuário adicionado com sucesso'
