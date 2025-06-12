import csv
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import (QMainWindow, QTableWidgetItem,
                             QFileDialog, QInputDialog, QMessageBox)


class MyWidget(QMainWindow):
    def __init__(self):
        # Вызываем инициализатор базового класса:
        super().__init__()
        uic.loadUi('forms/form1.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)  # Сигнал для кнопки 1
        self.pushButton_2.clicked.connect(self.run_2)  # Сигнал для кнопки 2
        # Обрати ВНИМАНИЕ!: имя элемента (кнопки) такое же, как и в QtDesigner

    def run(self):
        fname, ftype = QFileDialog.getOpenFileName(self,
                                                   "Выбери файл csv",
                                                   "data.csv",
                                                   "Файл (*.csv);;Файл (*.txt)")
        if not fname:
            return
        delimiter, ok_pressed = QInputDialog.getItem(self,
                                                     "Выбор разделителя",
                                                     "Выбери разделитель:",
                                                     (',', ';', '\t'))
        if not ok_pressed:
            return

        try:
            # raise FileNotFoundError("Файла нет!")
            with open(fname, encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
                title = next(reader)
                print(title)
                self.tableWidget.setColumnCount(len(title))
                self.tableWidget.setHorizontalHeaderLabels(title)
                self.tableWidget.setRowCount(0)

                for i, row in enumerate(reader):
                    self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                    for j, cell in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(cell))
            self.tableWidget.resizeColumnsToContents()

        except Exception as err:
            QMessageBox.critical(
                self,
                "Ошибка!",
                f"Произошла ошибка {err}")



    def run_2(self):
        delimiter, ok_pressed = QInputDialog.getItem(self,
                                                     "Выбор разделителя",
                                                     "Выбери разделитель:",
                                                     (',', ';', '\t'))
        if not ok_pressed:
            return
        fname, ftype = QFileDialog.getSaveFileName(self,
                                                   "Укажи файл csv",
                                                   "result.csv",
                                                   "Файл (*.csv);;Файл (*.txt)")
        if not fname:
            return

        with open(fname, 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            # Получение списка заголовков
            writer.writerow(
                [self.tableWidget.horizontalHeaderItem(i).text()
                 for i in range(self.tableWidget.columnCount())])
            for i in range(self.tableWidget.rowCount()):
                row = []
                for j in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(i, j)
                    if item is not None:
                        row.append(item.text())
                writer.writerow(row)

