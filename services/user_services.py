from datetime import datetime

from cryptography.fernet import Fernet

from app import session, load_key
from model.db_models import UserDB
from model.user_model import UserModel


def add_user_to_db(user_class):
    # Adds a new user to the DB, fails if cpf already exists in db
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
    # Returns a list of all users in the db
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
    # Returns the user with the requested id
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
    # returns a user list with the name requested
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
    # returns the user with the requested CPF number
    user_list = session.query(UserDB).filter(decrypt_item(UserDB.cpf) == request_cpf).all()
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


def update_user_by_id(request_id, data):
    # updates the user from request id with the data provided
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
    # Deletes the user with the provided ID
    user_to_delete = session.query(UserDB).get(request_id)
    session.delete(user_to_delete)
    session.commit()
    return 'User with ID {} deleted'.format(request_id)


def encrypt_item(sens_info):
    # Encrypts sensible information
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