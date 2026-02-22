# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'direction_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_DirectionDialog(object):
    def setupUi(self, DirectionDialog):
        if not DirectionDialog.objectName():
            DirectionDialog.setObjectName(u"DirectionDialog")
        DirectionDialog.resize(400, 250)
        self.vboxLayout = QVBoxLayout(DirectionDialog)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DirectionDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.editDirectionName = QLineEdit(DirectionDialog)
        self.editDirectionName.setObjectName(u"editDirectionName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editDirectionName)

        self.label1 = QLabel(DirectionDialog)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.spinPlaces = QSpinBox(DirectionDialog)
        self.spinPlaces.setObjectName(u"spinPlaces")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinPlaces)


        self.vboxLayout.addLayout(self.formLayout)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.btnSave = QPushButton(DirectionDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.hboxLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(DirectionDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.hboxLayout.addWidget(self.btnCancel)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(DirectionDialog)

        QMetaObject.connectSlotsByName(DirectionDialog)
    # setupUi

    def retranslateUi(self, DirectionDialog):
        DirectionDialog.setWindowTitle(QCoreApplication.translate("DirectionDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("DirectionDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label1.setText(QCoreApplication.translate("DirectionDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442:", None))
    # retranslateUi

