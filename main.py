import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loader = QUiLoader()
    ui_file = QFile("./ui/main.ui")  # или "ui/main.ui"

    if not ui_file.open(QFile.ReadOnly):
        print("Не удалось открыть main.ui")
        sys.exit(-1)

    window = loader.load(ui_file)
    ui_file.close()

    window.show()

    sys.exit(app.exec())
