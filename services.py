from db import UserDB
from app import session
from sqlalchemy import update


def add_to_db(user_class):
    add_user = UserDB(name=user_class.name,
                      cpf=user_class.cpf,
                      email=user_class.email,
                      phone_number=user_class.phone_number)
    session.add(add_user)
    try:
        session.commit()
        return 'SUCCESS'
    except:
        session.rollback()
        return 'FAILED'


def get_all_users():
    user_list = session.query(UserDB).all()
    ret = {"users": []}
    for user in user_list:
        ret["users"].append(
            {
                "id": user.id,
                "name": user.name,
                "cpf": user.cpf,
                "email": user.email,
                "phone_number": user.phone_number
            }
        )
    return ret


def get_user_by_id(request_id):
    user_list = session.query(UserDB).filter(UserDB.id == request_id)
    ret = {"users": []}
    for user in user_list:
        ret["users"].append(
            {
                "id": user.id,
                "name": user.name,
                "cpf": user.cpf,
                "email": user.email,
                "phone_number": user.phone_number
            }
        )
    print(type(ret))
    return ret


def get_user_by_name(request_name):
    user_list = session.query(UserDB).filter(UserDB.name == request_name)
    ret = {"users": []}
    for user in user_list:
        ret["users"].append(
            {
                "id": user.id,
                "name": user.name,
                "cpf": user.cpf,
                "email": user.email,
                "phone_number": user.phone_number
            }
        )
    return ret


def get_user_by_cpf(request_cpf):
    user_list = session.query(UserDB).filter(UserDB.cpf == request_cpf).all()
    ret = {"users": []}
    for user in user_list:
        ret["users"].append(
            {
                "id": user.id,
                "name": user.name,
                "cpf": user.cpf,
                "email": user.email,
                "phone_number": user.phone_number
            }
        )
    return ret


def update_user_by_id(request_id, user_class):
    user_to_update = session.query(UserDB).get(request_id)
    user_to_update.name = user_class.name
    user_to_update.cpf = user_class.cpf
    user_to_update.email = user_class.email
    user_to_update.phone_number = user_class.phone_number
    session.commit()
    return 'User with ID {} Updated'.format(request_id)


def delete_user_by_id(request_id):
    user_to_delete = session.query(UserDB).get(request_id)
    session.delete(user_to_delete)
    session.commit()
    return 'User with ID {} deleted'.format(request_id)