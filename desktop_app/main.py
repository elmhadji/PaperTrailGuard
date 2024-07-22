from PySide6.QtWidgets import QMainWindow ,QApplication
from ui.windows.login.login import Login
import sys

class Main(Login, QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		#TODO: Delete later 
		self.username_input.setText('admin')
		self.password_input.setText('admin')
		self.login()
		# for student_id in range(1, 20):
		# 	self.student_manager_window.show_regiter_student_window()
		# 	self.student_manager_window.register_students_window.name_input.setText(f"student_{str(student_id)}")
		# 	self.student_manager_window.register_students_window.birth_place_input.setText('geregr')
		# 	self.student_manager_window.register_students_window.university_input.setText('geregr') 
		# 	self.student_manager_window.register_students_window.speciality_input.setText('geregr')
		# 	self.student_manager_window.register_students_window.domain_input.setText('geregr')
		# 	self.student_manager_window.register_students_window.sector_input.setText('geregr') 
		# 	self.student_manager_window.register_students_window.departement_input.setText('geregr') 
		# 	self.student_manager_window.register_students_window.degree_combobox.setCurrentIndex(1), 
		# 	self.student_manager_window.register_students_window.note_input.setText('geregr') 
		# 	self.student_manager_window.register_students_window.picture_path = "desktop_app/tests/test_images/alice.jpg"
			
		# 	self.student_manager_window.register_students_window.register_student()
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myapp = Main()
	sys.exit(app.exec())