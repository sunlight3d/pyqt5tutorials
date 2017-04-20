import sys
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input arguments: "+str(sys.argv))
    window = QWidget()
    window.resize(300,500) # square
    window.move(100,100)
    window.setWindowTitle('Hello world !')
    window.show()
    sys.exit(app.exec_()) # The sys.exit() method ensures a clean exit.