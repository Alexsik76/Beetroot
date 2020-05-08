from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import operator
from calc1design import  Ui_MainWindow

def op_or_equal():
    pass

class MainWindow(QMainWindow, Ui_MainWindow):
    # input_str = ''
    # a, b, = None, None
    # current_op = ''
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.a = None
        self.b = None
        self.input_str = ''
        self.current_op = ''
 # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        # Setup operations.

        self.pushButton_add.pressed.connect(lambda: self.operation('add'))
        self.pushButton_sub.pressed.connect(lambda: self.operation('sub'))
        # self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        # self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        # self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7
        #
        # self.pushButton_pc.pressed.connect(self.operation_pc)
        self.pushButton_equal.pressed.connect(lambda: self.equals)
        # self.reset()

        self.show()

    def display(self):
        self.lcdNumber.display(float(self.input_str))

    def input_number(self, v):
        self.input_str += str(v)
        self.display()



    def operation(self, op:str):
        if self.input_str and self.a:
            self.b = float(self.input_str)
            try:
                rez = {
                    'add': self.a + self.b,
                    'sub': self.a - self.b,
                    'mul': self.a * self.b,
                    'div': self.a / self.b
                }[self.current_op]
            except ZeroDivisionError:
                self.lcdNumber.display('Err')
                self.a, self.b = None, None
            else:
                self.a, self.b = rez, None
                self.lcdNumber.display(rez)
        elif self.input_str:
            self.a = float(self.input_str)
        self.input_str = ''
        self.current_op = op
        # self.display()

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calc")

    window = MainWindow()
    app.exec_()