import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget,QLineEdit, QGridLayout,QTextEdit,QLabel, QApplication)

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        label_title = QLabel("Product's name:")
        txt_title = QLineEdit()
        txt_title.setPlaceholderText("Enter your product...")

        txt_review = QTextEdit()
        txt_review.setPlaceholderText("Enter your opinion...")

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        grid_layout.addWidget(label_title, 1, 0) #column 1, row 0
        grid_layout.addWidget(txt_title, 1, 1) #column 1, row 1

        label_review = QLabel('Your review:')
        grid_layout.addWidget(label_review, 2, 0) #column 2, row 0
        grid_layout.addWidget(txt_review, 2, 1, 5, 1) #column 2, row 1 => to column 5, row 1

        self.setLayout(grid_layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Rate for your App in AppStore')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())