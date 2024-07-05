# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(367, 356)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.username_label)

        self.username_input = QLineEdit(self.centralwidget)
        self.username_input.setObjectName(u"username_input")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_input)

        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.password_label)

        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setObjectName(u"password_input")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_input)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.forget_password_link = QPushButton(self.centralwidget)
        self.forget_password_link.setObjectName(u"forget_password_link")

        self.horizontalLayout.addWidget(self.forget_password_link)

        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")

        self.horizontalLayout.addWidget(self.login_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        Login.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(Login)
        self.statusBar.setObjectName(u"statusBar")
        Login.setStatusBar(self.statusBar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.username_label.setText(QCoreApplication.translate("Login", u"username", None))
        self.password_label.setText(QCoreApplication.translate("Login", u"Password", None))
        self.forget_password_link.setText(QCoreApplication.translate("Login", u"forget password ?", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Log in", None))
    # retranslateUi

