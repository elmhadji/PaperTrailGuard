from PySide6.QtWidgets import QMainWindow
from .student_manager_ui import Ui_StudentManager

class StudentManager(Ui_StudentManager, QMainWindow):
	def __init__(self):
		super(StudentManager, self).__init__()
		self.setupUi(self)
		self.register_button.clicked.connect()
		self.search_button.clicked.connect()
		self.delete_selected_button.clicked.connect()
		self.selected_all_checkBox.checkStateChanged.connect()
	
		self.show()
	
	def load_student_from_db (self):
		#TODO: Load studetn from db 
		# Create card foe each
		# Load there info 
		pass

	def register_student(self):
		pass

	def search_student(self):
		pass

	def delete_student(self):
		pass