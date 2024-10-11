import sys

from PyQt6.QtWidgets import QWidget, QApplication

from layout import Ui_Dialog


class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(self.button_click)
        self.show()


    def button_click(self):
        name = self.ui.nameEdit.text()
        self.ui.resultLabel.setText(f'Witaj {name}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())