from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import operator
from calc1design import  Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
 # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        # self.reset()

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calc")

    window = MainWindow()
    app.exec_()