from PySide6.QtWidgets import QMainWindow
from .login_ui import Ui_Login
from ..restore_password.restore_password import RestorePassword
from ..student_manager.student_manager import StudentManager

class Login (Ui_Login ,QMainWindow):
	
	def __init__(self):
		super(Login ,self).__init__()
		self.setupUi(self)
		self.restore_password_window = None
		self.student_manager_window = None
		self.forget_password_link.clicked.connect(self.redirection)
		self.login_button.clicked.connect(self.login)
		self.show()

	def login(self):
		username = self.username_input.text()
		password = self.password_input.text()
		if username != 'admin' or password != 'admin':
			from ...dialogs.alert import Alert
			Alert("Unknown Info", "The username or password are incorrect")
			return
		if self.student_manager_window is None:
			self.student_manager_window = StudentManager()
			self.close()

	def redirection(self):
		if self.restore_password_window is None:
			self.restore_password_window = RestorePassword()
			self.close()