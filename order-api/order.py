import user

class Order:
    order_id = itertools.count()

    def __init__(self, user_id, item_description, item_quantity, item_price, total_value):
        self.__id = next(Order.order_id)
