import itertools
from validate_docbr import CPF
from validate_email import validate_email


def valida_cpf(cpf):
    validate_cpf = CPF()
    return validate_cpf.validate(cpf)


class User:
    user_id = itertools.count()

    def __init__(self, name, cpf, email, phone_number, created_at, updated_at):
        self.__id = next(User.user_id)
        self.__name = name.lower.capitalize
        if not valida_cpf(cpf):
            raise ValueError("CPF Inválido")
        else:
            self.__cpf = cpf
        if not validate_email(email):
            raise ValueError("E-mail Inválido")
        else:
            self.__email = email
        if phone_number.len != 10 or phone_number != 11:
            raise ValueError("Telefone Inválido")
        else:
            self.__phone_number = phone_number
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def id(self):
        return self.__id
