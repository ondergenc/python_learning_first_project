from enum import Enum
from products.product import Product
from collections import OrderedDict
from datetime import datetime


class ProcessType(Enum):
    BUY = 1
    SELL = 2


class Store:
    stock = []
    transactions = OrderedDict()
    transaction_index: int = 0
    starting_balance: float = 0
    balance: float = 0

    def __init__(self, balance: float):
        self.balance = balance
        self.starting_balance = balance

    def __add__(self, product: Product):
        if product not in self.stock:
            self.stock.append(product)

    def __sub__(self, product: Product):
        self.stock.remove(product)

    def __contains__(self, product: Product):
        try:
            product_index = self.stock.index(product)
        except:
            return False
        finding_product = self.stock[product_index]
        return product_index > -1 and finding_product.stock_amount > 0

    def buy(self, product: Product, amount: int):
        try:
            product_index = self.stock.index(product)
        except:
            self.__add__(product)

        if amount < 0:
            print(ValueError("You don't buy negative amount!"))
            return

        product_index = self.stock.index(product)
        finding_product = self.stock[product_index]
        total_amount = finding_product.unit_price * amount
        if self.balance < total_amount:
            print(ValueError("ValueError: Not enough balance for this purchase!"))
            return

        finding_product.stock_amount += amount
        self.balance -= total_amount
        transaction_info = dict(type=ProcessType.BUY,
                                product=finding_product.title,
                                product_type=finding_product.product_type,
                                amount=amount,
                                new_balance=self.balance,
                                time=self.get_current_time()
                                )
        self.log_transaction(transaction_info)

    def sell(self, sell_product: Product, amount: int):
        try:
            product_index = self.stock.index(sell_product)
        except:
            print(ValueError("You don't have this product. You can not sell!"))
            return
        if amount < 0:
            print(ValueError("You don't sell negative amount!"))
            return

        product_index = self.stock.index(sell_product)
        finding_product = self.stock[product_index]

        if finding_product.stock_amount < amount:
            print(ValueError("ValueError: Does not have enough stock for '" + finding_product.title + "'"))
            return

        finding_product.stock_amount -= amount
        total_amount = finding_product.selling_price * amount
        self.balance += total_amount
        transaction_info = dict(type=ProcessType.SELL,
                                product=finding_product.title,
                                product_type=finding_product.product_type,
                                amount=amount,
                                new_balance=self.balance,
                                time=self.get_current_time()
                                )
        self.log_transaction(transaction_info)

        if finding_product.stock_amount == 0:
            self.__sub__(finding_product)

    def log_transaction(self, transaction_info: {}):
        self.transaction_index += 1
        self.transactions[self.transaction_index] = transaction_info

    def search(self, search_key: str):
        found_products = [product for product in self.stock if product.search(search_key)]
        if len(found_products) > 0:
            print("Products found:")
            for product in found_products:
                print(product)
            return found_products
        else:
            print("Product not found!")

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    def compute_profit(self):
        last_transaction = self.transactions[self.transaction_index]
        return last_transaction["new_balance"] - self.starting_balance

    @property
    def total_worth_of_products(self):
        total_worth = sum(product.stock_value() for product in self.stock)
        return total_worth
