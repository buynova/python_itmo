import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# QObject - базовый класс для всех классов
# QWidget - базовый класс (виджет) для всех виджетов


class LittleBig(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._increment = True

        self._initUi()
        self._initLayouts()
        self._initSignals()

    def _initUi(self):
        self.setWindowTitle('Little Big')
        self.resize(400, 300)

        self.setMinimumSize(300, 200)
        self.setMaximumSize(600, 400)

        self.btn = QPushButton('OK', self)

    def _initLayouts(self):
        self.setCentralWidget(self.btn)

    def _initSignals(self):
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        if self._increment:
            self.resize(self.width() + 10, self.height() + 10)
        else:
            self.resize(self.width() - 10, self.height() - 10)

        if self.width() <= self.minimumWidth():
            self._increment = True
        elif self.width() >= self.maximumWidth():
            self._increment = False

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = LittleBig()
    w.show()

    sys.exit(app.exec_())
