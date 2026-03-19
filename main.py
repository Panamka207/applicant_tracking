import pymysql
import sys
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView


class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='applicant_tracking',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            print('бд подключена')
        except Exception as e:
            self.connection = None
            print('бд не подключена:', e)

    def select(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM `applicants`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            for res in result:
                print(res)

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
        self.setup_tables()

        # self.btnReports.clicked.connect(self.run)
        self.btnApplicants.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pageApplicants))
        self.btnDashboard.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pageDashboard))
        self.btnApplications.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pageApplications))
        self.btnDirections.clicked.connect(self.open_directions)
        self.btnDepartments.clicked.connect(self.open_departments)
        self.btnReports.clicked.connect(self.open_reports)

    def open_dashboard(self):
        self.stackedWidget.setCurrentWidget(self.pageDashboard)

    def open_applications(self):
        self.stackedWidget.setCurrentWidget(self.pageApplications)

    def open_directions(self):
        self.stackedWidget.setCurrentWidget(self.pageDirections)

    def open_departments(self):
        self.stackedWidget.setCurrentWidget(self.pageDepartments)

    def open_reports(self):
        self.stackedWidget.setCurrentWidget(self.pageReports)

    def setup_tables(self):
        self.tableApplicants.setColumnCount(12)
        self.tableApplicants.setHorizontalHeaderLabels(
            ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол', 'Номер телефона', 'Паспортные данные', 'Медицинская справка', 'Фото'])
        self.tableApplicants.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)


if __name__ == '__main__':
    db = Database()
    db.select()
    db.close()

    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec())
