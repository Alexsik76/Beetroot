from datetime import datetime
class CustomException(Exception):
    def __init__(self, msg):
        self.log(msg)


    def log(self, msg):
        string = f'''{datetime.now().strftime("%dth of %B '%y, %I:%M%p %Z")} ERROR {msg} \n'''
        with open('logs.txt', "a") as file:
            file.write(string)


raise CustomException(ArithmeticError)
