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
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_StudentRegisterInfo(object):
    def setupUi(self, StudentRegisterInfo):
        if not StudentRegisterInfo.objectName():
            StudentRegisterInfo.setObjectName(u"StudentRegisterInfo")
        StudentRegisterInfo.resize(744, 450)
        self.centralwidget = QWidget(StudentRegisterInfo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_picture = QLabel(self.centralwidget)
        self.student_picture.setObjectName(u"student_picture")
        self.student_picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.student_picture)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout_3.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.name_input)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.birthday_input = QDateEdit(self.centralwidget)
        self.birthday_input.setObjectName(u"birthday_input")
        self.birthday_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.birthday_input)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.birth_place_input = QLineEdit(self.centralwidget)
        self.birth_place_input.setObjectName(u"birth_place_input")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.birth_place_input)


        self.verticalLayout.addLayout(self.formLayout_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.university_input = QLineEdit(self.centralwidget)
        self.university_input.setObjectName(u"university_input")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.university_input)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.speciality_input = QLineEdit(self.centralwidget)
        self.speciality_input.setObjectName(u"speciality_input")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.speciality_input)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.domain_input = QLineEdit(self.centralwidget)
        self.domain_input.setObjectName(u"domain_input")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.domain_input)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.sector_input = QLineEdit(self.centralwidget)
        self.sector_input.setObjectName(u"sector_input")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sector_input)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.departement_input = QLineEdit(self.centralwidget)
        self.departement_input.setObjectName(u"departement_input")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.departement_input)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_13)

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

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.registration_year_spinbox)

        self.preparation_year_spinbox = QSpinBox(self.centralwidget)
        self.preparation_year_spinbox.setObjectName(u"preparation_year_spinbox")
        self.preparation_year_spinbox.setFrame(True)
        self.preparation_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preparation_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.preparation_year_spinbox.setMinimum(1600)
        self.preparation_year_spinbox.setMaximum(2500)
        self.preparation_year_spinbox.setValue(2000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.preparation_year_spinbox)

        self.delibration_year_spinbox = QSpinBox(self.centralwidget)
        self.delibration_year_spinbox.setObjectName(u"delibration_year_spinbox")
        self.delibration_year_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delibration_year_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.delibration_year_spinbox.setMinimum(1600)
        self.delibration_year_spinbox.setMaximum(2500)
        self.delibration_year_spinbox.setValue(2000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.delibration_year_spinbox)

        self.degree_combobox = QComboBox(self.centralwidget)
        self.degree_combobox.addItem("")
        self.degree_combobox.addItem("")
        self.degree_combobox.addItem("")
        self.degree_combobox.setObjectName(u"degree_combobox")
        self.degree_combobox.setEditable(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.degree_combobox)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.note_input = QLineEdit(self.centralwidget)
        self.note_input.setObjectName(u"note_input")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.note_input)


        self.horizontalLayout_2.addLayout(self.formLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.select_picture_button = QPushButton(self.centralwidget)
        self.select_picture_button.setObjectName(u"select_picture_button")

        self.horizontalLayout.addWidget(self.select_picture_button)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout.addWidget(self.reset_button)

        self.register_button = QPushButton(self.centralwidget)
        self.register_button.setObjectName(u"register_button")

        self.horizontalLayout.addWidget(self.register_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(1, 1)
        StudentRegisterInfo.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StudentRegisterInfo)
        self.statusbar.setObjectName(u"statusbar")
        StudentRegisterInfo.setStatusBar(self.statusbar)

        self.retranslateUi(StudentRegisterInfo)

        QMetaObject.connectSlotsByName(StudentRegisterInfo)
    # setupUi

    def retranslateUi(self, StudentRegisterInfo):
        StudentRegisterInfo.setWindowTitle(QCoreApplication.translate("StudentRegisterInfo", u"MainWindow", None))
        self.student_picture.setText(QCoreApplication.translate("StudentRegisterInfo", u"Profile", None))
        self.label_2.setText(QCoreApplication.translate("StudentRegisterInfo", u"Name", None))
        self.name_input.setText("")
        self.label_3.setText(QCoreApplication.translate("StudentRegisterInfo", u"Birthday", None))
        self.birthday_input.setDisplayFormat(QCoreApplication.translate("StudentRegisterInfo", u"dd/MM/yyyy", None))
        self.label_4.setText(QCoreApplication.translate("StudentRegisterInfo", u"Place of birth", None))
        self.birth_place_input.setText("")
        self.label_6.setText(QCoreApplication.translate("StudentRegisterInfo", u"University", None))
        self.university_input.setText("")
        self.label_5.setText(QCoreApplication.translate("StudentRegisterInfo", u"Speciality", None))
        self.speciality_input.setText("")
        self.label_7.setText(QCoreApplication.translate("StudentRegisterInfo", u"Domain", None))
        self.domain_input.setText("")
        self.label_8.setText(QCoreApplication.translate("StudentRegisterInfo", u"Sector", None))
        self.sector_input.setText("")
        self.label_9.setText(QCoreApplication.translate("StudentRegisterInfo", u"Department", None))
        self.departement_input.setText("")
        self.label_10.setText(QCoreApplication.translate("StudentRegisterInfo", u"Degree", None))
        self.label_11.setText(QCoreApplication.translate("StudentRegisterInfo", u"Year Prepare", None))
        self.label_12.setText(QCoreApplication.translate("StudentRegisterInfo", u"Year Registration", None))
        self.label_13.setText(QCoreApplication.translate("StudentRegisterInfo", u"Date Deliberation", None))
        self.degree_combobox.setItemText(0, QCoreApplication.translate("StudentRegisterInfo", u"Select Degree", None))
        self.degree_combobox.setItemText(1, QCoreApplication.translate("StudentRegisterInfo", u"Bachelor", None))
        self.degree_combobox.setItemText(2, QCoreApplication.translate("StudentRegisterInfo", u"Master", None))

        self.label_14.setText(QCoreApplication.translate("StudentRegisterInfo", u"Note", None))
        self.note_input.setText("")
        self.select_picture_button.setText(QCoreApplication.translate("StudentRegisterInfo", u"Select Image", None))
        self.reset_button.setText(QCoreApplication.translate("StudentRegisterInfo", u"Reset", None))
        self.register_button.setText(QCoreApplication.translate("StudentRegisterInfo", u"Register", None))
    # retranslateUi

