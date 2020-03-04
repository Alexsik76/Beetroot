
class Persona:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    age = 0
    health = 100
    money = 0
    larder = {'meet': 0, 'fruits': 0, 'milk': 0, 'bread': 0}
    craft = 0
    land = 0
    salary = 0
    # calculating income

    def income(self):
        # each unit of the earth brings a random amount
        # of meet, fruits, milk, bread
        meet = self.land * (randint(0, 1))
        fruits = self.land * (randint(0, 50))
        milk = self.land * (randint(0, 30))
        bread = self.land * (randint(0, 3))
        # each unit of the craft brings a random amount
        # of money
        income_money = self.craft * (randint(0, 15))
        # updating the value
        # - products
        temp_products = [bread, milk, fruits, meet]
        for item in self.larder:
            self.larder[item] += temp_products.pop()
        # - money
            self.money += (income_money + self.salary)

    # Guideline Daily Amount

    def gda(self):
        if self.age < 18:
            return randint(1500, 2000)
        elif self.age >= 18 and self.sex == 'female':
            return randint(1800, 2200)
        else:
            return randint(2200, 2700)

    def sale(self, item, price, number):
        if self.larder[item] >= number:
            self.larder[item] -= number
            self.money += (number * price)
        else:
            print('Товар у такій кількості відсутній!')

    def purchase(self, item, price, number):
        if (price * number) >= self.money:
            self.larder[item] += number
            self.money -= (number * price)
