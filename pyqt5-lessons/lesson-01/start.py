import sys

from PyQt5.QtWidgets import QApplication, QWidget

# QObject - базовый класс для всех классов
# QWidget - базовый класс (виджет) для всех виджетов

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(200, 100)
    w.show()

    sys.exit(app.exec_())
