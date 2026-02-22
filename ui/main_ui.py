# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumWidth(200)
        self.sidebarFrame.setMaximumWidth(250)
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.lblTitle = QLabel(self.sidebarFrame)
        self.lblTitle.setObjectName(u"lblTitle")

        self.sidebarLayout.addWidget(self.lblTitle)

        self.btnPatients = QPushButton(self.sidebarFrame)
        self.btnPatients.setObjectName(u"btnPatients")

        self.sidebarLayout.addWidget(self.btnPatients)

        self.btnDirections = QPushButton(self.sidebarFrame)
        self.btnDirections.setObjectName(u"btnDirections")

        self.sidebarLayout.addWidget(self.btnDirections)

        self.btnExams = QPushButton(self.sidebarFrame)
        self.btnExams.setObjectName(u"btnExams")

        self.sidebarLayout.addWidget(self.btnExams)

        self.btnReports = QPushButton(self.sidebarFrame)
        self.btnReports.setObjectName(u"btnReports")

        self.sidebarLayout.addWidget(self.btnReports)

        self.sidebarSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarSpacer)


        self.mainLayout.addWidget(self.sidebarFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pagePatients = QWidget()
        self.pagePatients.setObjectName(u"pagePatients")
        self.patientsLayout = QVBoxLayout(self.pagePatients)
        self.patientsLayout.setObjectName(u"patientsLayout")
        self.searchFrame = QFrame(self.pagePatients)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchLayout = QHBoxLayout(self.searchFrame)
        self.searchLayout.setObjectName(u"searchLayout")
        self.lineSearch = QLineEdit(self.searchFrame)
        self.lineSearch.setObjectName(u"lineSearch")

        self.searchLayout.addWidget(self.lineSearch)

        self.btnSearch = QPushButton(self.searchFrame)
        self.btnSearch.setObjectName(u"btnSearch")

        self.searchLayout.addWidget(self.btnSearch)

        self.btnReset = QPushButton(self.searchFrame)
        self.btnReset.setObjectName(u"btnReset")

        self.searchLayout.addWidget(self.btnReset)


        self.patientsLayout.addWidget(self.searchFrame)

        self.tablePatients = QTableWidget(self.pagePatients)
        self.tablePatients.setObjectName(u"tablePatients")

        self.patientsLayout.addWidget(self.tablePatients)

        self.crudFrame = QFrame(self.pagePatients)
        self.crudFrame.setObjectName(u"crudFrame")
        self.crudLayout = QHBoxLayout(self.crudFrame)
        self.crudLayout.setObjectName(u"crudLayout")
        self.crudSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.crudLayout.addItem(self.crudSpacer)

        self.btnAddPatient = QPushButton(self.crudFrame)
        self.btnAddPatient.setObjectName(u"btnAddPatient")

        self.crudLayout.addWidget(self.btnAddPatient)

        self.btnEditPatient = QPushButton(self.crudFrame)
        self.btnEditPatient.setObjectName(u"btnEditPatient")

        self.crudLayout.addWidget(self.btnEditPatient)

        self.btnDeletePatient = QPushButton(self.crudFrame)
        self.btnDeletePatient.setObjectName(u"btnDeletePatient")

        self.crudLayout.addWidget(self.btnDeletePatient)


        self.patientsLayout.addWidget(self.crudFrame)

        self.stackedWidget.addWidget(self.pagePatients)
        self.pageDirections = QWidget()
        self.pageDirections.setObjectName(u"pageDirections")
        self.stackedWidget.addWidget(self.pageDirections)
        self.pageExams = QWidget()
        self.pageExams.setObjectName(u"pageExams")
        self.stackedWidget.addWidget(self.pageExams)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.stackedWidget.addWidget(self.pageReports)

        self.mainLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0443\u0447\u0435\u0442\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0415\u041d\u042e", None))
        self.btnPatients.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0446\u0438\u0435\u043d\u0442\u044b", None))
        self.btnDirections.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.btnExams.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0437\u0430\u043c\u0435\u043d\u044b", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.lineSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e, \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443...", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.btnAddPatient.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnEditPatient.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnDeletePatient.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

