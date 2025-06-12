import io
import sys

from PyQt6 import uic  # Импортируем класс uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QColorDialog
from PyQt6 import QtCore, QtGui, QtWidgets


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
        # Загружаем дизайн из этого объекта:
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.run)


    def run(self):
        name, ok_pressed = QInputDialog.getText(self, "Введи имя", "Как тебя зовут")
        age, ok1_pressed = QInputDialog.getInt(self, "Введи возраст:", "Сколько тебе лет:", 20, 14, 27, 1)
        color = QColorDialog.getColor(title="Выбери любимый цвет:")
        if color.isValid():
            self.image.setStyleSheet(f"background-color: {color.name()}")
        if ok_pressed * ok1_pressed:
            self.image.setText(f"Твое имя: {name} \nТвой возраст {age}")
        else:
            self.image.setText("Нажата кнопка: No")


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
