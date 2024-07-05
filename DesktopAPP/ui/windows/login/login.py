from PySide6.QtWidgets import QMainWindow
from .login_ui import Ui_Login
from ...dialogs.alert import Alert

class Login (Ui_Login ,QMainWindow):
	def __init__(self):
		super(Login ,self).__init__()
		self.setupUi(self)
		self.forget_password_link.clicked.connect(self.redirection)
		self.login_button.clicked.connect(self.login)
		self.show()

	def login(self):
		username = self.username_input.text()
		password = self.password_input.text()
		if username != 'admin' or password != 'admin':
			Alert("Unknown Info", "The username or password are incorrect")

	def redirection(self):
		pass