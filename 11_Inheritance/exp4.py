from datetime import datetime


class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        self.log()

    def log(self):
        string = f'''{datetime.now().strftime("%dth of %B '%y, %I:%M%p %Z")} ERROR {self.msg} \n'''
        with open('logs2.txt', "a") as file:
            file.write(string)


try:
    raise CustomException('999')
except CustomException:
    print('1')