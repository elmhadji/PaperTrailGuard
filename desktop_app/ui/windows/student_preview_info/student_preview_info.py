from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Qt, QDate
from PySide6.QtGui import QPixmap
from .student_preview_info_ui import Ui_StudentPreviewInfo
from db.db_manager import DbManager

class StudentPreviewInfo(QMainWindow, Ui_StudentPreviewInfo):
	window_closed = Signal()

	def __init__(self, student_info:dict[str,str]):
		super().__init__()
		self.student_info = student_info
		self.setupUi(self)
		self.load_student_info()

	def load_student_info(self):
		self.name_input.setText(self.student_info["name"])
		self.birthday_input.setDate(QDate.fromString(self.student_info["birthday"], 'dd_MM_yyyy'))
		self.birth_place_input.setText(self.student_info["birth_place"])
		self.university_input.setText(self.student_info["university"])
		self.speciality_input.setText(self.student_info["speciality"])
		self.domain_input.setText(self.student_info["domain"])
		self.sector_input.setText(self.student_info["sector"])
		self.departement_input.setText(self.student_info["department"])
		self.degree.setText(self.student_info["degree"])
		self.preparation_year_spinbox.setValue(int(self.student_info["preparation_year"]))
		self.registration_year_spinbox.setValue(int(self.student_info["registration_year"]))
		self.delibration_year_spinbox.setValue(int(self.student_info["deliberation_date"]))
		self.note_input.setText(self.student_info["note"])
		profile_picture = DbManager().get_student_profile_path(self.student_info['name'], self.student_info['birthday'])
		pixmap = QPixmap(profile_picture)
		self.student_picture.setPixmap(pixmap.scaled(200, 250, Qt.AspectRatioMode.KeepAspectRatio))

	def closeEvent(self ,event):
		self.window_closed.emit()
		event.accept()