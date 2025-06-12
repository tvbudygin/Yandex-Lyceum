from random import randrange
import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton



class Circle(QMainWindow):
    def __init__(self):
        super(Circle, self).__init__()
        self.do_paint = False
        self.unitui()

    def unitui(self):
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('рисуй')
        self.btn1 = QPushButton(self)
        self.btn1.resize(790, 30)
        self.btn1.move(5, 750)
        self.btn1.setText("draw")
        self.btn1.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw_circle(self, qp):
        qp.setPen(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
        a = randrange(1, 600)
        qp.drawEllipse(10, 10, a, a)

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Circle()
    form.show()
    sys.exit(app.exec())
