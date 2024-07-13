import sqlite3 as sq
import shutil
import os

class DbManager:
	 
	def __init__ (self, db_path='./student.db', picture_directory='./student_images'):
		if not os.path.isfile(db_path):
			open(db_path ,'w').close()
		self.picture_directory = picture_directory
		self.db_path = db_path
		os.makedirs(picture_directory, exist_ok=True)
		self.create_student_table()
	
	def create_student_table (self):
		connection = sq.connect(self.db_path)
		with connection:
			connection.execute(
								"""
								CREATE TABLE IF NOT EXISTS student (
									student_id INTEGER PRIMARY KEY AUTOINCREMENT,
									name TEXT NOT NULL UNIQUE,
									birthday TEXT NOT NULL ,
									birth_place TEXT NOT NULL ,
									university TEXT NOT NULL ,
									speciality TEXT NOT NULL ,
									domain TEXT NOT NULL ,
									sector TEXT NOT NULL ,
									department TEXT NOT NULL ,
									degree TEXT NOT NULL ,
									preparation_year TEXT NOT NULL ,
									registration_year TEXT NOT NULL ,
									deliberation_date TEXT NOT NULL ,
									note TEXT NOT NULL
								);
								"""
						   )
			connection.commit()

	def add_student(self, info: dict[str, str]) -> None:
		"""
		Save student information into the database associated with their picture.

		Parameters:
		info (dict[str, str]): A dictionary containing the student's information.
			The keys should include:
				'name', 'birthday', 'birth_place', 'university', 'speciality',
				'domain', 'sector', 'department', 'degree', 'preparation_year',
				'registration_year', 'deliberation_date', 'note', 'picture_path'
			and the values should be the corresponding details as strings.

		Returns:
		None: This function does not return anything.
		"""
		# Extracting information from the dictionary
		name = info.get('name')
		birthday = info.get('birthday')
		birth_place = info.get('birth_place')
		university = info.get('university')
		speciality = info.get('speciality')
		domain = info.get('domain')
		sector = info.get('sector')
		department = info.get('department')
		degree = info.get('degree')
		preparation_year = info.get('preparation_year')
		registration_year = info.get('registration_year')
		deliberation_date = info.get('deliberation_date')
		note = info.get('note')
		picture_path = info.get('picture_path')

		sql_query = """
		INSERT INTO student (name, birthday, birth_place, university, speciality, domain, sector, 
							  department, degree, preparation_year, registration_year, deliberation_date, note)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
		"""
		parameters = (name, birthday, birth_place, university, speciality, domain, sector, department, 
					  degree, preparation_year, registration_year, deliberation_date, note)
		connection = sq.connect(self.db_path)
		with connection:
			connection.execute(sql_query, parameters)
			connection.commit()

		if picture_path:
			self.picture_directory
			os.makedirs(self.picture_directory, exist_ok=True)
			picture_filename = f"{name.replace(' ', '_')}_{birthday}.jpg"
			destination_path = os.path.join(self.picture_directory, picture_filename)
			shutil.copy(picture_path, destination_path)

	def delete_student(self, student_id: int) -> None:
		"""
		Delete a student record from the database and remove their picture.

		Parameters:
		student_id (int): The unique ID of the student to delete.

		Returns:
		None: This function does not return anything.
		"""
		student = self.get_student_by_id(student_id)
		if student:
			name, birthday = student[1], student[2]
			picture_filename = f"{name.replace(' ', '_')}_{birthday}.jpg"
			picture_path = os.path.join(self.picture_directory, picture_filename)
			
			if os.path.exists(picture_path):
				os.remove(picture_path)
			
			sql_query = "DELETE FROM student WHERE student_id = ?"
			connection = sq.connect(self.db_path)
			with connection:
				connection.execute(sql_query, (student_id,))
				connection.commit()
	
	def modify_student(self, student_id: int, info: dict[str, str]) -> None:
		"""
		Modify student information in the database.

		Parameters:
		student_id (int): The unique ID of the student to modify.
		info (dict[str, str]): A dictionary containing the updated student's information.
			The keys should include any of:
				'name', 'birthday', 'birth_place', 'university', 'speciality',
				'domain', 'sector', 'department', 'degree', 'preparation_year',
				'registration_year', 'deliberation_date', 'note', 'picture_path'

		Returns:
		None: This function does not return anything.
		"""
		student = self.get_student_by_id(student_id)
		if student is None:
			return

		set_clause = ", ".join([f"{key} = ?" for key in info.keys() if key != 'picture_path'])
		sql_query = f"UPDATE student SET {set_clause} WHERE student_id = ?"
		parameters = [info[key] for key in info.keys() if key != 'picture_path'] + [student_id]
		connection = sq.connect(self.db_path)
		with connection:
			connection.execute(sql_query, parameters)
			connection.commit()
		#TODO: Modify picture name
		picture_path = info.get('picture_path')
		if picture_path:
			old_name, old_birthday = student[1], student[2]
			old_picture_filename = f"{old_name.replace(' ', '_')}_{old_birthday}.jpg"
			old_picture_path = os.path.join(self.picture_directory, old_picture_filename)

			if os.path.exists(old_picture_path):
				os.remove(old_picture_path)
			
			new_picture_filename = f"{info['name'].replace(' ', '_')}_{info['birthday']}.jpg"
			new_picture_path = os.path.join(self.picture_directory, new_picture_filename)
			shutil.copy(picture_path, new_picture_path)

	def print_student_pdf(self, student_id: int) -> None:
		"""
		Generate a PDF containing the student's information.

		Parameters:
		student_id (int): The unique ID of the student to print.

		Returns:
		None: This function does not return anything.
		"""
		#TODO: Replace this function to the card_student_info widget
		# Placeholder for PDF generation logic
		# You can use libraries such as FPDF, ReportLab, or any other to generate PDFs.
		student = self.get_student_by_id(student_id)
		if student:
			# Add logic to create a PDF from student data
			pass

	def get_student_by_id(self, student_id: int) -> tuple[int, ...] | None:
		"""
		Retrieve a student record from the database by their ID.

		Parameters:
		student_id (int): The unique ID of the student to retrieve.

		Returns:
		tuple: A tuple containing the student's information.
		"""
		student = None
		sql_query = "SELECT * FROM student WHERE Student_ID = ?"
		connection = sq.connect(self.db_path)
		with connection:
			cursor = connection.execute(sql_query, (student_id,))
			student = cursor.fetchone()
		return student
	
	def get_all_students(self) -> list[dict[str, str]] | None:
		"""
		Retrieve all student records from the database.

		Returns:
		list[dict[str, str]] | None: A list of dictionaries, each containing a student's information,
									or None if no students are found.
		"""
		sql_query = "SELECT * FROM student"
		connection = sq.connect(self.db_path)
		with connection:
			cursor = connection.execute(sql_query)
			students = cursor.fetchall()

		if students is None:
			return None

		student_list = []
		for student in students:
			student_dict = {
				'student_id': student[0],
				'name': student[1],
				'birthday': student[2],
				'birth_place': student[3],
				'university': student[4],
				'speciality': student[5],
				'domain': student[6],
				'sector': student[7],
				'department': student[8],
				'degree': student[9],
				'preparation_year': student[10],
				'registration_year': student[11],
				'deliberation_date': student[12],
				'note': student[13]
			}
			student_list.append(student_dict)

		return student_list