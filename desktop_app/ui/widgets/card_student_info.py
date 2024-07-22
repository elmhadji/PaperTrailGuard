from PySide6.QtWidgets import QWidget ,QDialog, QMessageBox
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from .card_student_info_ui import Ui_CardStudentInfo
from db.db_manager import DbManager

class CardStudentInfo(Ui_CardStudentInfo ,QWidget):
	update_student_info = Signal(dict)
	update_student_list = Signal()	

	def __init__(self, info:dict[str,str]):
		super(CardStudentInfo, self).__init__()
		self.info = info
		self.setupUi(self)
		self.load_card_info()
		self.delete_button.clicked.connect(self.delete_student_info)
		self.edit_button.clicked.connect(self.edit_student_info)
		self.print_pdf_button.clicked.connect(self.print_student_info)

	def load_card_info(self):
		self.name_label.setText(self.info['name'])
		self.birthday_label.setText(self.info['birthday'])
		self.birth_place_label.setText(self.info['birth_place'])
		self.degree_type_label.setText(self.info['degree'])
		profile_picture = DbManager().get_student_profile_path(self.info['name'], self.info['birthday'])
		pixmap = QPixmap(profile_picture)
		self.profile_image_label.setPixmap(pixmap.scaled(200, 250, Qt.AspectRatioMode.KeepAspectRatio))

	
	def edit_student_info(self):
		self.update_student_info.emit(self.info)

	def delete_student_info(self):
		dialog = QDialog()
		dialog.setWindowTitle("Confirm Deletion")

		message = QMessageBox(dialog)
		message.setIcon(QMessageBox.Icon.Question)
		message.setText(f"Are you sure you want to delete {self.info['name']}?")
		message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
		message.setDefaultButton(QMessageBox.StandardButton.No)

		result = message.exec_()
		if result == QMessageBox.StandardButton.Yes:
			database_manager = DbManager()
			database_manager.delete_student(int(self.info["student_id"]))
			self.update_student_list.emit()

	def print_student_info(self):
		pass
