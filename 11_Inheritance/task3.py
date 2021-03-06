# Product Store


class Product:
    def __init__(self, type1, name, price):
        self.type = type1
        self.name = name
        self.price = price


bananas = Product('fruits', 'bananas', 30)
apples = Product('fruit', 'apples', 10)
buckwheat = Product('groats', 'buckwheat', 90)
chicken_wings = Product('meet', 'chicken_wings', 22)
pork_head = Product('meet', 'pork head', 33)


def except_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError as string:
            print(string)
        # return result
    return wrapper

class ProductStore:
    def __init__(self):
        self.store = []



    @except_decorator
    def add(self, product, amount):
        ''' Adds a specified quantity of a single product with a predefined price premium for your store(30 percent)'''
        self.store.append({
            'type':     product.type,
            'name':     product.name,
            'price':    product.price + (product.price * 0.3),
            'amount':   amount
        })


silmag = ProductStore()

print(apples)
silmag.add(apples, 100)

print(silmag.store)
