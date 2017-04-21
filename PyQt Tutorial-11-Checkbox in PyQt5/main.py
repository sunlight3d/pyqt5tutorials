import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication)
from PyQt5.QtCore import Qt

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        checkbox = QCheckBox('Show window title', self)
        checkbox.move(30, 30)
        checkbox.stateChanged.connect(self.change_title)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("This is a window title !")

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('This is a window title !')
        else:
            self.setWindowTitle('')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())