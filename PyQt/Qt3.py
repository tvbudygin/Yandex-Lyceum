import io
import sys

from PyQt6 import uic  # Импортируем класс uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor, QPainter

# Перехватчик ошибок
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# Код формы в xml:
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
    <class>MainWindow</class>
    <widget class="QMainWindow" name="MainWindow">
        <property name="geometry">
            <rect>
                <x>0</x>
                <y>0</y>
                <width>600</width>
                <height>400</height>
            </rect>
        </property>
        <property name="windowTitle">
            <string>Окно с надписью и кнопкой</string>
        </property>
        <widget class="QPushButton" name="pushButton">
            <property name="geometry">
                <rect>
                    <x>240</x>
                    <y>350</y>
                    <width>120</width>
                    <height>30</height>
                </rect>
            </property>
            <property name="text">
                <string>Нажми меня</string>
            </property>
        </widget>
        <widget class="QLabel" name="image">
            <property name="sizePolicy">
                <sizepolicy hsizetype="Maximum" vsizetype="Maximum">
                    <horstretch>0</horstretch>
                    <verstretch>0</verstretch>
                </sizepolicy>
            </property>
            <property name="minimumSize">
                <size>
                    <width>250</width>
                    <height>250</height>
                </size>
            </property>
            <property name="maximumSize">
                <size>
                    <width>2600</width>
                    <height>2600</height>
                </size>
            </property>
            <property name="text">
                <string>TextLabel</string>
            </property>
        </widget>
    </widget>
    <resources/>
    <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        # Вызываем инициализатор базового класса:
        super().__init__()
        # Создаем объект '_io.StringIO'
        f = io.StringIO(template)
        self.do_paint = False
        # Загружаем дизайн из этого объекта:
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, a0):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)

        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)

        qp.setBrush(QColor(255, 0, 255))
        qp.drawRect(30, 90, 120, 30)

    def run(self):
        button = QMessageBox.question(
            self,
            "Диалоговое окно с вопросом",
            "Нарисовать RGB флаг (да/нет)"
        )
        if button == QMessageBox.StandardButton.Yes:
            self.do_paint = True
        else:
            self.do_paint = False
        self.repaint()


if __name__ == '__main__':
    # Проверка на наличие уст-в с высоким разрешением:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    # Стандартный запуск приложения:
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
