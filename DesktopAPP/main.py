from PySide6.QtWidgets import QMainWindow ,QApplication
from ui.windows.login.login import Login
import sys

class Main(Login, QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myapp = Main()
	sys.exit(app.exec())