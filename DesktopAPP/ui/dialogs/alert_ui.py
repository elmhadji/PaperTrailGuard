# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alert.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Alert(object):
    def setupUi(self, Alert):
        if not Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.resize(401, 290)
        self.verticalLayout = QVBoxLayout(Alert)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Alert)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title)

        self.message = QLabel(Alert)
        self.message.setObjectName(u"message")
        font1 = QFont()
        font1.setPointSize(11)
        self.message.setFont(font1)

        self.verticalLayout.addWidget(self.message)

        self.buttonBox = QDialogButtonBox(Alert)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Alert)
        self.buttonBox.accepted.connect(Alert.accept)
        self.buttonBox.rejected.connect(Alert.reject)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Alert", u"Title", None))
        self.message.setText(QCoreApplication.translate("Alert", u"Alert Content", None))
    # retranslateUi

