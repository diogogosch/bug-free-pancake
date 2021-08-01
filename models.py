from validate_docbr import CPF
from validate_email import validate_email
from datetime import datetime

valid_cpf = CPF()


class UserModel:

    def __init__(self, name_input, cpf_input, email_input, phone_number_input):
        self.name = name_input
        self.cpf = cpf_input
        self.email = email_input
        self.phone_number = phone_number_input

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_updated):
        self._name = name_updated.lower().capitalize()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf_updated):
        if not valid_cpf.validate(cpf_updated):
            raise ValueError("CPF Inválido")
        else:
            self._cpf = cpf_updated

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_updated):
        if not validate_email(email_updated):
            raise ValueError("E-mail Inválido")
        else:
            self._email = email_updated.lower()

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number_updated):
        if len(phone_number_updated) != 10 and len(phone_number_updated) != 11:
            raise ValueError("Telefone Inválido")
        else:
            self._phone_number = phone_number_updated


class OrderModel:

    def __init__(self, item_description, item_quantity, item_price):
        self.__item_description = item_description
        self.__item_quantity = float(item_quantity)
        self.__item_price = float(item_price)
        self.__total_value = self.__item_quantity * self.__item_price
        self.__created_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def item_description(self):
        return

    @item_description.setter
    def item_description(self, item_description_updated):
        self.__item_description = item_description_updated
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def item_quantity(self):
        return

    @item_quantity.setter
    def item_quantity(self, item_quantity_updated):
        self.__item_quantity = float(item_quantity_updated)
        self.__total_value = self.__item_quantity * self.__item_price
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def item_price(self):
        return self.__item_price

    @item_price.setter
    def item_price(self, item_price_updated):
        self.__item_price = float(item_price_updated)
        self.__total_value = self.__item_quantity * self.__item_price
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at
