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
        ForgetPassowrd.resize(367, 356)
        self.centralwidget = QWidget(ForgetPassowrd)
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


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
        self.label.setText(QCoreApplication.translate("ForgetPassowrd", u"Forget Password ", None))
        self.label_2.setText(QCoreApplication.translate("ForgetPassowrd", u"username", None))
        self.lineEdit.setText(QCoreApplication.translate("ForgetPassowrd", u"Admin", None))
        self.label_3.setText(QCoreApplication.translate("ForgetPassowrd", u"Password", None))
        self.lineEdit_2.setText(QCoreApplication.translate("ForgetPassowrd", u"Admin", None))
        self.pushButton.setText(QCoreApplication.translate("ForgetPassowrd", u"Return", None))
    # retranslateUi

