import sys
from pprint import pprint
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class TutorialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('This is PyQ5 Tutorial')
        self.statusBar().showMessage('This is a status bar')
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False) #only for MacOS

        file_menu = menuBar.addMenu('&File')
        exit_action = QAction(QIcon('icon_exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)
        self.setGeometry(300, 300, 400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())