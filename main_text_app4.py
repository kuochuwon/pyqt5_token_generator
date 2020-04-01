import sys
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QWidget,
                             QPushButton,
                             QAction,
                             QLineEdit,
                             QMessageBox,
                             QPlainTextEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Token generator'
        self.left = 50
        self.top = 50
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 180)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 240)

        # Create a copy button in the window
        self.copy_button = QPushButton('Copy', self)
        self.copy_button.move(260, 240)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.copy_button.clicked.connect(self.copy_click)

        # print on screen
        # self.textedit = QPlainTextEdit(self)
        # self.textedit.move(10, 10)
        # self.textedit.resize(400, 200)

        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com',
                             "bearer " + textboxValue, QMessageBox.Ok)

    @pyqtSlot()
    def copy_click(self):
        textboxValue = self.textbox.text()
        clipboard = QApplication.clipboard()
        clipboard.setText("bearer " + textboxValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
