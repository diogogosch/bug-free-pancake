import itertools
from validate_docbr import CPF
from validate_email import validate_email
from datetime import datetime


class User:
    user_id = itertools.count()

    def __init__(self, name, cpf, email, phone_number):
        self.__id = next(User.user_id)
        self.__name = name.lower().capitalize()
        if not CPF(cpf):
            raise ValueError("CPF Inválido")
        else:
            self.__cpf = cpf
        if not validate_email(email):
            raise ValueError("E-mail Inválido")
        else:
            self.__email = email.lower()
        if len(phone_number) != 10 and len(phone_number) != 11:
            raise ValueError("Telefone Inválido")
        else:
            self.__phone_number = phone_number
        self.__created_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_updated):
        self.__name = name_updated
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf_updated):
        if not CPF(cpf_updated):
            raise ValueError("CPF Inválido")
        else:
            self.__cpf = cpf_updated
            self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email_updated):
        self.__email = email_updated
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number_updated):
        self.__phone_number = phone_number_updated
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at
