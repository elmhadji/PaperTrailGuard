# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_preview_info.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)
from . import student_preview_info_rc

class Ui_StudentPreviewInfo(object):
    def setupUi(self, StudentPreviewInfo):
        if not StudentPreviewInfo.objectName():
            StudentPreviewInfo.setObjectName(u"StudentPreviewInfo")
        StudentPreviewInfo.resize(850, 450)
        StudentPreviewInfo.setMinimumSize(QSize(850, 450))
        StudentPreviewInfo.setStyleSheet(u"#StudentPreviewInfo {\n"
"	font: 12pt \"Noto Sans\";\n"
"}\n"
"\n"
"#StudentPreviewInfo QLineEdit, #StudentPreviewInfo QSpinBox{\n"
"	border: 1px solid  rgb(0, 94, 193);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#StudentPreviewInfo QComboBox, #StudentPreviewInfo QDateEdit {\n"
"	padding: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(StudentPreviewInfo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.student_picture = QLabel(self.centralwidget)
        self.student_picture.setObjectName(u"student_picture")
        self.student_picture.setMaximumSize(QSize(200, 200))
        self.student_picture.setPixmap(QPixmap(u":/Images/assets/images/default_profile.png"))
        self.student_picture.setScaledContents(True)
        self.student_picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.student_picture)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.name_input)

        self.birthday_input = QDateEdit(self.centralwidget)
        self.birthday_input.setObjectName(u"birthday_input")
        self.birthday_input.setReadOnly(True)
        self.birthday_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.verticalLayout_6.addWidget(self.birthday_input)

        self.birth_place_input = QLineEdit(self.centralwidget)
        self.birth_place_input.setObjectName(u"birth_place_input")
        self.birth_place_input.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.birth_place_input)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_7.setStretch(0, 3)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 4)

        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.university_input = QLineEdit(self.centralwidget)
        self.university_input.setObjectName(u"university_input")
        self.university_input.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.university_input)

        self.speciality_input = QLineEdit(self.centralwidget)
        self.speciality_input.setObjectName(u"speciality_input")
        self.speciality_input.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.speciality_input)

        self.domain_input = QLineEdit(self.centralwidget)
        self.domain_input.setObjectName(u"domain_input")
        self.domain_input.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.domain_input)

        self.sector_input = QLineEdit(self.centralwidget)
        self.sector_input.setObjectName(u"sector_input")
        self.sector_input.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.sector_input)

        self.departement_input = QLineEdit(self.centralwidget)
        self.departement_input.setObjectName(u"departement_input")
        self.departement_input.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.departement_input)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.degree = QLineEdit(self.centralwidget)
        self.degree.setObjectName(u"degree")
        self.degree.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.degree)

        self.preparation_year_spinbox = QSpinBox(self.centralwidget)
        self.preparation_year_spinbox.setObjectName(u"preparation_year_spinbox")
        self.preparation_year_spinbox.setWrapping(False)
        self.preparation_year_spinbox.setFrame(True)
        self.preparation_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preparation_year_spinbox.setReadOnly(True)
        self.preparation_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.preparation_year_spinbox.setProperty("showGroupSeparator", False)
        self.preparation_year_spinbox.setMinimum(1600)
        self.preparation_year_spinbox.setMaximum(2500)
        self.preparation_year_spinbox.setValue(2000)

        self.verticalLayout_3.addWidget(self.preparation_year_spinbox)

        self.registration_year_spinbox = QSpinBox(self.centralwidget)
        self.registration_year_spinbox.setObjectName(u"registration_year_spinbox")
        self.registration_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.registration_year_spinbox.setReadOnly(True)
        self.registration_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.registration_year_spinbox.setMinimum(1600)
        self.registration_year_spinbox.setMaximum(2500)
        self.registration_year_spinbox.setValue(2000)

        self.verticalLayout_3.addWidget(self.registration_year_spinbox)

        self.delibration_year_spinbox = QSpinBox(self.centralwidget)
        self.delibration_year_spinbox.setObjectName(u"delibration_year_spinbox")
        self.delibration_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delibration_year_spinbox.setReadOnly(True)
        self.delibration_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.delibration_year_spinbox.setMinimum(1600)
        self.delibration_year_spinbox.setMaximum(2500)
        self.delibration_year_spinbox.setValue(2000)

        self.verticalLayout_3.addWidget(self.delibration_year_spinbox)

        self.note_input = QLineEdit(self.centralwidget)
        self.note_input.setObjectName(u"note_input")
        self.note_input.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.note_input)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        StudentPreviewInfo.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StudentPreviewInfo)
        self.statusbar.setObjectName(u"statusbar")
        StudentPreviewInfo.setStatusBar(self.statusbar)

        self.retranslateUi(StudentPreviewInfo)

        QMetaObject.connectSlotsByName(StudentPreviewInfo)
    # setupUi

    def retranslateUi(self, StudentPreviewInfo):
        StudentPreviewInfo.setWindowTitle(QCoreApplication.translate("StudentPreviewInfo", u"Preview Student", None))
        self.student_picture.setText("")
        self.label_2.setText(QCoreApplication.translate("StudentPreviewInfo", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("StudentPreviewInfo", u"Birthday", None))
        self.label_4.setText(QCoreApplication.translate("StudentPreviewInfo", u"Place of birth", None))
        self.name_input.setText("")
        self.birthday_input.setDisplayFormat(QCoreApplication.translate("StudentPreviewInfo", u"dd_MM_yyyy", None))
        self.birth_place_input.setText("")
        self.label_6.setText(QCoreApplication.translate("StudentPreviewInfo", u"University", None))
        self.label_5.setText(QCoreApplication.translate("StudentPreviewInfo", u"Speciality", None))
        self.label_7.setText(QCoreApplication.translate("StudentPreviewInfo", u"Domain", None))
        self.label_8.setText(QCoreApplication.translate("StudentPreviewInfo", u"Sector", None))
        self.label_9.setText(QCoreApplication.translate("StudentPreviewInfo", u"Department", None))
        self.university_input.setText("")
        self.speciality_input.setText("")
        self.domain_input.setText("")
        self.sector_input.setText("")
        self.departement_input.setText("")
        self.label_10.setText(QCoreApplication.translate("StudentPreviewInfo", u"Degree", None))
        self.label_11.setText(QCoreApplication.translate("StudentPreviewInfo", u"Year Prepare", None))
        self.label_12.setText(QCoreApplication.translate("StudentPreviewInfo", u"Year Registration", None))
        self.label_13.setText(QCoreApplication.translate("StudentPreviewInfo", u"Date Deliberation", None))
        self.label_14.setText(QCoreApplication.translate("StudentPreviewInfo", u"Note", None))
        self.note_input.setText("")
    # retranslateUi

