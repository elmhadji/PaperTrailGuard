# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_register_info.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)
from . import student_register_info_rc

class Ui_StudentRegisterInfo(object):
    def setupUi(self, StudentRegisterInfo):
        if not StudentRegisterInfo.objectName():
            StudentRegisterInfo.setObjectName(u"StudentRegisterInfo")
        StudentRegisterInfo.resize(890, 450)
        StudentRegisterInfo.setMinimumSize(QSize(890, 450))
        StudentRegisterInfo.setStyleSheet(u"#StudentRegisterInfo {\n"
"	font: 12pt \"Noto Sans\";\n"
"}\n"
"\n"
"#StudentRegisterInfo QLineEdit, #StudentRegisterInfo QSpinBox, #StudentRegisterInfo QPushButton{\n"
"	border: 1px solid  rgb(0, 94, 193);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#StudentRegisterInfo QComboBox, #StudentRegisterInfo QDateEdit {\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#StudentRegisterInfo QPushButton {\n"
"	background-color: rgb(0, 94, 193);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#StudentRegisterInfo QPushButton::hover {\n"
"	background-color: #0066cc;\n"
"}\n"
"\n"
"#StudentRegisterInfo #reset_button::hover {\n"
"	background-color: red;\n"
"	border: 1px solid  red;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(StudentRegisterInfo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.student_picture = QLabel(self.centralwidget)
        self.student_picture.setObjectName(u"student_picture")
        self.student_picture.setMaximumSize(QSize(200, 200))
        self.student_picture.setPixmap(QPixmap(u":/Images/assets/images/default_profile.png"))
        self.student_picture.setScaledContents(True)
        self.student_picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.student_picture)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_7.addWidget(self.name_input)

        self.birthday_input = QDateEdit(self.centralwidget)
        self.birthday_input.setObjectName(u"birthday_input")
        self.birthday_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.birthday_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.verticalLayout_7.addWidget(self.birthday_input)

        self.birth_place_input = QLineEdit(self.centralwidget)
        self.birth_place_input.setObjectName(u"birth_place_input")

        self.verticalLayout_7.addWidget(self.birth_place_input)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.university_input = QLineEdit(self.centralwidget)
        self.university_input.setObjectName(u"university_input")

        self.verticalLayout_3.addWidget(self.university_input)

        self.speciality_input = QLineEdit(self.centralwidget)
        self.speciality_input.setObjectName(u"speciality_input")

        self.verticalLayout_3.addWidget(self.speciality_input)

        self.domain_input = QLineEdit(self.centralwidget)
        self.domain_input.setObjectName(u"domain_input")

        self.verticalLayout_3.addWidget(self.domain_input)

        self.sector_input = QLineEdit(self.centralwidget)
        self.sector_input.setObjectName(u"sector_input")

        self.verticalLayout_3.addWidget(self.sector_input)

        self.departement_input = QLineEdit(self.centralwidget)
        self.departement_input.setObjectName(u"departement_input")

        self.verticalLayout_3.addWidget(self.departement_input)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_4.addWidget(self.label_14)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_4.addWidget(self.label_13)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.note_input = QLineEdit(self.centralwidget)
        self.note_input.setObjectName(u"note_input")

        self.verticalLayout_5.addWidget(self.note_input)

        self.degree_combobox = QComboBox(self.centralwidget)
        self.degree_combobox.addItem("")
        self.degree_combobox.addItem("")
        self.degree_combobox.addItem("")
        self.degree_combobox.setObjectName(u"degree_combobox")
        self.degree_combobox.setEditable(False)

        self.verticalLayout_5.addWidget(self.degree_combobox)

        self.preparation_year_spinbox = QSpinBox(self.centralwidget)
        self.preparation_year_spinbox.setObjectName(u"preparation_year_spinbox")
        self.preparation_year_spinbox.setFrame(True)
        self.preparation_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preparation_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.preparation_year_spinbox.setMinimum(1600)
        self.preparation_year_spinbox.setMaximum(2500)
        self.preparation_year_spinbox.setValue(2000)

        self.verticalLayout_5.addWidget(self.preparation_year_spinbox)

        self.registration_year_spinbox = QSpinBox(self.centralwidget)
        self.registration_year_spinbox.setObjectName(u"registration_year_spinbox")
        self.registration_year_spinbox.setWrapping(False)
        self.registration_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.registration_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.registration_year_spinbox.setAccelerated(True)
        self.registration_year_spinbox.setProperty("showGroupSeparator", False)
        self.registration_year_spinbox.setMinimum(1600)
        self.registration_year_spinbox.setMaximum(2500)
        self.registration_year_spinbox.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.registration_year_spinbox.setValue(2000)

        self.verticalLayout_5.addWidget(self.registration_year_spinbox)

        self.delibration_year_spinbox = QSpinBox(self.centralwidget)
        self.delibration_year_spinbox.setObjectName(u"delibration_year_spinbox")
        self.delibration_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delibration_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.delibration_year_spinbox.setMinimum(1600)
        self.delibration_year_spinbox.setMaximum(2500)
        self.delibration_year_spinbox.setValue(2000)

        self.verticalLayout_5.addWidget(self.delibration_year_spinbox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.select_picture_button = QPushButton(self.centralwidget)
        self.select_picture_button.setObjectName(u"select_picture_button")
        icon = QIcon()
        icon.addFile(u":/Icons/assets/icons/image-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_picture_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.select_picture_button)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/assets/icons/rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reset_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.reset_button)

        self.register_button = QPushButton(self.centralwidget)
        self.register_button.setObjectName(u"register_button")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/assets/icons/user-plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.register_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.register_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.horizontalLayout_6.setStretch(1, 2)
        StudentRegisterInfo.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StudentRegisterInfo)
        self.statusbar.setObjectName(u"statusbar")
        StudentRegisterInfo.setStatusBar(self.statusbar)

        self.retranslateUi(StudentRegisterInfo)

        QMetaObject.connectSlotsByName(StudentRegisterInfo)
    # setupUi

    def retranslateUi(self, StudentRegisterInfo):
        StudentRegisterInfo.setWindowTitle(QCoreApplication.translate("StudentRegisterInfo", u"MainWindow", None))
        self.student_picture.setText("")
        self.label_2.setText(QCoreApplication.translate("StudentRegisterInfo", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("StudentRegisterInfo", u"Birthday", None))
        self.label_4.setText(QCoreApplication.translate("StudentRegisterInfo", u"Place of birth", None))
        self.name_input.setText("")
        self.birthday_input.setDisplayFormat(QCoreApplication.translate("StudentRegisterInfo", u"dd_MM_yyyy", None))
        self.birth_place_input.setText("")
        self.label_6.setText(QCoreApplication.translate("StudentRegisterInfo", u"University", None))
        self.label_5.setText(QCoreApplication.translate("StudentRegisterInfo", u"Speciality", None))
        self.label_7.setText(QCoreApplication.translate("StudentRegisterInfo", u"Domain", None))
        self.label_8.setText(QCoreApplication.translate("StudentRegisterInfo", u"Sector", None))
        self.label_9.setText(QCoreApplication.translate("StudentRegisterInfo", u"Department", None))
        self.university_input.setText("")
        self.speciality_input.setText("")
        self.domain_input.setText("")
        self.sector_input.setText("")
        self.departement_input.setText("")
        self.label_14.setText(QCoreApplication.translate("StudentRegisterInfo", u"Note", None))
        self.label_10.setText(QCoreApplication.translate("StudentRegisterInfo", u"Degree", None))
        self.label_11.setText(QCoreApplication.translate("StudentRegisterInfo", u"Year Prepare", None))
        self.label_12.setText(QCoreApplication.translate("StudentRegisterInfo", u"Year Registration", None))
        self.label_13.setText(QCoreApplication.translate("StudentRegisterInfo", u"Date Deliberation", None))
        self.note_input.setText("")
        self.degree_combobox.setItemText(0, QCoreApplication.translate("StudentRegisterInfo", u"Select Degree", None))
        self.degree_combobox.setItemText(1, QCoreApplication.translate("StudentRegisterInfo", u"Bachelor", None))
        self.degree_combobox.setItemText(2, QCoreApplication.translate("StudentRegisterInfo", u"Master", None))

        self.select_picture_button.setText(QCoreApplication.translate("StudentRegisterInfo", u"Select Image", None))
        self.reset_button.setText(QCoreApplication.translate("StudentRegisterInfo", u"Reset", None))
        self.register_button.setText(QCoreApplication.translate("StudentRegisterInfo", u"Register", None))
    # retranslateUi

