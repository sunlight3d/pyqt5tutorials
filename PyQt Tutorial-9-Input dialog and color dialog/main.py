import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget,QPushButton, QApplication)

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.numberOfPressed = 0
        button1 = QPushButton("Button 1", self)
        button1.move(30, 50)

        button2 = QPushButton("Button 2", self)
        button2.move(150, 50)

        button1.clicked.connect(self.buttonClicked)
        button2.clicked.connect(self.buttonClicked)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Example of event handler')


    def buttonClicked(self):
        self.numberOfPressed = self.numberOfPressed + 1
        # pprint("button pressed. Number: "+str(self.numberOfPressed))
        sender = self.sender()
        pprint("You pressed: " + sender.text())

    def mousePressEvent(self, event):
        pprint("Mouse pressed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())