from PySide6.QtWidgets import QMainWindow, QListWidgetItem ,QAbstractItemView, QDialog, QMessageBox
from PySide6.QtCore import Slot
from .student_manager_ui import Ui_StudentManager
from db.db_manager import DbManager
from ui.widgets.card_student_info.card_student_info import CardStudentInfo

class StudentManager(Ui_StudentManager, QMainWindow):
	def __init__(self):
		super(StudentManager, self).__init__()
		self.setupUi(self)
		self.register_students_window = None
		self.student_card_info_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
		self.register_button.clicked.connect(lambda: self.show_regiter_student_window())
		self.search_button.clicked.connect(self.search_student)
		self.delete_selected_button.clicked.connect(self.delete_selected_student)
		self.refresh_button.clicked.connect(self.refresh_student_list)
		self.selected_all_checkBox.stateChanged.connect(self.select_all_student)
		self.degree_combo_box.currentIndexChanged.connect(lambda index: self.filter_student_by_degree(index))
		self.load_student_from_db()
		self.show()
	
	def load_student_from_db (self):
		self.student_card_info_list.clear()
		database_manager = DbManager()
		students_info = database_manager.get_all_students()
		if len(students_info) == 0:
			print('The DataBase is Empty!!!!')
			return 
		self.set_list_widget(students_info)
	
	def refresh_student_list (self):
		self.name_input.setText("")
		self.degree_combo_box.setCurrentIndex(0)
	
	def set_list_widget (self, students_info:list):
		#FIXME: This function is highly intensive for resource
		#FIXME: Try later to switch from QListWidget to QListView may solve issuse
		if len(students_info) == 0:
			return
		for student_info in students_info:
			student_card_info = CardStudentInfo(student_info)
			student_card_info.update_student_info.connect(self.show_regiter_student_window)
			student_card_info.update_student_list.connect(self.load_student_from_db)
			student_card_info.show_student_preview_info.connect(self.show_student_preview_info)
			itemList = QListWidgetItem(self.student_card_info_list)
			self.student_card_info_list.insertItem(0 ,itemList)
			itemList.setSizeHint(student_card_info.minimumSizeHint())
			self.student_card_info_list.setItemWidget(itemList , student_card_info)
	

	def search_student(self):
		name = self.name_input.text().strip()
		if name != "":
			degree_index = self.degree_combo_box.currentIndex()
			students = DbManager().get_student_by_name_and_degree(name, degree_index)
			self.student_card_info_list.clear()
			self.set_list_widget(students)
			
	def select_all_student(self):
		for item_index in range(self.student_card_info_list.count()):
			item = self.student_card_info_list.item(item_index)
			item.setSelected(True)

	def delete_selected_student(self):
		dialog = QDialog()
		dialog.setWindowTitle("Confirm Deletion")

		message = QMessageBox(dialog)
		message.setIcon(QMessageBox.Icon.Question)
		message.setText("Are you sure you want to delete all selected student?")
		message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
		message.setDefaultButton(QMessageBox.StandardButton.No)

		result = message.exec_()
		if result == QMessageBox.StandardButton.Yes:
			for item_index in range(self.student_card_info_list.count()):
				item = self.student_card_info_list.item(item_index)
				if item.isSelected():
					card_student_info:CardStudentInfo = self.student_card_info_list.itemWidget(item)
					DbManager().delete_student(int(card_student_info.info["student_id"]))
			self.load_student_from_db()

	def filter_student_by_degree(self ,degree:int = 0):
		name = self.name_input.text().strip()
		if name != "":
			return
		elif degree != 0:
			# GET STUDENT BY DEGREE
			students_info = DbManager().get_student_by_degree(degree)
			self.student_card_info_list.clear()
			self.set_list_widget(students_info)
		else:
			# GET ALL STUDENT
			self.load_student_from_db()
	
	@Slot(dict)
	def show_student_preview_info(self, student_info:dict[str,str]):
		from ..student_preview_info.student_preview_info import StudentPreviewInfo
		self.student_preview_info_window = StudentPreviewInfo(student_info)
		self.student_preview_info_window.show()

	@Slot(dict)
	def show_regiter_student_window (self, student_info:dict[str,str]=None):
		from ..student_register_info.student_register_info import StudentRegisterInfo
		if self.register_students_window is None:
			self.register_students_window = StudentRegisterInfo(student_info)
			self.register_students_window.window_closed.connect(self.register_students_window_closed)
			
	@Slot()
	def register_students_window_closed(self):
		self.register_students_window = None
		self.load_student_from_db()