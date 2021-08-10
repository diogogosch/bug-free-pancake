class OrderModel:

    def __init__(self, user_id, item_description, item_quantity, item_price):
        self.__user_id = user_id
        self.__item_description = item_description
        self.__item_quantity = float(item_quantity)
        self.__item_price = float(item_price)
        self.__total_value = self.__item_quantity * self.__item_price

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id_updated):
        self.__user_id = user_id_updated

    @property
    def item_description(self):
        return self.__item_description

    @item_description.setter
    def item_description(self, item_description_updated):
        assert type(item_description_updated) is str
        self.__item_description = item_description_updated

    @property
    def item_quantity(self):
        return self.__item_quantity

    @item_quantity.setter
    def item_quantity(self, item_quantity_updated):
        assert type(item_quantity_updated) is str
        self.__item_quantity = float(item_quantity_updated)
        self.__total_value = self.__item_quantity * self.__item_price

    @property
    def item_price(self):
        return self.__item_price

    @item_price.setter
    def item_price(self, item_price_updated):
        assert type(item_price_updated) is str
        self.__item_price = float(item_price_updated)
        self.__total_value = self.__item_quantity * self.__item_price

    @property
    def total_value(self):
        return self.__total_value