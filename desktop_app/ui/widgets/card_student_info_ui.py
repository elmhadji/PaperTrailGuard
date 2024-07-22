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
        self.profile_image_label = QLabel(CardStudentInfo)
        self.profile_image_label.setObjectName(u"profile_image_label")
        self.profile_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.profile_image_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.info_preview_button = QPushButton(CardStudentInfo)
        self.info_preview_button.setObjectName(u"info_preview_button")
        self.info_preview_button.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.info_preview_button)

        self.degree_type_label = QLabel(CardStudentInfo)
        self.degree_type_label.setObjectName(u"degree_type_label")
        self.degree_type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.degree_type_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(CardStudentInfo)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.name_label = QLabel(CardStudentInfo)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 1, 1, 1)

        self.label_4 = QLabel(CardStudentInfo)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.birthday_label = QLabel(CardStudentInfo)
        self.birthday_label.setObjectName(u"birthday_label")

        self.gridLayout.addWidget(self.birthday_label, 1, 1, 1, 1)

        self.label_5 = QLabel(CardStudentInfo)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.birth_place_label = QLabel(CardStudentInfo)
        self.birth_place_label.setObjectName(u"birth_place_label")

        self.gridLayout.addWidget(self.birth_place_label, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.print_pdf_button = QPushButton(CardStudentInfo)
        self.print_pdf_button.setObjectName(u"print_pdf_button")

        self.horizontalLayout.addWidget(self.print_pdf_button)

        self.edit_button = QPushButton(CardStudentInfo)
        self.edit_button.setObjectName(u"edit_button")

        self.horizontalLayout.addWidget(self.edit_button)

        self.delete_button = QPushButton(CardStudentInfo)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout.addWidget(self.delete_button)


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
        self.profile_image_label.setText(QCoreApplication.translate("CardStudentInfo", u"Profile Image", None))
        self.info_preview_button.setText("")
        self.degree_type_label.setText(QCoreApplication.translate("CardStudentInfo", u"Degree type", None))
        self.label_3.setText(QCoreApplication.translate("CardStudentInfo", u"Name", None))
        self.name_label.setText("")
        self.label_4.setText(QCoreApplication.translate("CardStudentInfo", u"Birthday", None))
        self.birthday_label.setText("")
        self.label_5.setText(QCoreApplication.translate("CardStudentInfo", u"Birth Place", None))
        self.birth_place_label.setText("")
        self.print_pdf_button.setText(QCoreApplication.translate("CardStudentInfo", u"print", None))
        self.edit_button.setText(QCoreApplication.translate("CardStudentInfo", u"edit", None))
        self.delete_button.setText(QCoreApplication.translate("CardStudentInfo", u"delete", None))
    # retranslateUi

