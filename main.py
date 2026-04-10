import pymysql
import sys
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QDialog, QMessageBox


class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                port=3307,
                user='root',
                password='123456',
                database='applicant_tracking',
                charset='utf8',
                # cursorclass=pymysql.cursors.DictCursor
            )
            print('бд подключена')
        except Exception as e:
            self.connection = None
            print('бд не подключена:', e)

    def select(self, table):
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM `{table}`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            # for res in result:
            #     print(res)
            print(f"Загружено {len(result)} строк из таблицы {table}")
            return result

    def filter(self, table, filters):
        filtered = {key: value for key,
                    value in filters.items() if 'Выберите' not in value}

        conditions = []
        for key, value in filtered.items():
            # Если значение - число (0 или 1), без кавычек
            if value in ['0', '1']:
                conditions.append(f"`{key}` = {value}")
            else:
                # Если строка - с кавычками
                conditions.append(f"`{key}` = '{value}'")

        where = ' AND '.join(conditions)
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM `{table}` WHERE {where};"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(sql)
            return result

    def insert_applicant(self, data):
        with self.connection.cursor() as cursor:
            sql = """INSERT INTO `applicants` 
                    (snils, last_name, first_name, middle_name, birth_date,
                    gender, phone, passport, medical_certificate, email, address, foto)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                data['snils'], data['last_name'], data['first_name'],
                data['middle_name'], data['birth_date'], data['gender'],
                data['phone'], data['passport'], data['medical_certificate'],
                data['email'], data['address'], data['foto']
            ))
            self.connection.commit()

    def insert_education(self, data):
        with self.connection.cursor() as cursor:
            sql = """INSERT INTO `education_documents`
                    (snils, school, graduation_year, average_grade)
                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (
                data['snils'], data['school'],
                data['graduation_year'], data['average_grade']
            ))
            self.connection.commit()

    def update_applicant(self, data):
        with self.connection.cursor() as cursor:
            sql = """UPDATE `applicants` SET
                    last_name = %s,
                    first_name = %s,
                    middle_name = %s,
                    birth_date = %s,
                    gender = %s,
                    phone = %s,
                    passport = %s,
                    medical_certificate = %s,
                    email = %s,
                    address = %s,
                    foto = %s
                    WHERE snils = %s"""
            cursor.execute(sql, (
                data['last_name'], data['first_name'],
                data['middle_name'], data['birth_date'], data['gender'],
                data['phone'], data['passport'], data['medical_certificate'],
                data['email'], data['address'], data['foto'],
                data['snils']
            ))
            self.connection.commit()

    def update_education(self, data):
        with self.connection.cursor() as cursor:
            sql = """UPDATE `education_documents` SET
                    school = %s,
                    graduation_year = %s,
                    average_grade = %s
                    WHERE snils = %s"""
            cursor.execute(sql, (
                data['school'],
                data['graduation_year'],
                data['average_grade'],
                data['snils']
            ))
            self.connection.commit()

    def delete_applicant(self, snils):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `applicants` WHERE snils = %s"
            cursor.execute(sql, (snils,))
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/login.ui', self)
        self.setup_ui()
        self.login_btn.clicked.connect(self.login)
        self.main_window = None

    def setup_ui(self):
        self.setWindowTitle("Авторизация")
        self.login_input.setFocus()

    def login(self):
        self.main_window = MyWidget()
        self.main_window.show()
        self.close()


