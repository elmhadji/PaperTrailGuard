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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_StudentPreviewInfo(object):
    def setupUi(self, StudentPreviewInfo):
        if not StudentPreviewInfo.objectName():
            StudentPreviewInfo.setObjectName(u"StudentPreviewInfo")
        StudentPreviewInfo.resize(846, 454)
        self.centralwidget = QWidget(StudentPreviewInfo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dateEdit)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout.addLayout(self.formLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_7)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_5)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_12)


        self.horizontalLayout.addLayout(self.formLayout_2)

        StudentPreviewInfo.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StudentPreviewInfo)
        self.statusbar.setObjectName(u"statusbar")
        StudentPreviewInfo.setStatusBar(self.statusbar)

        self.retranslateUi(StudentPreviewInfo)

        QMetaObject.connectSlotsByName(StudentPreviewInfo)
    # setupUi

    def retranslateUi(self, StudentPreviewInfo):
        StudentPreviewInfo.setWindowTitle(QCoreApplication.translate("StudentPreviewInfo", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("StudentPreviewInfo", u"Profile", None))
        self.label_2.setText(QCoreApplication.translate("StudentPreviewInfo", u"Name", None))
        self.lineEdit.setText(QCoreApplication.translate("StudentPreviewInfo", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("StudentPreviewInfo", u"Birthday", None))
        self.label_4.setText(QCoreApplication.translate("StudentPreviewInfo", u"Place of birth", None))
        self.lineEdit_2.setText("")
        self.label_6.setText(QCoreApplication.translate("StudentPreviewInfo", u"University", None))
        self.lineEdit_4.setText("")
        self.label_5.setText(QCoreApplication.translate("StudentPreviewInfo", u"Speciality", None))
        self.lineEdit_3.setText("")
        self.label_7.setText(QCoreApplication.translate("StudentPreviewInfo", u"Domain", None))
        self.label_8.setText(QCoreApplication.translate("StudentPreviewInfo", u"Sector", None))
        self.lineEdit_6.setText("")
        self.label_9.setText(QCoreApplication.translate("StudentPreviewInfo", u"Department", None))
        self.lineEdit_7.setText("")
        self.lineEdit_5.setText("")
        self.label_10.setText(QCoreApplication.translate("StudentPreviewInfo", u"Degree", None))
        self.lineEdit_8.setText("")
        self.label_11.setText(QCoreApplication.translate("StudentPreviewInfo", u"Year Prepare", None))
        self.lineEdit_9.setText("")
        self.label_12.setText(QCoreApplication.translate("StudentPreviewInfo", u"Year Registration", None))
        self.lineEdit_10.setText("")
        self.label_13.setText(QCoreApplication.translate("StudentPreviewInfo", u"Date Deliberation", None))
        self.lineEdit_11.setText("")
        self.label_14.setText(QCoreApplication.translate("StudentPreviewInfo", u"Note", None))
        self.lineEdit_12.setText("")
    # retranslateUi

