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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import card_student_info_rc

class Ui_CardStudentInfo(object):
    def setupUi(self, CardStudentInfo):
        if not CardStudentInfo.objectName():
            CardStudentInfo.setObjectName(u"CardStudentInfo")
        CardStudentInfo.resize(328, 248)
        CardStudentInfo.setStyleSheet(u"#CardStudentInfoFram {\n"
"	font: 12pt \"Noto Sans\";\n"
"	background-color: #E6ECEF;\n"
"	border: 2px solid #5B91B5;\n"
"	border-radius: 8px;\n"
"}\n"
"#CardStudentInfoFramSelected {\n"
"	background-color: #C39089;\n"
"	border: 2px solid #C39089;\n"
"}\n"
"\n"
"#CardStudentInfoFram QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"#CardStudentInfoFram QPushButton::hover{\n"
"	background-color: #005EC1;\n"
"	border: 1px solid #005EC1;\n"
"	border-radius: 11px;\n"
"}\n"
"\n"
"#CardStudentInfoFram #delete_button::hover{\n"
"	background-color: red;\n"
"	border: 1px solid red;\n"
"	border-radius: 11px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(CardStudentInfo)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.CardStudentInfoFram = QFrame(CardStudentInfo)
        self.CardStudentInfoFram.setObjectName(u"CardStudentInfoFram")
        self.CardStudentInfoFram.setFrameShape(QFrame.Shape.StyledPanel)
        self.CardStudentInfoFram.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.CardStudentInfoFram)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.profile_image_label = QLabel(self.CardStudentInfoFram)
        self.profile_image_label.setObjectName(u"profile_image_label")
        self.profile_image_label.setMaximumSize(QSize(150, 170))
        self.profile_image_label.setPixmap(QPixmap(u":/images/assets/images/default_profile.png"))
        self.profile_image_label.setScaledContents(True)
        self.profile_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.profile_image_label.setWordWrap(False)

        self.verticalLayout.addWidget(self.profile_image_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.info_preview_button = QPushButton(self.CardStudentInfoFram)
        self.info_preview_button.setObjectName(u"info_preview_button")
        self.info_preview_button.setMinimumSize(QSize(40, 40))
        self.info_preview_button.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/circle-info-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_preview_button.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.info_preview_button)

        self.degree_type_label = QLabel(self.CardStudentInfoFram)
        self.degree_type_label.setObjectName(u"degree_type_label")
        self.degree_type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.degree_type_label)

        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.CardStudentInfoFram)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.name_label = QLabel(self.CardStudentInfoFram)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 1, 1, 1)

        self.label_4 = QLabel(self.CardStudentInfoFram)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.birthday_label = QLabel(self.CardStudentInfoFram)
        self.birthday_label.setObjectName(u"birthday_label")

        self.gridLayout.addWidget(self.birthday_label, 1, 1, 1, 1)

        self.label_5 = QLabel(self.CardStudentInfoFram)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.birth_place_label = QLabel(self.CardStudentInfoFram)
        self.birth_place_label.setObjectName(u"birth_place_label")

        self.gridLayout.addWidget(self.birth_place_label, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.delete_button = QPushButton(self.CardStudentInfoFram)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/trash-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_button)

        self.print_pdf_button = QPushButton(self.CardStudentInfoFram)
        self.print_pdf_button.setObjectName(u"print_pdf_button")
        self.print_pdf_button.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/file-pdf-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.print_pdf_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.print_pdf_button)

        self.edit_button = QPushButton(self.CardStudentInfoFram)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/pencil-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.edit_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.CardStudentInfoFram)


        self.retranslateUi(CardStudentInfo)

        QMetaObject.connectSlotsByName(CardStudentInfo)
    # setupUi

    def retranslateUi(self, CardStudentInfo):
        CardStudentInfo.setWindowTitle(QCoreApplication.translate("CardStudentInfo", u"Form", None))
        self.profile_image_label.setText("")
        self.info_preview_button.setText("")
        self.degree_type_label.setText(QCoreApplication.translate("CardStudentInfo", u"Degree type", None))
        self.label_3.setText(QCoreApplication.translate("CardStudentInfo", u"Name", None))
        self.name_label.setText("")
        self.label_4.setText(QCoreApplication.translate("CardStudentInfo", u"Birthday", None))
        self.birthday_label.setText("")
        self.label_5.setText(QCoreApplication.translate("CardStudentInfo", u"Birth Place", None))
        self.birth_place_label.setText("")
        self.delete_button.setText("")
        self.print_pdf_button.setText("")
        self.edit_button.setText("")
    # retranslateUi

