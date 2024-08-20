from PySide6.QtWidgets import QWidget ,QDialog, QMessageBox
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from .card_student_info_ui import Ui_CardStudentInfo
from db.db_manager import DbManager
from fpdf import FPDF
import arabic_reshaper
from bidi import get_display
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import subprocess
import qrcode
import os

class CardStudentInfo(Ui_CardStudentInfo ,QWidget):
	update_student_info = Signal(dict)
	update_student_list = Signal()
	show_student_preview_info = Signal(dict)

	def __init__(self, info:dict[str,str]):
		super(CardStudentInfo, self).__init__()
		self.info = info
		self.setupUi(self)
		self.load_card_info()
		self.delete_button.clicked.connect(self.delete_student_info)
		self.edit_button.clicked.connect(self.edit_student_info)
		self.print_pdf_button.clicked.connect(self.print_student_info)
		self.info_preview_button.clicked.connect(lambda: self.show_student_preview_info.emit(self.info))

	def load_card_info(self):
		self.name_label.setText(self.info['name'])
		self.birthday_label.setText(self.info['birthday'])
		self.birth_place_label.setText(self.info['birth_place'])
		self.degree_type_label.setText(self.info['degree'])
		profile_picture = DbManager().get_student_profile_path(self.info['name'], self.info['birthday'])
		pixmap = QPixmap(profile_picture)
		self.profile_image_label.setPixmap(pixmap.scaled(150, 170, Qt.AspectRatioMode.KeepAspectRatio))

	def edit_student_info(self):
		self.update_student_info.emit(self.info)

	def delete_student_info(self):
		dialog = QDialog()
		dialog.setWindowTitle("Confirm Deletion")

		message = QMessageBox(dialog)
		message.setIcon(QMessageBox.Icon.Question)
		message.setText(f"Are you sure you want to delete {self.info['name']}?")
		message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
		message.setDefaultButton(QMessageBox.StandardButton.No)

		result = message.exec_()
		if result == QMessageBox.StandardButton.Yes:
			database_manager = DbManager()
			database_manager.delete_student(int(self.info["student_id"]))
			self.update_student_list.emit()

	def print_student_info(self):
		info = f"""
جامعة مصطفى اسطمبولي بمعسكر بمقتضى:
-المرسوم التنفيذي رقم 08-265 المؤرخ في 19 أوت 2008 المتضمن نظام الدراسات للحصول على شهادة الليسانس و شهادة الماستر و شهادة الدكتوراه
-القرار رقم 576 المؤرخ في 5 أوت 2015 المتضمن مطابقة التكوينات في الليسانس المؤهلة بجامعة معسكر في ميدان "{self.info['domain']}"
-محضر جلسة المداولات بتاريخ {self.info['deliberation_date']}
بيشهد ان السيد(ة)/ الانسة: {self.info['name']}      المولود(ة) في: {self.info['birthday']}     ب: {self.info['birth_place']}
قد تحصل(ت) على شهادة: {self.info['degree']}
في ميدان: {self.info['domain']}
فرع: {self.info['sector']}
تخصص: {self.info['speciality']}
بكلية: {self.info['university']}
بمعسكر          تاريخ: {self.info['deliberation_date']}
عميد الكلية            مدير الجامعة
"""
		info_qr = f"""
Name:{self.info['name']}
Birthday: {self.info['birthday']}
Birth Place: {self.info['birth_place']}
Domain: {self.info['domain']}
Sector: {self.info['sector']}
Speciality: {self.info['speciality']}
			"""
		
		reshaped_text = arabic_reshaper.reshape(info)
		new_info = get_display(reshaped_text)
		pdf = FPDF(orientation='l', unit='mm', format="A4")
		pdf.add_page()
		pdf.set_xy(90, 10)
		pdf.image(name='desktop_app/assets/images/logo.png', link='', type='')
		pdf.set_xy(40, 0)
		pdf.add_font('DejaVu', '', 'desktop_app/assets/dejavu-sans/ttf/DejaVuSansCondensed.ttf', uni=True)
		pdf.set_font('DejaVu', '', 20)
		pdf.cell(w=210, h=130, align='C', txt=get_display(arabic_reshaper.reshape('شهادة نجاح')))
		pdf.set_xy(10, 60)
		pdf.set_font('DejaVu', '', 14)
		pdf.multi_cell(w=280, h=8, txt=new_info, border='', align='R')
		# encMessage ="B"+str(encMessage)
		encMessage = self.encrypt_text(info_qr)
		qr = qrcode.make(encMessage)
		qrcode_path = "desktop_app/assets/qrcode.png"
		qr.save(qrcode_path)
		pdf.set_xy(15, 135)
		pdf.image(name=qrcode_path,  w=50, h=50)
		if os.path.exists(qrcode_path):
			os.remove(qrcode_path)
		pdf_file_path = "desktop_app/assets/Diplom.pdf"
		pdf.output(pdf_file_path, 'F')
		try:
			subprocess.run(['open', pdf_file_path])  # macOS
		except FileNotFoundError:
			subprocess.run(['xdg-open', pdf_file_path])  # Linux

		

	def encrypt_text(self, data:str) -> str:
		"""
		Parameters:
		data: The text you want to encrypt\n
		Returns:
		An string that is the encrypted version of the data
		"""
		directory = 'desktop_app/assets'
		data = data.encode("utf-8")
		try:
			with open(os.path.join(directory, 'key.bin'), 'rb') as file:
				key = file.read()
		except FileNotFoundError:
			key = get_random_bytes(16)
			with open(os.path.join(directory, 'key.bin'), 'wb') as file:
				file.write(key)
		cipher = AES.new(key, AES.MODE_CBC)
		encrypted_data = b64encode(cipher.iv + cipher.encrypt(pad(data, AES.block_size)))
		return encrypted_data+b64encode(key)
