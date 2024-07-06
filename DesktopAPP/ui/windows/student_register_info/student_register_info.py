from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal
from .student_register_info_ui import Ui_StudentRegisterInfo

class StudentRegisterInfo(Ui_StudentRegisterInfo, QMainWindow):
	window_closed = Signal()

	def __init__(self ,student_info:dict[str:str]=None):
		super(Ui_StudentRegisterInfo, self).__init__()
		self.setupUi(self)
		self.register_button.clicked.connect(self.register_student)
		self.reset_button.clicked.connect(self.reset_window)
		self.select_picture_button.clicked.connect(self.select_student_picture)
		self.show()

	def closeEvent(self ,event):
		self.window_closed.emit()
		event.accept()
	
	def register_student(self):
		#TODO: Register student
		self.window_closed.emit()
		self.close()
	
	def reset_window(self):
		pass

	def select_student_picture(self):
		pass