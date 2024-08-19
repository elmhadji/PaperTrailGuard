# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restore_password.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_ForgetPassowrd(object):
    def setupUi(self, ForgetPassowrd):
        if not ForgetPassowrd.objectName():
            ForgetPassowrd.setObjectName(u"ForgetPassowrd")
        ForgetPassowrd.resize(380, 500)
        ForgetPassowrd.setMinimumSize(QSize(380, 500))
        ForgetPassowrd.setMaximumSize(QSize(380, 500))
        ForgetPassowrd.setStyleSheet(u"#ForgetPassword {\n"
"	font: 12pt \"Noto Sans\";\n"
"}\n"
"\n"
"#title {\n"
"	font: 700 25pt \"Noto Sans\";\n"
"	padding: 35px\n"
"}\n"
"\n"
"#username_input, #password_input, #return_button {\n"
"	border: 1px solid  rgb(0, 94, 193);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#return_button {\n"
"	background-color: rgb(0, 94, 193);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#return_button::hover {\n"
"	background-color: #0066cc;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(ForgetPassowrd)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.username_input = QLineEdit(self.centralwidget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setEnabled(True)
        self.username_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username_input.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_input)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEnabled(True)
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_input.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_input)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.return_button = QPushButton(self.centralwidget)
        self.return_button.setObjectName(u"return_button")

        self.horizontalLayout.addWidget(self.return_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        ForgetPassowrd.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(ForgetPassowrd)
        self.statusBar.setObjectName(u"statusBar")
        ForgetPassowrd.setStatusBar(self.statusBar)

        self.retranslateUi(ForgetPassowrd)

        QMetaObject.connectSlotsByName(ForgetPassowrd)
    # setupUi

    def retranslateUi(self, ForgetPassowrd):
        ForgetPassowrd.setWindowTitle(QCoreApplication.translate("ForgetPassowrd", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("ForgetPassowrd", u"Forget Password ", None))
        self.label_2.setText(QCoreApplication.translate("ForgetPassowrd", u"username", None))
        self.username_input.setText(QCoreApplication.translate("ForgetPassowrd", u"admin", None))
        self.label_3.setText(QCoreApplication.translate("ForgetPassowrd", u"Password", None))
        self.password_input.setText(QCoreApplication.translate("ForgetPassowrd", u"admin", None))
        self.return_button.setText(QCoreApplication.translate("ForgetPassowrd", u"Return", None))
    # retranslateUi

