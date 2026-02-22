from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys


def load_ui(path):
    loader = QUiLoader()
    ui_file = QFile(path)
    ui_file.open(QFile.ReadOnly)
    window = loader.load(ui_file)
    ui_file.close()
    return window


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = load_ui("ui/main.ui")

    # НАЙДЕМ КНОПКУ
    btn_add = main_window.findChild(type(main_window), "btnAddPatient")

    # ПРАВИЛЬНЫЙ способ:
    from PySide6.QtWidgets import QPushButton
    btn_add = main_window.findChild(QPushButton, "btnAddPatient")

    def open_applicant_dialog():
        dialog = load_ui("ui/applicant_dialog.ui")
        dialog.exec()

    btn_add.clicked.connect(open_applicant_dialog)

    main_window.show()
    sys.exit(app.exec())
