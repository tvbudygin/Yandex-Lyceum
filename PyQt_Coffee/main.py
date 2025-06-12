import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QInputDialog, QPushButton, QTextBrowser
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath('PyQt_coffee'))
DB_PATH = os.path.join(BASE_DIR, 'PyQt_coffee/data', 'coffee.sqlite')
a = {"Капучино": 1, "Эспрессо": 2, "Американо": 3, "Латте": 4}
add_val_k = []
add_val_e = []
add_val_a = []
add_val_l = []


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 600, 800, 600)
        self.setWindowTitle('кофе')

        self.cap = QPushButton(self)
        self.cap.move(0, 0)
        self.cap.resize(387, 32)
        self.cap.setText("Капучино")
        self.cap.clicked.connect(self.cap_f)

        self.americ = QPushButton(self)
        self.americ.move(389, 0)
        self.americ.resize(387, 32)
        self.americ.setText("Американо")
        self.americ.clicked.connect(self.americ_f)

        self.ecsp = QPushButton(self)
        self.ecsp.move(0, 34)
        self.ecsp.resize(387, 32)
        self.ecsp.setText("Эспрессо")
        self.ecsp.clicked.connect(self.ecsp_f)

        self.latte = QPushButton(self)
        self.latte.move(389, 34)
        self.latte.resize(387, 32)
        self.latte.setText("Латте")
        self.latte.clicked.connect(self.latte_f)

        self.changes = QPushButton(self)
        self.changes.move(0, 68)
        self.changes.resize(387, 32)
        self.changes.setText("больше возможностей")
        self.changes.clicked.connect(self.new_form)

        self.textB = QTextBrowser(self)
        self.textB.move(12, 122)
        self.textB.resize(776, 445)
        self.show()

    def latte_f(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
            WHERE id = 4""")
        for i in result:
            e = list(i)
            if len(add_val_l) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def ecsp_f(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
                    WHERE id = 2""")
        for i in result:
            e = list(i)
            if len(add_val_e) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")

        cur.close()

    def americ_f(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
                    WHERE id = 3""")
        for i in result:
            e = list(i)
            if len(add_val_a) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def cap_f(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
                    WHERE id = 1""")
        for i in result:
            e = list(i)
            if len(add_val_k) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def new_form(self):
        self.new_f = Changes()
        self.new_f.show()
        self.textB.clear()


class Changes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(311, 238, 311, 238)
        self.setWindowTitle('изминить кофе')

        self.add = QPushButton(self)
        self.add.move(6, 54)
        self.add.resize(299, 32)
        self.add.setText("добавить запись о кофе")
        self.add.clicked.connect(self.add_v)

        self.change = QPushButton(self)
        self.change.move(6, 134)
        self.change.resize(299, 32)
        self.change.setText("изминить запись о кофе")
        self.change.clicked.connect(self.change_v)
        self.show()

    def add_v(self):
        cofe, ok_pressed = QInputDialog.getItem(
            self, "Выбрать кофе", "Кофе",
            ("Капучино", "Эспрессо", "Американо", "Латте"), 0, False)
        if ok_pressed:
            name, ok_pressed = QInputDialog.getText(self, "Введите новую запись о кофе", "Новая запись")
            if ok_pressed:
                con = sqlite3.connect(DB_PATH)
                cur = con.cursor()
                result = cur.execute(f"UPDATE coffee SET новые = ? WHERE id = ?", (name, a[cofe]))
                con.commit()
                cur.close()
                if cofe == "Капучино":
                    add_val_k.append('новые')
                elif cofe == "Эспрессо":
                    add_val_e.append('новые')
                elif cofe == "Американо":
                    add_val_a.append('новые')
                elif cofe == "Латте":
                    add_val_l.append('новые')
                self.close()

    def change_v(self):
        cofe, ok_pressed = QInputDialog.getItem(
            self, "Выбрать колонку", "Колонка",
            ("Капучино", "Эспрессо", "Американо", "Латте"), 0, False)
        if ok_pressed:
            if len(add_val_k) > 0 and cofe == "Капучино":
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_k), 0, False)
            elif len(add_val_e) > 0 and cofe == 'Эспрессо':
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_e), 0, False)
            elif len(add_val_a) > 0 and cofe == "Американо":
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_a), 0, False)
            elif len(add_val_l) > 0 and cofe == "Латте":
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_l), 0, False)
            else:
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка"), 0, False)
        if ok_pressed:
            name, ok_pressed = QInputDialog.getText(self, "Введите новое значение", "Новое значение")
            if ok_pressed:
                con = sqlite3.connect(DB_PATH)
                cur = con.cursor()
                result = cur.execute(f"UPDATE coffee SET {tabl} = ? WHERE id = ?", (name, a[cofe]))
                con.commit()
                cur.close()
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Coffee()
    form.show()
    sys.exit(app.exec())
