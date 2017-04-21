import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget,QPushButton,QInputDialog, QLineEdit, QApplication)

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Open', self)
        self.btn.move(0, 20)
        self.btn.clicked.connect(self.showDialog)

        self.text_name = QLineEdit(self)
        self.text_name.move(100,22)
        self.text_name.setPlaceholderText("Enter your name:")

        self.setGeometry(300,300, 290, 140)
        self.setWindowTitle("Input dialog example")

    def showDialog(self):
        text, result = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if result == True:
            self.text_name.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())