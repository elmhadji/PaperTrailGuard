from PySide6.QtWidgets import QWidget
from .card_student_info_ui import Ui_CardStudentInfo

class CardStudentInfo(Ui_CardStudentInfo ,QWidget):
	
	def __init__(self, name:str, birthday:str, birth_place:str, degree_type:str):
		super(CardStudentInfo, self).__init__()
		self.setupUi(self)
		self.load_card_info(name, birthday ,birth_place, degree_type)

	def load_card_info(self, name:str, birthday:str, birth_place:str, degree_type:str):
		pass