from PySide6.QtWidgets import QMainWindow ,QWidget
from .restore_password_ui import Ui_ForgetPassowrd

class RestorePassword( Ui_ForgetPassowrd ,QMainWindow):
	def __init__(self):
		super(RestorePassword ,self).__init__()
		self.setupUi(self)
		self.login_window = None
		self.return_button.clicked.connect(self.return_to_login)
		self.show()
	
	def return_to_login (self):
		from ..login.login import Login
		if self.login_window is None:
			self.login_window = Login()
			self.close()
