import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QLabel)
from PyQt5 import  QtCore

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("This is a label example !")
        label.setAlignment(QtCore.Qt.AlignHCenter)

        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        horizontal_box1 = QHBoxLayout()
        horizontal_box1.addWidget(label)

        horizontal_box2 = QHBoxLayout()
        horizontal_box2.addWidget(ok_button)
        horizontal_box2.addWidget(cancel_button)

        vertical_box = QVBoxLayout()
        vertical_box.addStretch(1)
        vertical_box.addLayout(horizontal_box1)
        vertical_box.addLayout(horizontal_box2)

        self.setLayout(vertical_box)

        self.setWindowTitle('This is an example of Horizontal box layout')
        self.setGeometry(300, 300, 300, 120)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())