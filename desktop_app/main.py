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

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myapp = Main()
	sys.exit(app.exec())