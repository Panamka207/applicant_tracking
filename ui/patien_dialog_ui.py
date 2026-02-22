# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patien_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PatientDialog(object):
    def setupUi(self, PatientDialog):
        if not PatientDialog.objectName():
            PatientDialog.setObjectName(u"PatientDialog")
        PatientDialog.resize(450, 400)
        self.vboxLayout = QVBoxLayout(PatientDialog)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(PatientDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.editLastName = QLineEdit(PatientDialog)
        self.editLastName.setObjectName(u"editLastName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editLastName)

        self.label1 = QLabel(PatientDialog)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.editFirstName = QLineEdit(PatientDialog)
        self.editFirstName.setObjectName(u"editFirstName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editFirstName)

        self.label2 = QLabel(PatientDialog)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label2)

        self.editMiddleName = QLineEdit(PatientDialog)
        self.editMiddleName.setObjectName(u"editMiddleName")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editMiddleName)

        self.label3 = QLabel(PatientDialog)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label3)

        self.editBirthDate = QDateEdit(PatientDialog)
        self.editBirthDate.setObjectName(u"editBirthDate")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editBirthDate)

        self.label4 = QLabel(PatientDialog)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label4)

        self.editPhone = QLineEdit(PatientDialog)
        self.editPhone.setObjectName(u"editPhone")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editPhone)

        self.label5 = QLabel(PatientDialog)
        self.label5.setObjectName(u"label5")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label5)

        self.comboDirection = QComboBox(PatientDialog)
        self.comboDirection.setObjectName(u"comboDirection")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboDirection)


        self.vboxLayout.addLayout(self.formLayout)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.btnSave = QPushButton(PatientDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.hboxLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(PatientDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.hboxLayout.addWidget(self.btnCancel)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(PatientDialog)

        QMetaObject.connectSlotsByName(PatientDialog)
    # setupUi

    def retranslateUi(self, PatientDialog):
        PatientDialog.setWindowTitle(QCoreApplication.translate("PatientDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0431\u0438\u0442\u0443\u0440\u0438\u0435\u043d\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("PatientDialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label1.setText(QCoreApplication.translate("PatientDialog", u"\u0418\u043c\u044f:", None))
        self.label2.setText(QCoreApplication.translate("PatientDialog", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.label3.setText(QCoreApplication.translate("PatientDialog", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.label4.setText(QCoreApplication.translate("PatientDialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.label5.setText(QCoreApplication.translate("PatientDialog", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435:", None))
        self.btnSave.setText(QCoreApplication.translate("PatientDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("PatientDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

