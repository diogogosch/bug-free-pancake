from db import UserDB
from app import session


def add_to_db(user):
    add_user = UserDB(name=user.name,
                      cpf=user.cpf,
                      email=user.email,
                      phone_number=user.phone_number)
    session.add(add_user)
    try:
        session.commit()
        return 'SUCESSO'
    except:
        session.rollback()
        return 'FALHA'
