from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from .student_manager_ui import Ui_StudentManager

class StudentManager(Ui_StudentManager, QMainWindow):
	def __init__(self):
		super(StudentManager, self).__init__()
		self.setupUi(self)
		self.register_students_window = None
		self.register_button.clicked.connect(self.show_regiter_student_window)
		self.search_button.clicked.connect(self.search_student)
		self.delete_selected_button.clicked.connect(self.search_selected_student)
		# self.selected_all_checkBox.checkStateChanged.connect()
	
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

	def search_selected_student(self):
		pass
	
	def show_regiter_student_window (self):
		from ..student_register_info.student_register_info import StudentRegisterInfo
		if self.register_students_window is None:
			self.register_students_window = StudentRegisterInfo()
			self.register_students_window.window_closed.connect(self.register_students_window_closed)

	@Slot()
	def register_students_window_closed(self):
		self.register_students_window = None