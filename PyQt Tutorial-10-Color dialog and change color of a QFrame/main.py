import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        selected_color = QColor(0, 0, 255)
        self.button = QPushButton("Choose color", self)
        self.button.move(25, 25)
        self.button.clicked.connect(self.showColorDialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("QWidget { background-color: %s}" % selected_color.name())
        self.frame.setGeometry(150, 22, 50, 50)
        self.setGeometry(300, 300, 250,200)

    def showColorDialog(self):
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            self.frame.setStyleSheet("QWidget { background-color: %s}" % selected_color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())