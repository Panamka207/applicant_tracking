import pymysql
import sys
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem


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

    def count(self, table):
        with self.connection.cursor() as cursor:
            sql = f"SELECT COUNT(*) FROM `{table}`;"
            cursor.execute(sql)
            result = cursor.fetchall()
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
    # def search_table(self, table_name):
    #     '''Поиск и вывод данных в таблицу'''
    #     config = self.search_config[table_name]
    #     text = config['search_field'].text()
    #     result = self.db.search(table_name, text)

    #     config['table_widget'].setRowCount(len(result))
    #     for row_number, row_data in enumerate(result):
    #         for column_number, data in enumerate(row_data):
    #             config['table_widget'].setItem(row_number, column_number,
    #                                            QTableWidgetItem(str(data)))

    # def filter_table(self, table_name):
    #     if table_name == 'applicants':
    #         filters = {
    #             'gender': self.cmbGender.currentText(),
    #             'medical_certificate': '1' if self.cmbCertificate.currentText() == 'Есть' else '0',
    #             'foto': '1' if self.cmbPhoto.currentText() == 'Есть' else '0'
    #         }
    #         if any('Выберите' not in value for value in filters.values()):
    #             result = self.db.filter(table_name, filters)
    #         else:
    #             result = self.db.select(table_name)

    #     # Теперь result всегда определена!
    #     config = self.search_config[table_name]
    #     config['table_widget'].setRowCount(len(result))
    #     for row_number, row_data in enumerate(result):
    #         for column_number, data in enumerate(row_data):
    #             config['table_widget'].setItem(row_number, column_number,
    #                                            QTableWidgetItem(str(data)))


if __name__ == '__main__':
    # db = Database()
    # db.select()
    # db.close()

    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec())
