import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


def load_ui(path):
    loader = QUiLoader()
    ui_file = QFile(path)

    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Не удалось открыть UI файл: {path}")

    window = loader.load(ui_file)
    ui_file.close()
    return window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загружаем UI
        self.ui = load_ui("ui/main_window.ui")
        self.setCentralWidget(self.ui)

        # Получаем stackedWidget
        self.stacked = self.ui.findChild(
            type(self.ui.stackedWidget), "stackedWidget")

        # Подключаем кнопки меню
        self.ui.btnPageApplicants.clicked.connect(
            lambda: self.stacked.setCurrentIndex(0)
        )
        self.ui.btnPageDirections.clicked.connect(
            lambda: self.stacked.setCurrentIndex(1)
        )
        self.ui.btnPageExams.clicked.connect(
            lambda: self.stacked.setCurrentIndex(2)
        )
        self.ui.btnPageReports.clicked.connect(
            lambda: self.stacked.setCurrentIndex(3)
        )

        # Открываем первую страницу по умолчанию
        self.stacked.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Учет абитуриентов")
    window.resize(1300, 800)
    window.show()

    sys.exit(app.exec())
