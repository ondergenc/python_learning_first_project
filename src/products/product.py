from enum import Enum


class ProductType(Enum):
    BOOK = 1
    ALBUM = 2


class Product:
    products = []

    def __init__(self, title: str, unit_price: int):
        self.title = title
        self.unit_price = unit_price
        self.stock_amount = 0
        self._profit_rate:float = 1.20
        self.products.append(self.title)

    @property
    def selling_price(self):
        return self.unit_price * self.profit_rate

    @property
    def profit_rate(self) -> float:
        return self._profit_rate

    @profit_rate.setter
    def set_profit_rate(self, new_rate: float):
        max_increase_rate: float = 0.15
        increase = new_rate - self.profit_rate
        if increase > max_increase_rate:
            print(ValueError("New profit rate can't be bigger than 15% of the old profit rate"))
            return
        self._profit_rate = new_rate

    def stock_value(self):
        return self.selling_price * self.stock_amount

    def __str__(self):
        return "Title: " + self.title

    def search(self, search_key: str):
        return search_key in self.products
