import sys
from pprint import pprint
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QLabel
# from PyQt5.QtGui import QIcon

class TutorialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('This is PyQ5 Tutorial')
        self.statusBar().showMessage('This is a status bar')
        label1 = QLabel('This is line 1 ', self)
        label1.move(20, 10)

        label2 = QLabel('This is line 2 ', self)
        label2.move(40, 40)

        label2 = QLabel('This is line 3 ', self)
        label2.move(60, 70)

        self.setGeometry(300, 300, 1000, 1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())