from PyQt6.QtWidgets import QWidget, QPushButton, QTableWidget, QApplication, QPlainTextEdit, QLabel, QComboBox, \
    QTableWidgetItem
import sys
import sqlite3


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Фильмотека')

        self.addButton = QPushButton('добавить', self)
        self.addButton.resize(self.addButton.sizeHint())
        self.addButton.move(0, 0)
        self.addButton.clicked.connect(self.adding)

        self.substract_button = QTableWidget(self)
        self.substract_button.resize(600, 560)
        self.substract_button.move(0, 40)
        self.abc()

    def abc(self):
        con = sqlite3.connect('data/films_db.sqlite')
        cur = con.cursor()
        result = cur.execute("""
                                SELECT films.id, films.title, films.year, genres.title, films.duration
                                FROM Films
                                INNER JOIN genres ON Films.genre = Genres.id
                                ;
                                """)
        self.result1 = []
        for elem in result:
            self.result1.append(elem)
        self.substract_button.setRowCount(len(self.result1))
        self.substract_button.setColumnCount(len(self.result1[0]))
        names = ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность']
        self.substract_button.setHorizontalHeaderLabels(names)
        k = 0
        self.result1.reverse()
        for elem in self.result1:
            self.substract_button.setItem(k, 0, QTableWidgetItem(str(elem[0])))
            self.substract_button.setItem(k, 1, QTableWidgetItem(str(elem[1])))
            self.substract_button.setItem(k, 2, QTableWidgetItem(str(elem[2])))
            self.substract_button.setItem(k, 3, QTableWidgetItem(str(elem[3])))
            self.substract_button.setItem(k, 4, QTableWidgetItem(str(elem[4])))
            k += 1

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()


class AddWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.p = parent
        con = sqlite3.connect('data/films_db.sqlite')
        cur = con.cursor()
        result = cur.execute("""
                SELECT *
                  FROM genres as g
                 ;
                """)
        self.params = dict()
        for i in result:
            self.params[i[1]] = i[0]
        con = sqlite3.connect('data/films_db.sqlite')
        cur = con.cursor()
        result = cur.execute("""
                            SELECT *
                            FROM films as f
                            ;
                            """)
        for elem in result:
            self.result1 = elem[0]
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Фильмотека')

        self.l1 = QLabel('Название', self)
        self.l1.move(2, 25)

        self.title = QPlainTextEdit(self)
        self.title.resize(300, 30)
        self.title.move(90, 20)

        self.l2 = QLabel('Год выпуска', self)
        self.l2.move(2, 85)

        self.year = QPlainTextEdit(self)
        self.year.resize(300, 30)
        self.year.move(90, 80)

        self.l3 = QLabel('Жанр', self)
        self.l3.move(2, 145)

        self.comboBox = QComboBox(self)
        self.comboBox.resize(300, 30)
        self.comboBox.move(90, 140)
        for i in self.params:
            self.comboBox.addItem(i)

        self.l4 = QLabel('Длина', self)
        self.l4.move(2, 205)

        self.duration = QPlainTextEdit(self)
        self.duration.resize(300, 30)
        self.duration.move(90, 200)

        self.pushButton = QPushButton('Добавить', self)
        self.pushButton.move(300, 350)
        self.pushButton.clicked.connect(self.get_adding_verdict)

        self.l5 = QLabel('', self)
        self.l5.move(50, 350)

    def get_adding_verdict(self):
        t1 = self.title.toPlainText()
        t2 = self.comboBox.currentText()
        t3 = self.year.toPlainText()
        t4 = self.duration.toPlainText()
        try:
            if t1 != '' and int(t3) and int(t4) and int(t3) <= 2024 and int(t4) >= 0:
                con = sqlite3.connect('data/films_db.sqlite')
                cur = con.cursor()
                result = cur.execute("""
                               INSERT INTO films(id, title, year ,genre ,duration) VALUES(?, ?, ?, ?, ?)
                               """, (int(self.result1) + 1, t1, int(t3), int(self.params[t2]), int(t4)))
                con.commit()
                self.p.abc()
                self.close()
                return True
            self.l5.setText('Неверно заполнена форма')
            self.l5.resize(self.l5.sizeHint())
            return False
        except Exception as e:
            print(e)
            self.l5.setText('Неверно заполнена форма')
            self.l5.resize(self.l5.sizeHint())
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
