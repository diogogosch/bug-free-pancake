from validate_docbr import CPF
from validate_email import validate_email


class User:

    def __init__(self, name_input, cpf_input, email_input, phone_number_input):
        self.__name = None
        self.__cpf = None
        self.__email = None
        self.__phone_number = None
        self.name(name_input)
        self.cpf(cpf_input)
        self.email(email_input)
        self.phone_number(phone_number_input)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_updated):
        self.__name = name_updated.lower().capitalize()

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf_updated):
        if not CPF(cpf_updated):
            raise ValueError("CPF Inválido")
        else:
            self.__cpf = cpf_updated

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email_updated):
        if not validate_email(email_updated):
            raise ValueError("E-mail Inválido")
        else:
            self.__email = email_updated.lower()

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number_updated):
        if len(phone_number_updated) != 10 and len(phone_number_updated) != 11:
            raise ValueError("Telefone Inválido")
        else:
            self.__phone_number = phone_number_updated