class ApplicantDialog(QDialog):
    def __init__(self, db, snils=None, parent=None):
        super().__init__(parent)
        uic.loadUi('./ui/applicant_dialog.ui', self)
        self.db = db
        self.snils = snils
        self.btnSave.clicked.connect(self.save)
        self.btnCancel.clicked.connect(self.reject)
        self.inputSnils.setEnabled(True)

        if self.snils:
            self.setWindowTitle("Редактирование абитуриента")
            self.inputSnils.setEnabled(False)
            self.fill_data()
        else:
            self.setWindowTitle("Добавление абитуриента")
            self.inputSnils.setEnabled(True)

    def fill_data(self):
        '''Заполняем поля данными из БД'''
        with self.db.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM `applicants` WHERE snils = %s", (self.snils,))
            row = cursor.fetchone()

        if not row:
            return

        self.inputSnils.setText(str(row[0]))
        self.inputLastName.setText(str(row[1]))
        self.inputFirstName.setText(str(row[2]))
        self.inputMiddleName.setText(str(row[3]) if row[3] else '')
        self.inputBirthDate.setDate(row[4])

        gender_index = self.inputGender.findText(str(row[5]) if row[5] else '')
        self.inputGender.setCurrentIndex(
            gender_index if gender_index >= 0 else 0)

        self.inputPhone.setText(str(row[6]))
        self.inputPassport.setText(str(row[7]))
        self.inputMedical.setChecked(bool(row[8]))
        self.inputEmail.setText(str(row[9]))
        self.inputAddress.setText(str(row[10]))
        self.inputFoto.setChecked(bool(row[11]))

        with self.db.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM `education_documents` WHERE snils = %s", (self.snils,))
            edu = cursor.fetchone()

        if edu:
            self.inputSchool.setText(str(edu[3]))
            self.inputGraduationYear.setValue(int(edu[2]))
            self.inputAverageGrade.setValue(float(edu[4]))

    def validate(self):
        if not self.inputSnils.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите СНИЛС")
            return False
        if not self.inputLastName.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите фамилию")
            return False
        if not self.inputFirstName.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите имя")
            return False
        if not self.inputPhone.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите телефон")
            return False
        if not self.inputPassport.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите паспортные данные")
            return False
        if not self.inputEmail.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите email")
            return False
        if not self.inputAddress.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите адрес")
            return False
        if not self.inputSchool.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите название школы")
            return False
        phone = self.inputPhone.text().strip()
        if not phone:
            QMessageBox.warning(self, "Ошибка", "Введите телефон")
            return False
        if not phone.startswith('+'):
            QMessageBox.warning(
                self, "Ошибка", "Телефон должен начинаться с +")
            return False
        if len(phone) != 12:
            QMessageBox.warning(
                self, "Ошибка", "Телефон должен содержать ровно 12 символов")
            return False
        if not phone[1:].isdigit():
            QMessageBox.warning(
                self, "Ошибка", "Телефон должен содержать только цифры после +")
            return False
        return True

    def save(self):
        if not self.validate():
            return
        try:
            if self.snils:
                # РЕДАКТИРОВАНИЕ
                self.db.update_applicant({
                    'snils': self.snils,
                    'last_name': self.inputLastName.text().strip(),
                    'first_name': self.inputFirstName.text().strip(),
                    'middle_name': self.inputMiddleName.text().strip() or None,
                    'birth_date': self.inputBirthDate.date().toString("yyyy-MM-dd"),
                    'gender': self.inputGender.currentText() if self.inputGender.currentIndex() != 0 else None,
                    'phone': self.inputPhone.text().strip(),
                    'passport': self.inputPassport.text().strip(),
                    'medical_certificate': 1 if self.inputMedical.isChecked() else 0,
                    'email': self.inputEmail.text().strip(),
                    'address': self.inputAddress.text().strip(),
                    'foto': 1 if self.inputFoto.isChecked() else 0
                })

                self.db.update_education({
                    'snils': self.snils,
                    'school': self.inputSchool.text().strip(),
                    'graduation_year': self.inputGraduationYear.value(),
                    'average_grade': self.inputAverageGrade.value()
                })
                QMessageBox.information(
                    self, "Успех", "Данные успешно обновлены!")
            else:
                # ДОБАВЛЕНИЕ
                self.db.insert_applicant({
                    'snils': self.inputSnils.text().strip(),
                    'last_name': self.inputLastName.text().strip(),
                    'first_name': self.inputFirstName.text().strip(),
                    'middle_name': self.inputMiddleName.text().strip() or None,
                    'birth_date': self.inputBirthDate.date().toString("yyyy-MM-dd"),
                    'gender': self.inputGender.currentText() if self.inputGender.currentIndex() != 0 else None,
                    'phone': self.inputPhone.text().strip(),
                    'passport': self.inputPassport.text().strip(),
                    'medical_certificate': 1 if self.inputMedical.isChecked() else 0,
                    'email': self.inputEmail.text().strip(),
                    'address': self.inputAddress.text().strip(),
                    'foto': 1 if self.inputFoto.isChecked() else 0
                })
                self.db.insert_education({
                    'snils': self.inputSnils.text().strip(),
                    'school': self.inputSchool.text().strip(),
                    'graduation_year': self.inputGraduationYear.value(),
                    'average_grade': self.inputAverageGrade.value()
                })
                QMessageBox.information(
                    self, "Успех", "Абитуриент успешно добавлен!")

            self.accept()

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Ошибка при сохранении:\n{e}")


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/main_window.ui', self)

        self.db = Database()

        self.setup_tables()

        self.search_config = {
            'applicants': {
                'search_field': self.searchApplicants,
                'table_widget': self.tableApplicants
            },
            'applications': {
                'search_field': self.searchApplication,
                'table_widget': self.tableApplications
            },
            'departaments': {
                'search_field': self.searchDepartments,
                'table_widget': self.tableDepartments
            },
            'specialties': {
                'search_field': self.searchDirections,
                'table_widget': self.tableDirections
            }
        }

        self.connect_button()
        self.load_data()

        self.menu_buttons = [
            self.btnApplicants,
            self.btnDashboard,
            self.btnApplications,
            self.btnDirections,
            self.btnDepartments,
            self.btnReports
        ]
        self.btnDashboard.setChecked(True)
        self.stackedWidget.setCurrentWidget(self.pageDashboard)
        # self.btnReports.clicked.connect(self.run)

    def on_menu_click(self, btn):
        for b in self.menu_buttons:
            b.setChecked(False)  # снять со всех
        btn.setChecked(True)  # поставить на нажатую

    def connect_button(self):
        '''Подключение кнопок'''
        self.btnApplicants.clicked.connect(
            lambda: (self.stackedWidget.setCurrentWidget(self.pageApplicants), self.on_menu_click(self.btnApplicants)))
        self.btnDashboard.clicked.connect(
            lambda: (self.stackedWidget.setCurrentWidget(self.pageDashboard), self.on_menu_click(self.btnDashboard)))
        self.btnApplications.clicked.connect(
            lambda: (self.stackedWidget.setCurrentWidget(self.pageApplications), self.on_menu_click(self.btnApplications)))
        self.btnDirections.clicked.connect(
            lambda: (self.stackedWidget.setCurrentWidget(self.pageDirections), self.on_menu_click(self.btnDirections)))
        self.btnDepartments.clicked.connect(
            lambda: (self.stackedWidget.setCurrentWidget(self.pageDepartments), self.on_menu_click(self.btnDepartments)))
        self.btnReports.clicked.connect(
            lambda: (self.stackedWidget.setCurrentWidget(self.pageReports), self.on_menu_click(self.btnReports)))
        self.btnSearchApplicant.clicked.connect(lambda:
                                                (self.search_and_filter('applicants')))
        self.btnSearchApplication.clicked.connect(lambda:
                                                  self.search_and_filter('applications'))
        self.btnSearchDirection.clicked.connect(lambda:
                                                self.search_and_filter('specialties'))
        self.btnSearchDepartment.clicked.connect(lambda:
                                                 self.search_and_filter('departaments'))
        self.btnUpdateApplicant.clicked.connect(
            lambda: (self.load_data(), self.reset_selection(self.tableApplicants, self.searchApplicants)))

        self.btnUpdateApplication.clicked.connect(
            lambda: (self.load_data(), self.reset_selection(self.tableApplications, self.searchApplication)))

        self.btnUpdateDirection.clicked.connect(
            lambda: (self.load_data(), self.reset_selection(self.tableDirections, self.searchDirections)))

        self.btnUpdateDepartment.clicked.connect(
            lambda: (self.load_data(), self.reset_selection(self.tableDepartments, self.searchDepartments)))
        self.btnAddApplicant.clicked.connect(self.open_add_dialog)
        self.btnEditApplicant.clicked.connect(self.open_edit_dialog)
        self.btnDeleteApplicant.clicked.connect(self.delete_applicant)

    def setup_tables(self):
        '''Загрузка заголовков таблиц'''
        self.tableApplicants.setColumnCount(12)
        self.tableApplicants.setHorizontalHeaderLabels(
            ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол', 'Номер телефона', 'Паспортные данные', 'Медицинская справка', 'Электронная почта', 'Адрес', 'Фото'])
        self.tableApplicants.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        self.tableApplications.setColumnCount(5)
        self.tableApplications.setHorizontalHeaderLabels(
            ['id', 'СНИЛС', 'Код специальности', 'Дата подачи', 'Льгота'])
        self.tableApplications.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        self.tableApplications.setColumnHidden(0, True)

        self.tableDirections.setColumnCount(7)
        self.tableDirections.setHorizontalHeaderLabels(
            ['Код специальности', 'Название специальности', 'Название отделения', 'Количество бюджетных мест', 'Количество платных мест', 'Время обучения', 'Форма обучения'])
        self.tableDirections.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        # self.tableDirections.setColumnHidden(0, True)

        self.tableDepartments.setColumnCount(3)
        self.tableDepartments.setHorizontalHeaderLabels(
            ['id', 'Название отделения', 'Заведующий отделения'])
        self.tableDepartments.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        self.tableDepartments.setColumnHidden(0, True)

    def load_data(self):
        '''Загрузка данных из бд'''
        # self.statVal1 = ''

        tables = {
            'applicants': self.tableApplicants,
            'applications': self.tableApplications,
            'departaments': self.tableDepartments,
            'specialties': self.tableDirections
        }

        for key, value in tables.items():
            print(key, value)
            sql = self.db.select(key)

            if sql and len(sql) > 0:
                actual_columns = len(sql[0])
                print(
                    f"База вернула {actual_columns} колонок, таблица ожидает {value.columnCount()}")

                if actual_columns != value.columnCount():
                    value.setColumnCount(actual_columns)

            value.setRowCount(len(sql))
            for row_number, row_data in enumerate(sql):
                for column_number, data in enumerate(row_data):
                    value.setItem(row_number, column_number,
                                  QTableWidgetItem(str(data)))

    def search_and_filter(self, table_name):
        config = self.search_config[table_name]
        table_widget = config['table_widget']
        search_text = config['search_field'].text().lower()
        if search_text:  # поиск
            print(search_text)
            all_data = self.db.select(table_name)
            table_widget.setRowCount(len(all_data))
            table_widget.clearSelection()
            table_widget.setSelectionMode(
                table_widget.selectionMode().MultiSelection
            )

            for row_number, row_data in enumerate(all_data):
                flag = False
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    table_widget.setItem(row_number, column_number, item)
                    if search_text in str(data).lower():
                        print(data)
                        flag = True

                if flag:
                    table_widget.selectRow(row_number)

        else:  # фильтрация
            if table_name == 'applicants':
                filters = {
                    'gender': self.cmbGender.currentText(),
                    'medical_certificate': '1' if self.cmbCertificate.currentText() == 'Есть' else
                    ('0' if self.cmbCertificate.currentText()
                     == 'Нет' else 'Выберите фото'),
                    'foto': '1' if self.cmbPhoto.currentText() == 'Есть' else
                    ('0' if self.cmbPhoto.currentText()
                     == 'Нет' else 'Выберите фото')
                }
                all_default = all('Выберите' in v for v in filters.values())

                if all_default:
                    result = self.db.select(table_name)
                else:
                    result = self.db.filter(table_name, filters)
            else:
                result = self.db.select(table_name)

            config['table_widget'].setRowCount(len(result))
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    config['table_widget'].setItem(row_number, column_number,
                                                   QTableWidgetItem(str(data)))

    def reset_selection(self, table_widget, search_field):
        table_widget.clearSelection()
        table_widget.setSelectionMode(
            table_widget.SelectionMode.SingleSelection)
        search_field.clear()

    def open_add_dialog(self):
        dialog = ApplicantDialog(self.db, parent=self)
        if dialog.exec():
            self.load_data()

    def open_edit_dialog(self):
        selected = self.tableApplicants.selectedItems()
        if not selected:
            QMessageBox.warning(
                self, "Ошибка", "Выберите абитуриента для редактирования")
            return

        row = self.tableApplicants.currentRow()
        snils = self.tableApplicants.item(row, 0).text()

        dialog = ApplicantDialog(self.db, snils=snils, parent=self)
        if dialog.exec():
            self.load_data()

    def delete_applicant(self):
        selected = self.tableApplicants.selectedItems()
        if not selected:
            QMessageBox.warning(
                self, "Ошибка", "Выберите абитуриента для удаления")
            return

        row = self.tableApplicants.currentRow()
        snils = self.tableApplicants.item(row, 0).text()

        reply = QMessageBox.question(
            self, "Подтверждение",
            f"Вы уверены что хотите удалить абитуриента?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.db.delete_applicant(snils)
                QMessageBox.information(
                    self, "Успех", "Абитуриент успешно удалён!")
                self.load_data()
            except Exception as e:
                QMessageBox.critical(
                    self, "Ошибка", f"Ошибка при удалении:\n{e}")


if __name__ == '__main__':
    # db = Database()
    # db.select()
    # db.close()

    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec())
