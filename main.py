import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(235, 210, 52))
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        diameter = random.randint(20, 200)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
