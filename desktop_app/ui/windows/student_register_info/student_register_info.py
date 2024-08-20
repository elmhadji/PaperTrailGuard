from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Signal, QDate, QStandardPaths
from PySide6.QtGui import QPixmap, Qt
from .student_register_info_ui import Ui_StudentRegisterInfo
from ui.dialogs.alert import Alert 
from db.db_manager import DbManager

class StudentRegisterInfo(Ui_StudentRegisterInfo, QMainWindow):
	window_closed = Signal()

	def __init__(self ,student_info:dict[str:str]=None):
		super(Ui_StudentRegisterInfo, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("Register Student")
		
		self.preparation_year_spinbox.setValue(QDate().year())
		self.registration_year_spinbox.setValue(QDate().year())
		self.delibration_year_spinbox.setValue(QDate().year())
		self.picture_path = None
		self.student_info = student_info
		self.register_button.clicked.connect(self.register_student)
		self.reset_button.clicked.connect(self.reset_window)
		self.select_picture_button.clicked.connect(self.select_student_picture)
		if self.student_info is not None:
			self.register_button.clicked.disconnect(self.register_student)
			self.register_button.clicked.connect(self.edit_student_info)
			self.setWindowTitle("Update Student Info")
			self.register_button.setText("Update")
			self.load_student_info()
		self.show()

	def closeEvent(self ,event):
		self.window_closed.emit()
		event.accept()

	
	def check_fields(self) -> bool:
		"""
		check all fields
		Return:
		return true value if all required field have valide values false if not
		"""
		if self.name_input.text().strip() == "":
			Alert("All Field Required", "Name field cannot be empty")
			return False
		# 6205 days = 17 years
		if self.birthday_input.date().daysTo(QDate().currentDate()) <= 6205:
			Alert("All Field Required", "Birthday field cannot be a weird value")
			return False
		
		if self.birth_place_input.text().strip() == "":
			Alert("All Field Required", "Birth Place field cannot be empty")
			return False
		
		if self.university_input.text().strip() == "":
			Alert("All Field Required", "University field cannot be empty")
			return False
		
		if self.speciality_input.text().strip() == "":
			Alert("All Field Required", "Speciality field cannot be empty")
			return False
		
		if self.domain_input.text().strip() == "":
			Alert("All Field Required", "Domain field cannot be empty")
			return False
		
		if self.sector_input.text().strip() == "":
			Alert("All Field Required", "Sector field cannot be empty")
			return False
		
		if self.departement_input.text().strip() == "":
			Alert("All Field Required", "Departement field cannot be empty")
			return False
		
		if self.note_input.text().strip() == "":
			Alert("All Field Required", "Note field cannot be empty")
			return False
		
		if self.degree_combobox.currentIndex() == 0 :
			Alert("All Field Required", "Degree field cannot be empty")
			return False
		
		if self.picture_path is None:
			Alert("Picture Required", "Picture cannot be empty")
			return False
		
		return True
	
	def register_student(self):
		if self.check_fields():
		
			info = {
				'name':self.name_input.text(),
				'birthday':self.birthday_input.date().toString('dd_MM_yyyy'), 
				'birth_place':self.birth_place_input.text(), 
				'university':self.university_input.text(), 
				'speciality':self.speciality_input.text(),
				'domain':self.domain_input.text(), 
				'sector':self.sector_input.text(), 
				'department':self.departement_input.text(), 
				'degree':self.degree_combobox.currentText(), 
				'preparation_year':self.preparation_year_spinbox.value(),
				'registration_year':self.registration_year_spinbox.value(), 
				'deliberation_date':self.delibration_year_spinbox.value(), 
				'note':self.note_input.text(), 
				'picture_path':self.picture_path,
			}
			database_manager = DbManager()
			database_manager.add_student(info)
			self.close()

	def edit_student_info(self):
		if self.check_fields():
			database_manager = DbManager()
			info = {
				'name':self.name_input.text(),
				'birthday':self.birthday_input.date().toString('dd_MM_yyyy'), 
				'birth_place':self.birth_place_input.text(), 
				'university':self.university_input.text(), 
				'speciality':self.speciality_input.text(),
				'domain':self.domain_input.text(), 
				'sector':self.sector_input.text(), 
				'department':self.departement_input.text(), 
				'degree':self.degree_combobox.currentText(), 
				'preparation_year':self.preparation_year_spinbox.value(),
				'registration_year':self.registration_year_spinbox.value(), 
				'deliberation_date':self.delibration_year_spinbox.value(), 
				'note':self.note_input.text(), 
				'picture_path':self.picture_path,
			}
			database_manager.modify_student(int(self.student_info["student_id"]), info)
			self.close()

	def reset_window(self):
		self.name_input.setText("")
		self.birthday_input.setDate(QDate().currentDate())
		self.birth_place_input.setText("")
		self.university_input.setText("")
		self.speciality_input.setText("")
		self.domain_input.setText("")
		self.sector_input.setText("")
		self.departement_input.setText("")
		self.degree_combobox.setCurrentIndex(0)
		self.preparation_year_spinbox.setValue(QDate().year())
		self.registration_year_spinbox.setValue(QDate().year())
		self.delibration_year_spinbox.setValue(QDate().year())
		self.note_input.setText("")
		self.picture_path = None
		pixmap = QPixmap("desktop_app/assets/images/default_profile.png")
		self.student_picture.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))

	def select_student_picture(self):
		file_path = QFileDialog.getOpenFileName(
			self,
			caption='Select Person Pictures',
			dir=QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation),
			filter='Images (*.png *.xpm *.jpg *.jpeg)'
		)
		if file_path:
			self.picture_path = file_path[0]
			if self.student_info is not None:
				self.student_info['picture_path'] = self.picture_path
			pixmap = QPixmap(self.picture_path)
			self.student_picture.setPixmap(pixmap.scaled(200, 250, Qt.AspectRatioMode.KeepAspectRatio))

	def load_student_info(self):
		self.name_input.setText(self.student_info["name"])
		self.birthday_input.setDate(QDate.fromString(self.student_info["birthday"], 'dd_MM_yyyy'))
		self.birth_place_input.setText(self.student_info["birth_place"])
		self.university_input.setText(self.student_info["university"])
		self.speciality_input.setText(self.student_info["speciality"])
		self.domain_input.setText(self.student_info["domain"])
		self.sector_input.setText(self.student_info["sector"])
		self.departement_input.setText(self.student_info["department"])
		if self.student_info["degree"] == "Bachelor":
			self.degree_combobox.setCurrentIndex(1)
		elif self.student_info["degree"] == "Master":
			self.degree_combobox.setCurrentIndex(2)
		self.preparation_year_spinbox.setValue(int(self.student_info["preparation_year"]))
		self.registration_year_spinbox.setValue(int(self.student_info["registration_year"]))
		self.delibration_year_spinbox.setValue(int(self.student_info["deliberation_date"]))
		self.note_input.setText(self.student_info["note"])
		profile_picture = DbManager().get_student_profile_path(self.student_info['name'], self.student_info['birthday'])
		pixmap = QPixmap(profile_picture)
		self.student_picture.setPixmap(pixmap.scaled(200, 250, Qt.AspectRatioMode.KeepAspectRatio))
		