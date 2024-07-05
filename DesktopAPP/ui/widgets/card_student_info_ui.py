# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_student_info.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CardStudentInfo(object):
    def setupUi(self, CardStudentInfo):
        if not CardStudentInfo.objectName():
            CardStudentInfo.setObjectName(u"CardStudentInfo")
        CardStudentInfo.resize(476, 293)
        self.horizontalLayout_2 = QHBoxLayout(CardStudentInfo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CardStudentInfo)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(CardStudentInfo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(CardStudentInfo)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_6 = QLabel(CardStudentInfo)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_4 = QLabel(CardStudentInfo)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_7 = QLabel(CardStudentInfo)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_5 = QLabel(CardStudentInfo)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_8 = QLabel(CardStudentInfo)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(CardStudentInfo)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(CardStudentInfo)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(CardStudentInfo)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.retranslateUi(CardStudentInfo)

        QMetaObject.connectSlotsByName(CardStudentInfo)
    # setupUi

    def retranslateUi(self, CardStudentInfo):
        CardStudentInfo.setWindowTitle(QCoreApplication.translate("CardStudentInfo", u"Form", None))
        self.label.setText(QCoreApplication.translate("CardStudentInfo", u"Profile Image", None))
        self.label_2.setText(QCoreApplication.translate("CardStudentInfo", u"Degree type", None))
        self.label_3.setText(QCoreApplication.translate("CardStudentInfo", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("CardStudentInfo", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("CardStudentInfo", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("CardStudentInfo", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("CardStudentInfo", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("CardStudentInfo", u"TextLabel", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

