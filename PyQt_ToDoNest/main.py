import sys
from PyQt6 import uic
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# подключаю дизайн и при нажатиях на разные кнопки, выполняются разные действия
class Start_of_working(QMainWindow):  # класс в котором все подключается и выполняется
    def __init__(self):
        super(Start_of_working, self).__init__()
        try:
            uic.loadUi('/Users/timbudygin/PycharmProjects/ToDoNest_By_Timofei/ToDoNest_By_Timofei.ui', self)
        except FileNotFoundError as f:
            print(f'файл не найден {f}')
        try:
            self.change_crt.clicked.connect(self.change_crt_f)
            self.add_task.clicked.connect(self.add_task_f)
            self.checkBox_1.clicked.connect(self.did_task_f1)
            self.checkBox_2.clicked.connect(self.did_task_f2)
            self.checkBox_3.clicked.connect(self.did_task_f3)
            self.checkBox_4.clicked.connect(self.did_task_f4)
            self.add_ddl1.clicked.connect(self.add_ddl_f1)
            self.add_ddl2.clicked.connect(self.add_ddl_f2)
            self.add_ddl3.clicked.connect(self.add_ddl_f3)
            self.add_ddl4.clicked.connect(self.add_ddl_f4)
        except AttributeError as a:
            print(f"не найдено название при нажатии на кнопку {a}")
        self.quantity_in_1 = 0
        self.quantity_in_2 = 0
        self.quantity_in_3 = 0
        self.quantity_in_4 = 0
        self.num_with_ddl1 = []
        self.num_with_ddl2 = []
        self.num_with_ddl3 = []
        self.num_with_ddl4 = []
        self.months = {
            1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря"
        }

    def change_crt_f(self):  # функция для изменения критериев
        name, ok_pressed = QInputDialog.getInt(self, "Введите номер критерия",
                                               "Какой критерий вы хотите поменять?", 1, 1, 4, 1)
        if ok_pressed:
            name1, ok_pressed1 = QInputDialog.getText(self, "Введите новое название", "Какое новое название?")
            try:
                if ok_pressed1:
                    if name == 1:
                        self.crt_1.setText(name1)
                    elif name == 2:
                        self.crt_2.setText(name1)
                    elif name == 3:
                        self.crt_3.setText(name1)
                    elif name == 4:
                        self.crt_4.setText(name1)
            except AttributeError as a:
                print(f"не найдено название в изменение критериев{a}")
            except Exception as e:
                print(e)

    def add_task_f(self):  # добаление заданий в критерии
        name, ok_pressed = QInputDialog.getInt(self, "Введите номер критерия",
                                               "В какой критерий вы хотите добавить задание?", 1, 1, 4, 1)
        if ok_pressed:
            name1, ok_pressed1 = QInputDialog.getText(self, "Введите новое задание", "Какое новое задание?")
            try:
                if ok_pressed1 and name1 != "":
                    if name == 1:
                        self.quantity_in_1 += 1
                        if self.quantity_in_1 == 1:
                            self.tasks_1.setText(f"{self.quantity_in_1}. {name1}")
                        else:
                            self.tasks_1.setText(f"{self.tasks_1.toPlainText()}\n{self.quantity_in_1}. {name1}")
                    elif name == 2:
                        self.quantity_in_2 += 1
                        if self.quantity_in_2 == 1:
                            self.tasks_2.setText(f"{self.quantity_in_2}. {name1}")
                        else:
                            self.tasks_2.setText(f"{self.tasks_2.toPlainText()}\n{self.quantity_in_2}. {name1}")
                    elif name == 3:
                        self.quantity_in_3 += 1
                        if self.quantity_in_3 == 1:
                            self.tasks_3.setText(f"{self.quantity_in_3}. {name1}")
                        else:
                            self.tasks_3.setText(f"{self.tasks_3.toPlainText()}\n{self.quantity_in_3}. {name1}")
                    elif name == 4:
                        self.quantity_in_4 += 1
                        if self.quantity_in_4 == 1:
                            self.tasks_4.setText(f"{self.quantity_in_4}. {name1}")
                        else:
                            self.tasks_4.setText(f"{self.tasks_4.toPlainText()}\n{self.quantity_in_4}. {name1}")
            except AttributeError as a:
                print(f"не найдено название в добавлении заданий{a}")
            except Exception as e:
                print(e)

    def did_task_f1(self):  # убираем сделанные задания в 1 критерии
        if len(self.tasks_1.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "Какое задание вы сделали?", 1, 1, self.quantity_in_1, 1)
            try:
                if ok_pressed:
                    text_from_brw = self.tasks_1.toPlainText().split("\n")
                    from db.db import add_tasks
                    did_t = text_from_brw[name - 1]
                    kol_vo_num = 0
                    if name - 1 in self.num_with_ddl1:
                        del self.num_with_ddl1[self.num_with_ddl1[name - 1]]
                        for i in did_t[::-1]:
                            if i == ':':
                                kol_vo_num += 12
                                break
                            else:
                                kol_vo_num += 1
                        did_t = did_t[:-(kol_vo_num - 1)]
                    res = add_tasks(did_t)
                    for i in range(len(res)):
                        if i == 0:
                            self.label_1.setText(res[i])
                        elif i == 1:
                            self.label_2.setText(res[i])
                        elif i == 2:
                            self.label_3.setText(res[i])
                        elif i == 3:
                            self.label_4.setText(res[i])
                        elif i == 4:
                            self.label_5.setText(res[i])
                        elif i == 5:
                            self.label_6.setText(res[i])
                        elif i == 6:
                            self.label_7.setText(res[i])
                        elif i == 7:
                            self.label_8.setText(res[i])
                        elif i == 8:
                            self.label_9.setText(res[i])
                        elif i == 9:
                            self.label_10.setText(res[i])
                    del text_from_brw[name - 1]
                    self.quantity_in_1 -= 1
                    if self.quantity_in_1 > 0:
                        for i in range(self.quantity_in_1):
                            if i == 0:
                                self.tasks_1.setText(f"{i + 1}. {text_from_brw[i][3:]}")
                            else:
                                self.tasks_1.setText(f"{self.tasks_1.toPlainText()}\n{i + 1}. {text_from_brw[i][3:]}")
                    else:
                        self.tasks_1.clear()
                    for i in range(len(self.num_with_ddl1)):
                        self.num_with_ddl1[i] = self.num_with_ddl1[i] - 1
                self.checkBox_1.setChecked(False)
            except AttributeError as a:
                print(f"не найдено название в 1 критерии выполненных заданий{a}")
            except Exception as e:
                print(e)

    def did_task_f2(self):  # убираем сделанные задания в 2 критерии
        if len(self.tasks_2.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "Какое задание вы сделали?", 1, 1, self.quantity_in_2, 1)
            try:
                if ok_pressed:
                    text_from_brw = self.tasks_2.toPlainText().split("\n")
                    from db.db import add_tasks
                    did_t = text_from_brw[name - 1]
                    kol_vo_num = 0
                    if name - 1 in self.num_with_ddl2:
                        del self.num_with_ddl2[self.num_with_ddl2[name - 1]]
                        for i in did_t[::-1]:
                            if i == ':':
                                kol_vo_num += 12
                                break
                            else:
                                kol_vo_num += 1
                        did_t = did_t[:-(kol_vo_num - 1)]
                    res = add_tasks(did_t)
                    for i in range(len(res)):
                        if i == 0:
                            self.label_1.setText(res[i])
                        elif i == 1:
                            self.label_2.setText(res[i])
                        elif i == 2:
                            self.label_3.setText(res[i])
                        elif i == 3:
                            self.label_4.setText(res[i])
                        elif i == 4:
                            self.label_5.setText(res[i])
                        elif i == 5:
                            self.label_6.setText(res[i])
                        elif i == 6:
                            self.label_7.setText(res[i])
                        elif i == 7:
                            self.label_8.setText(res[i])
                        elif i == 8:
                            self.label_9.setText(res[i])
                        elif i == 9:
                            self.label_10.setText(res[i])
                    del text_from_brw[name - 1]
                    self.quantity_in_2 -= 1
                    if self.quantity_in_2 > 0:
                        for i in range(self.quantity_in_2):
                            if i == 0:
                                self.tasks_2.setText(f"{i + 1}. {text_from_brw[i][3:]}")
                            else:
                                self.tasks_2.setText(f"{self.tasks_2.toPlainText()}\n{i + 1}. {text_from_brw[i][3:]}")
                    else:
                        self.tasks_2.clear()
                    for i in range(len(self.num_with_ddl2)):
                        self.num_with_ddl2[i] = self.num_with_ddl2[i] - 1
                self.checkBox_2.setChecked(False)
            except AttributeError as a:
                print(f"не найдено название во 2 критерии выполненных заданий{a}")
            except Exception as e:
                print(e)

    def did_task_f3(self):  # убираем сделанные задания в 3 критерии
        if len(self.tasks_3.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "Какое задание вы сделали?", 1, 1, self.quantity_in_3, 1)
            try:
                if ok_pressed:
                    text_from_brw = self.tasks_3.toPlainText().split("\n")
                    from db.db import add_tasks
                    did_t = text_from_brw[name - 1]
                    kol_vo_num = 0
                    if name - 1 in self.num_with_ddl3:
                        del self.num_with_ddl3[self.num_with_ddl3[name - 1]]
                        for i in did_t[::-1]:
                            if i == ':':
                                kol_vo_num += 12
                                break
                            else:
                                kol_vo_num += 1
                        did_t = did_t[:-(kol_vo_num - 1)]
                    res = add_tasks(did_t)
                    for i in range(len(res)):
                        if i == 0:
                            self.label_1.setText(res[i])
                        elif i == 1:
                            self.label_2.setText(res[i])
                        elif i == 2:
                            self.label_3.setText(res[i])
                        elif i == 3:
                            self.label_4.setText(res[i])
                        elif i == 4:
                            self.label_5.setText(res[i])
                        elif i == 5:
                            self.label_6.setText(res[i])
                        elif i == 6:
                            self.label_7.setText(res[i])
                        elif i == 7:
                            self.label_8.setText(res[i])
                        elif i == 8:
                            self.label_9.setText(res[i])
                        elif i == 9:
                            self.label_10.setText(res[i])
                    del text_from_brw[name - 1]
                    self.quantity_in_3 -= 1
                    if self.quantity_in_3 > 0:
                        for i in range(self.quantity_in_3):
                            if i == 0:
                                self.tasks_3.setText(f"{i + 1}. {text_from_brw[i][3:]}")
                            else:
                                self.tasks_3.setText(f"{self.tasks_3.toPlainText()}\n{i + 1}. {text_from_brw[i][3:]}")
                    else:
                        self.tasks_3.clear()
                    for i in range(len(self.num_with_ddl3)):
                        self.num_with_ddl3[i] = self.num_with_ddl3[i] - 1
                self.checkBox_3.setChecked(False)
            except AttributeError as a:
                print(f"не найдено название в 3 критерии выполненных заданий{a}")
            except Exception as e:
                print(e)

    def did_task_f4(self):  # убираем сделанные задания в 4 критерии
        if len(self.tasks_4.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "Какое задание вы сделали?", 1, 1, self.quantity_in_4, 1)
            try:
                if ok_pressed:
                    text_from_brw = self.tasks_4.toPlainText().split("\n")
                    from db.db import add_tasks
                    did_t = text_from_brw[name - 1]
                    kol_vo_num = 0
                    if name - 1 in self.num_with_ddl4:
                        del self.num_with_ddl4[self.num_with_ddl4[name - 1]]
                        for i in did_t[::-1]:
                            if i == ':':
                                kol_vo_num += 12
                                break
                            else:
                                kol_vo_num += 1
                        did_t = did_t[:-(kol_vo_num - 1)]
                    res = add_tasks(did_t)
                    for i in range(len(res)):
                        if i == 0:
                            self.label_1.setText(res[i])
                        elif i == 1:
                            self.label_2.setText(res[i])
                        elif i == 2:
                            self.label_3.setText(res[i])
                        elif i == 3:
                            self.label_4.setText(res[i])
                        elif i == 4:
                            self.label_5.setText(res[i])
                        elif i == 5:
                            self.label_6.setText(res[i])
                        elif i == 6:
                            self.label_7.setText(res[i])
                        elif i == 7:
                            self.label_8.setText(res[i])
                        elif i == 8:
                            self.label_9.setText(res[i])
                        elif i == 9:
                            self.label_10.setText(res[i])
                    del text_from_brw[name - 1]
                    self.quantity_in_4 -= 1
                    if self.quantity_in_4 > 0:
                        for i in range(self.quantity_in_4):
                            if i == 0:
                                self.tasks_4.setText(f"{i + 1}. {text_from_brw[i][3:]}")
                            else:
                                self.tasks_4.setText(f"{self.tasks_4.toPlainText()}\n{i + 1}. {text_from_brw[i][3:]}")
                    else:
                        self.tasks_4.clear()
                    for i in range(len(self.num_with_ddl4)):
                        self.num_with_ddl4[i] = self.num_with_ddl4[i] - 1
                self.checkBox_4.setChecked(False)
            except AttributeError as a:
                print(f"не найдено название в 4 критерии выполненных заданий{a}")
            except Exception as e:
                print(e)

    def add_ddl_f1(self):  # добавление дедлайнов в задания(по его номеру) в 1 критерии
        if len(self.tasks_1.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "К какому заданию вы хотите добавить дедлайн?", 1, 1,
                                                   self.quantity_in_1, 1)
            if ok_pressed:
                name1, ok_pressed1 = QInputDialog.getText(self, "Введите дату дедлайна",
                                                          "К какой дате вам нужно "
                                                          "сделать задание(включительно, в фоомате 00.00)?")
                try:
                    if ok_pressed1 and "." in name1:
                        name1 = name1.split(".")
                        if (int(name1[1]) == 1 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 2 and int(name1[0]) <= 29) or (
                                int(name1[1]) == 3 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 4 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 5 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 6 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 7 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 8 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 9 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 10 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 11 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 12 and int(name1[0]) <= 31):
                            if name - 1 not in self.num_with_ddl1:
                                text_from_brw = self.tasks_1.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                num_task += "         до: " + name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_1.clear()
                                self.num_with_ddl1.append(name - 1)
                                for i in range(self.quantity_in_1):
                                    if i == 0:
                                        self.tasks_1.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_1.setText(f"{self.tasks_1.toPlainText()}\n{text_from_brw[i]}")
                            else:
                                text_from_brw = self.tasks_1.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                kol_vo_num = 0
                                for i in num_task[::-1]:
                                    if i == ':':
                                        break
                                    else:
                                        kol_vo_num += 1
                                num_task = num_task[:-(kol_vo_num - 1)]
                                num_task += name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_1.clear()
                                for i in range(self.quantity_in_1):
                                    if i == 0:
                                        self.tasks_1.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_1.setText(f"{self.tasks_1.toPlainText()}\n{text_from_brw[i]}")
                except AttributeError as a:
                    print(f"не найдено название в 1 критерии добавления дедлайнов{a}")
                except Exception as e:
                    print(e)

    def add_ddl_f2(self):  # добавление дедлайнов в задания(по его номеру) в 2 критерии
        if len(self.tasks_2.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "К какому заданию вы хотите добавить дедлайн?", 1, 1,
                                                   self.quantity_in_2, 1)
            if ok_pressed:
                name1, ok_pressed1 = QInputDialog.getText(self, "Введите дату дедлайна",
                                                          "К какой дате вам нужно "
                                                          "сделать задание(включительно, в фоомате 00.00)?")
                try:
                    if ok_pressed1 and "." in name1:
                        name1 = name1.split(".")
                        if (int(name1[1]) == 1 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 2 and int(name1[0]) <= 29) or (
                                int(name1[1]) == 3 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 4 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 5 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 6 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 7 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 8 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 9 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 10 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 11 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 12 and int(name1[0]) <= 31):
                            if name - 1 not in self.num_with_ddl2:
                                text_from_brw = self.tasks_2.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                num_task += "         до: " + name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_2.clear()
                                self.num_with_ddl2.append(name - 1)
                                for i in range(self.quantity_in_2):
                                    if i == 0:
                                        self.tasks_2.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_2.setText(f"{self.tasks_2.toPlainText()}\n{text_from_brw[i]}")
                            else:
                                text_from_brw = self.tasks_2.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                kol_vo_num = 0
                                for i in num_task[::-1]:
                                    if i == ':':
                                        break
                                    else:
                                        kol_vo_num += 1
                                num_task = num_task[:-(kol_vo_num - 1)]
                                num_task += name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_2.clear()
                                for i in range(self.quantity_in_2):
                                    if i == 0:
                                        self.tasks_2.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_2.setText(f"{self.tasks_2.toPlainText()}\n{text_from_brw[i]}")
                except AttributeError as a:
                    print(f"не найдено название в 1 критерии добавления дедлайнов{a}")
                except Exception as e:
                    print(e)

    def add_ddl_f3(self):  # добавление дедлайнов в задания(по его номеру) в 3 критерии
        if len(self.tasks_3.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "К какому заданию вы хотите добавить дедлайн?", 1, 1,
                                                   self.quantity_in_3, 1)
            if ok_pressed:
                name1, ok_pressed1 = QInputDialog.getText(self, "Введите дату дедлайна",
                                                          "К какой дате вам нужно с"
                                                          "делать задание(включительно, в фоомате 00.00)?")
                try:
                    if ok_pressed1 and "." in name1:
                        name1 = name1.split(".")
                        print(name1)
                        if (int(name1[1]) == 1 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 2 and int(name1[0]) <= 29) or (
                                int(name1[1]) == 3 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 4 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 5 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 6 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 7 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 8 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 9 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 10 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 11 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 12 and int(name1[0]) <= 31):
                            if name - 1 not in self.num_with_ddl3:
                                text_from_brw = self.tasks_3.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                num_task += "         до: " + name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_3.clear()
                                self.num_with_ddl3.append(name - 1)
                                for i in range(self.quantity_in_3):
                                    if i == 0:
                                        self.tasks_3.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_3.setText(f"{self.tasks_3.toPlainText()}\n{text_from_brw[i]}")
                            else:
                                text_from_brw = self.tasks_3.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                kol_vo_num = 0
                                for i in num_task[::-1]:
                                    if i == ':':
                                        break
                                    else:
                                        kol_vo_num += 1
                                num_task = num_task[:-(kol_vo_num - 1)]
                                num_task += name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_3.clear()
                                for i in range(self.quantity_in_3):
                                    if i == 0:
                                        self.tasks_3.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_3.setText(f"{self.tasks_3.toPlainText()}\n{text_from_brw[i]}")
                except AttributeError as a:
                    print(f"не найдено название в 1 критерии добавления дедлайнов{a}")
                except Exception as e:
                    print(e)

    def add_ddl_f4(self):  # добавление дедлайнов в задания(по его номеру) в 4 критерии
        if len(self.tasks_4.toPlainText()) > 0:
            name, ok_pressed = QInputDialog.getInt(self, "Введите номер задания",
                                                   "К какому заданию вы хотите добавить дедлайн?", 1, 1,
                                                   self.quantity_in_4, 1)
            if ok_pressed:
                name1, ok_pressed1 = QInputDialog.getText(self, "Введите дату дедлайна",
                                                          "К какой дате вам нужно "
                                                          "сделать задание(включительно, в фоомате 00.00)?")
                try:
                    if ok_pressed1 and "." in name1:
                        name1 = name1.split(".")
                        print(name1)
                        if (int(name1[1]) == 1 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 2 and int(name1[0]) <= 29) or (
                                int(name1[1]) == 3 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 4 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 5 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 6 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 7 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 8 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 9 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 10 and int(name1[0]) <= 31) or (
                                int(name1[1]) == 11 and int(name1[0]) <= 30) or (
                                int(name1[1]) == 12 and int(name1[0]) <= 31):
                            if name - 1 not in self.num_with_ddl4:
                                text_from_brw = self.tasks_4.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                num_task += "         до: " + name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_4.clear()
                                self.num_with_ddl4.append(name - 1)
                                for i in range(self.quantity_in_4):
                                    if i == 0:
                                        self.tasks_4.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_4.setText(f"{self.tasks_4.toPlainText()}\n{text_from_brw[i]}")
                            else:
                                text_from_brw = self.tasks_4.toPlainText().split("\n")
                                num_task = text_from_brw[name - 1]
                                del text_from_brw[name - 1]
                                kol_vo_num = 0
                                for i in num_task[::-1]:
                                    if i == ':':
                                        break
                                    else:
                                        kol_vo_num += 1
                                num_task = num_task[:-(kol_vo_num - 1)]
                                num_task += name1[0] + " " + self.months[int(name1[1])]
                                text_from_brw.insert(name - 1, num_task)
                                self.tasks_4.clear()
                                for i in range(self.quantity_in_4):
                                    if i == 0:
                                        self.tasks_4.setText(f"{text_from_brw[i]}")
                                    else:
                                        self.tasks_4.setText(f"{self.tasks_4.toPlainText()}\n{text_from_brw[i]}")
                except AttributeError as a:
                    print(f"не найдено название в 1 критерии добавления дедлайнов{a}")
                except Exception as e:
                    print(e)


def main():
    sys.excepthook = except_hook
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    form = Start_of_working()
    form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
