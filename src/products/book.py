from products import Product
from products import ProductType


class Book(Product):
    authors = []

    def __init__(self, title: str, unit_price: int, author: str):
        super().__init__(title, unit_price)
        self.author = author
        self.product_type = ProductType.BOOK
        self.authors.append(self.author)

    def __str__(self):
        return "Author: {}, Title: {}, Amount: {}".format(self.author, self.title, self.stock_amount)

    def search(self, search_key: str):
        return self.title.__contains__(search_key) or self.author.__contains__(search_key)
