import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        values = [
            '1', '2', '3', '-',
            '4', '5', '6', '*',
            '7', '8', '9', '/',
            '0', '.', '=', '+'
        ]
        positions = [(i, j) for i in range(4) for j in range(4)]
        # position is an array of tuples
        pprint("positions = "+str(positions))
        # self.setGeometry(300, 300, 300, 120)
        for position, value in zip(positions, values):
            print("position = " + str(position))
            print("value = " + str(value))
            if value == '':
                continue
            button = QPushButton(value)
            grid_layout.addWidget(button, *position)
        self.setWindowTitle('This is an example of Grid layout')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())