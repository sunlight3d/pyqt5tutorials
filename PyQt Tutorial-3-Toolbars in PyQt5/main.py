import sys
from pprint import pprint
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class TutorialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('This is PyQ5 Tutorial')
        self.statusBar().showMessage('This is a status bar')

        self.toolbar = self.addToolBar('Save')

        save_action = QAction(QIcon('icon_save.png'), '&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save program') # show when move mouse to the icon

        exit_action = QAction(QIcon('icon_exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program')  # show when move mouse to the icon
        exit_action.triggered.connect(qApp.quit)

        self.toolbar.addAction(save_action)
        self.toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())
