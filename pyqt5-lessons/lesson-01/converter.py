import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout


class Course(QObject):
    def get(self):
        return 30.0


class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initLayouts()
        self._initSignals()

    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.updateConvertBtnStatus()

    def _initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)

        self.setCentralWidget(w)

    def _initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.srcAmount.valueChanged.connect(self.updateConvertBtnStatus)

    def onClick(self):
        value = self.srcAmount.value()

        if value:
            self.resultAmount.setValue(value / Course().get())

    def updateConvertBtnStatus(self):
        value = self.srcAmount.value()
        self.convertBtn.setEnabled(bool(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())
