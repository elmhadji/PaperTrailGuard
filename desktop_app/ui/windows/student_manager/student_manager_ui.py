# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_manager.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)
from . import student_manager_rc

class Ui_StudentManager(object):
    def setupUi(self, StudentManager):
        if not StudentManager.objectName():
            StudentManager.setObjectName(u"StudentManager")
        StudentManager.resize(767, 558)
        StudentManager.setStyleSheet(u"#StudentManager {\n"
"	font: 12pt \"Noto Sans\";\n"
"}\n"
"\n"
"#search_button, #register_button, #delete_selected_button, #refresh_button, QLineEdit{\n"
"	border: 1px solid  rgb(0, 94, 193);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"#degree_combo_box {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#search_button, #register_button, #delete_selected_button, #refresh_button {\n"
"	background-color: rgb(0, 94, 193);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#search_button::hover, #register_button::hover, #refresh_button::hover {\n"
"	background-color: #0066cc;\n"
"}\n"
"\n"
"#delete_selected_button::hover {\n"
"	background-color: red;\n"
"	border: 1px solid  red;\n"
"}\n"
"")
        self.centralwidget = QWidget(StudentManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.degree_combo_box = QComboBox(self.centralwidget)
        self.degree_combo_box.addItem("")
        self.degree_combo_box.addItem("")
        self.degree_combo_box.addItem("")
        self.degree_combo_box.setObjectName(u"degree_combo_box")

        self.horizontalLayout.addWidget(self.degree_combo_box)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")

        self.horizontalLayout.addWidget(self.name_input)

        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        icon = QIcon()
        icon.addFile(u":/Icons/assets/icons/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.search_button)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.register_button = QPushButton(self.centralwidget)
        self.register_button.setObjectName(u"register_button")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/assets/icons/user-plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.register_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.register_button)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.selected_all_checkBox = QCheckBox(self.centralwidget)
        self.selected_all_checkBox.setObjectName(u"selected_all_checkBox")
        self.selected_all_checkBox.setTristate(False)

        self.horizontalLayout_3.addWidget(self.selected_all_checkBox)

        self.delete_selected_button = QPushButton(self.centralwidget)
        self.delete_selected_button.setObjectName(u"delete_selected_button")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/assets/icons/trash-solid-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_selected_button.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.delete_selected_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.refresh_button = QPushButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/assets/icons/rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_button.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.refresh_button)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.student_card_info_list = QListWidget(self.frame)
        self.student_card_info_list.setObjectName(u"student_card_info_list")
        self.student_card_info_list.setAcceptDrops(False)
        self.student_card_info_list.setFrameShape(QFrame.Shape.StyledPanel)
        self.student_card_info_list.setFrameShadow(QFrame.Shadow.Sunken)
        self.student_card_info_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.student_card_info_list.setProperty("showDropIndicator", True)
        self.student_card_info_list.setDragEnabled(False)
        self.student_card_info_list.setDragDropOverwriteMode(False)
        self.student_card_info_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.student_card_info_list.setDefaultDropAction(Qt.DropAction.LinkAction)
        self.student_card_info_list.setAlternatingRowColors(False)
        self.student_card_info_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.student_card_info_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.student_card_info_list.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.student_card_info_list.setMovement(QListView.Movement.Snap)
        self.student_card_info_list.setFlow(QListView.Flow.LeftToRight)
        self.student_card_info_list.setProperty("isWrapping", True)
        self.student_card_info_list.setResizeMode(QListView.ResizeMode.Adjust)
        self.student_card_info_list.setLayoutMode(QListView.LayoutMode.Batched)
        self.student_card_info_list.setViewMode(QListView.ViewMode.ListMode)
        self.student_card_info_list.setWordWrap(True)
        self.student_card_info_list.setSelectionRectVisible(True)
        self.student_card_info_list.setItemAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.student_card_info_list, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)

        StudentManager.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StudentManager)
        self.statusbar.setObjectName(u"statusbar")
        StudentManager.setStatusBar(self.statusbar)

        self.retranslateUi(StudentManager)

        QMetaObject.connectSlotsByName(StudentManager)
    # setupUi

    def retranslateUi(self, StudentManager):
        StudentManager.setWindowTitle(QCoreApplication.translate("StudentManager", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("StudentManager", u"Degree", None))
        self.degree_combo_box.setItemText(0, QCoreApplication.translate("StudentManager", u"All", None))
        self.degree_combo_box.setItemText(1, QCoreApplication.translate("StudentManager", u"Bachelor", None))
        self.degree_combo_box.setItemText(2, QCoreApplication.translate("StudentManager", u"Master", None))

        self.label_2.setText(QCoreApplication.translate("StudentManager", u"Name", None))
        self.search_button.setText("")
        self.register_button.setText(QCoreApplication.translate("StudentManager", u"Register", None))
        self.selected_all_checkBox.setText("")
        self.delete_selected_button.setText(QCoreApplication.translate("StudentManager", u"Delete Selected", None))
        self.refresh_button.setText(QCoreApplication.translate("StudentManager", u"Refresh", None))
    # retranslateUi

