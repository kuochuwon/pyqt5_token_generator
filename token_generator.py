import sys
import json
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
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 700
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create up textbox
        self.up_textbox = QLineEdit(self)
        self.up_textbox.move(20, 20)
        self.up_textbox.resize(280, 180)

        # Create textbox below
        # Add text field
        self.text = QPlainTextEdit(self)
        self.text.move(20, 310)
        self.text.resize(280, 180)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 240)

        # Create a copy button in the window
        self.copy_button = QPushButton('Copy', self)
        self.copy_button.move(260, 240)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.copy_button.clicked.connect(self.copy_click)

        self.show()

    def extract(text):
        json_data = json.loads(text)
        tokens = json_data.get("token")
        access_token = tokens.get("access_token")
        output = f"Bearer {access_token}"
        return output

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.up_textbox.text()
        self.text.insertPlainText(
            textboxValue + "\n")
        QMessageBox.question(self, 'Message - Token generator',
                             textboxValue, QMessageBox.Ok)

    @pyqtSlot()
    def copy_click(self):
        textboxValue = self.up_textbox.text()
        result_token = App.extract(textboxValue)
        self.text.insertPlainText(
            result_token + "\n")

        clipboard = QApplication.clipboard()
        clipboard.setText(result_token)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
