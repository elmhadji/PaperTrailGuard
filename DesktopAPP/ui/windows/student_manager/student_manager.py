from PySide6.QtWidgets import QMainWindow
from .student_manager_ui import Ui_StudentManager

class StudentManager(Ui_StudentManager, QMainWindow):
	def __init__(self):
		super(StudentManager, self).__init__()
		self.setupUi(self)
		self.show()