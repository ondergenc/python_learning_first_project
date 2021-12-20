from store.store import Store
from products.book import Book
from products.album import Album

store = Store(balance=50000)
print("Store Balance: ", store.balance)

b1 = Book(title="Tutunamayanlar", unit_price=75, author="Oguz Atay")
b2 = Book(title="Metamorphosis", unit_price=70, author="Franz Kafka")
b3 = Book(title="Heart of Darkness", unit_price=100, author="Joseph Conrad")
print("b1.stock_amount: ", b1.stock_amount)

store.buy(b1, 100)
print("b1 stock_amount: ", b1.stock_amount)
print("b1 stock_value: ", b1.stock_value())
print("store total worth of products:  ", store.total_worth_of_products)

store.buy(b2, 100)
store.buy(b3, 100)
print("store balance: ", store.balance)

for key, value in store.transactions.items():
    print(key, value)

print("b1 selling price:", b1.selling_price)
print("b2 selling price:", b2.selling_price)
print("b3 selling price:", b3.selling_price)

a1 = Album("The Division Bell", 30, "Pink Floyd")
a2 = Album("Abbey Road", 35, "The Beatles")
a1.add_songs(["cluster one", "high hopes", "lost for words", "poles apart"])
print("a1 songs: ",a1.songs)

store.buy(a1, 100)
store.buy(a2, 100)
print("a1 profit: ", a1.profit_rate)
print("a1 selling price: ", a1.selling_price)

a1.set_profit_rate = 1.9
a1.set_profit_rate = 1.5

print("a1 selling price: ", a1.selling_price)

print("store total worth of products: ", store.total_worth_of_products)

print("store balance: ", store.balance)

store.buy(a1, 100000)

store.sell(b1, 150)

print("store total worth of products: ", store.total_worth_of_products)

store.sell(b1, 99)
store.sell(b2, 99)
store.sell(b3, 99)

print("store balance: ", store.balance)

store.sell(a1, 99)
store.sell(a2, 100)

print("store balance: ", store.balance)

print("store compute profit: ", store.compute_profit())

print(store.transactions)


store.search("an")
store.search("Beatles")
store.search("Pink")

