from PySide6.QtWidgets import QDialog
from .alert_ui import Ui_Alert

class Alert (Ui_Alert ,QDialog):
	def __init__(self, title:str ,message:str):
		super(Alert ,self).__init__()
		self.setupUi(self)
		self.load_alert_info(title ,message)
		self.buttonBox.accepted.connect(self.close)
		self.buttonBox.rejected.connect(self.close)
		self.exec()


	def load_alert_info(self, title:str, message:str):
		self.title.setText(title)
		self.message.setText(message)
