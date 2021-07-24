import itertools
from validate_docbr import CPF
from validate_email import validate_email
from datetime import datetime


class UserClass:
    user_id = itertools.count()

    def __init__(self, name, cpf, email, phone_number):
        self.__id = next(UserClass.user_id)
        self.__name = name.lower().capitalize()
        if not CPF(cpf):
            raise ValueError("CPF Inválido")
        else:
            self.__cpf = cpf
        if not validate_email(email):
            raise ValueError("E-mail Inválido")
        else:
            self.__email = email
        if len(phone_number) != 10 and len(phone_number) != 11:
            raise ValueError("Telefone Inválido")
        else:
            self.__phone_number = phone_number
        self.__created_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def id(self):
        return self.__id
