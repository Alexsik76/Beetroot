from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.log()

    def log(self):
        string = f'''{datetime.now().strftime("%dth of %B '%y, %I:%M%p %Z")} ERROR {self.args} \n'''
        with open('logs2.txt', "a") as file:
            file.write(string)


try:
    raise CustomException(666)
except CustomException:
    print('Successfully')

class CustomException2(Exception):
    pass


# Працює:
try:
    x = 1 / 0
except Exception:
    print('Error')

cust2 = CustomException2()
# Не працює:
try:
    x = 1 / 0
except cust2:
    print('Error')