import datetime
import user
import itertools


class Order:
    order_id = itertools.count()

    def __init__(self, user_id, item_description, item_quantity, item_price):
        self.__id = next(Order.order_id)
        self.__user_id = user_id
        self.__item_description = item_description
        self.__item_quantity = float(item_quantity)
        self.__item_price = float(item_price)
        self.__total_value = self.__item_quantity * self.__item_price
        self.__created_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
        self.__updated_at = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

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
