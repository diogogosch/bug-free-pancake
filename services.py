from db import UserDB, OrderDB
from models import UserModel, OrderModel
from app import session, load_key
from datetime import datetime
from cryptography.fernet import Fernet


def add_user_to_db(user_class):
    add_user = UserDB(name=user_class.name,
                      cpf=encrypt_item(user_class.cpf),
                      email=encrypt_item(user_class.email),
                      phone_number=encrypt_item(user_class.phone_number))
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
        print_cpf = decrypt_item(user.cpf)
        print_email = decrypt_item(user.email)
        print_phone_number = decrypt_item(user.phone_number)
        ret["users"].append(
            {
                "id": user.id,
                "name": user.name,
                "cpf": print_cpf,
                "email": print_email,
                "phone_number": print_phone_number
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


# def get_user_by_cpf(request_cpf):
#     user_list = session.query(UserDB).filter(UserDB.cpf == request_cpf).all()
#     ret = {"users": []}
#     for user in user_list:
#         ret["users"].append(
#             {
#                 "id": user.id,
#                 "name": user.name,
#                 "cpf": user.cpf,
#                 "email": user.email,
#                 "phone_number": user.phone_number
#             }
#         )
#     return ret


def update_user_by_id(request_id, data):
    user_to_update = session.query(UserDB).get(request_id)
    user_name = data['name'] if data.get('name') else user_to_update.name
    user_cpf = data['cpf'] if data.get('cpf') else user_to_update.cpf
    user_email = data['email'] if data.get('email') else user_to_update.email
    user_phone_number = data['phone_number'] if data.get('phone_number') else user_to_update.phone_number
    user_class = UserModel(user_name, user_cpf, user_email, user_phone_number)
    user_to_update.name = user_class.name
    user_to_update.cpf = encrypt_item(user_class.cpf)
    user_to_update.email = encrypt_item(user_class.email)
    user_to_update.phone_number = encrypt_item(user_class.phone_number)
    user_to_update.updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
    session.commit()
    return 'User with ID {} Updated'.format(request_id)


def delete_user_by_id(request_id):
    user_to_delete = session.query(UserDB).get(request_id)
    session.delete(user_to_delete)
    session.commit()
    return 'User with ID {} deleted'.format(request_id)


def add_order_to_db(order_class):
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
    order_to_delete = session.query(OrderDB).get(request_id)
    session.delete(order_to_delete)
    session.commit()
    return 'Order with ID {} deleted'.format(request_id)


def encrypt_item(sens_info):
    key = load_key()
    to_encrypt = sens_info.encode()
    f = Fernet(key)
    encrypted = f.encrypt(to_encrypt)
    return encrypted


def decrypt_item(encrypted_info):
    # Decrypts sensible information
    key = load_key()
    f = Fernet(key)
    to_decrypt = f.decrypt(encrypted_info.encode())
    decrypted = to_decrypt.decode()
    return decrypted

