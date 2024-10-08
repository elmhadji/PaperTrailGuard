import sqlite3 as sq
import shutil
import os


class DbManager:
	 
	def __init__ (self, db_path='desktop_app/db/student.db', picture_directory='desktop_app/db/student_images'):
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
			shutil.copy2(picture_path, destination_path)

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
		old_name, old_birthday = student[1], student[2]

		set_clause = ", ".join([f"{key} = ?" for key in info.keys() if key != 'picture_path'])
		sql_query = f"UPDATE student SET {set_clause} WHERE student_id = ?"
		parameters = [info[key] for key in info.keys() if key != 'picture_path'] + [student_id]
		connection = sq.connect(self.db_path)
		with connection:
			connection.execute(sql_query, parameters)
			connection.commit()

		new_name = info.get('name', old_name)
		new_birthday = info.get('birthday', old_birthday)
		# Update picture name if student info updated
		if new_name != old_name or new_birthday != old_birthday:
			old_picture_filename = f"{old_name.replace(' ', '_')}_{old_birthday}.jpg"
			new_picture_filename = f"{new_name.replace(' ', '_')}_{new_birthday}.jpg"
			old_picture_path = os.path.join(self.picture_directory, old_picture_filename)
			new_picture_path = os.path.join(self.picture_directory, new_picture_filename)

			if os.path.exists(old_picture_path):
				os.rename(old_picture_path, new_picture_path)
		# Update picture if student add new one
		picture_path = info.get('picture_path')
		if picture_path:
			old_picture_filename = f"{old_name.replace(' ', '_')}_{old_birthday}.jpg"
			old_picture_path = os.path.join(self.picture_directory, old_picture_filename)

			if os.path.exists(old_picture_path):
				os.remove(old_picture_path)
			
			new_picture_filename = f"{new_name.replace(' ', '_')}_{new_birthday}.jpg"
			new_picture_path = os.path.join(self.picture_directory, new_picture_filename)
			shutil.copy2(picture_path, new_picture_path)

	def get_student_by_id(self, student_id: int) -> tuple[int, str] | None:
		"""
		Retrieve a student record from the database by their ID.

		Parameters:
		student_id (int): The unique ID of the student to retrieve.

		Returns:
		tuple: A tuple containing the student's information.
		
		Example:[
					0:student_id, \\
					1:'name', \\
					2:'birthday', \\
					3:'birth_place',\\
					4:'university' ,\\
					5:'speciality' ,\\
					6:'domain' ,\\
					7:'sector' ,\\
					8:'department' ,\\
					9:'degree' ,\\
					10:'preparation_year' ,\\
					11:'registration_year' ,\\
					12:'deliberation_date' ,\\
					13:'note'\\
				]
		"""
		student = None
		sql_query = "SELECT * FROM student WHERE Student_ID = ?"
		connection = sq.connect(self.db_path)
		with connection:
			cursor = connection.execute(sql_query, (student_id,))
			student = cursor.fetchone()
		return student
	
	def get_all_students(self) -> list[dict[str, str]]:
		"""
		Retrieve all student records from the database.

		Returns:
			student_list (list[dict[str, str]]): A list of dictionaries, each containing a student's information, or Empty list if no students are found
		"""
		sql_query = "SELECT * FROM student"
		connection = sq.connect(self.db_path)
		with connection:
			cursor = connection.execute(sql_query)
			students = cursor.fetchall()

		if students is None:
			return []

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
	
	def get_student_by_degree(self, degree: int) -> list[dict[str, str]]:
		"""
		Retrieve all student records from the database by their degree.

		Parameters:
			degree (int): The degree index of the students to retrieve.

		Returns :
			Filtred list of dictionaries by degree, each containing a student's information, or Empty list if no students are found.
		"""
		match degree:
			case 1:
				degree = "Bachelor"
			case 2:
				degree = "Master"
			case _ :
				return []

		sql_query = "SELECT * FROM student WHERE degree = ?"
		connection = sq.connect(self.db_path)
		with connection:
			cursor = connection.execute(sql_query, (degree,))
			students = cursor.fetchall()

		if students is None:
			return []

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

	def get_student_by_name_and_degree(self, name: str, degree_index: int) -> list[dict[str, str]]:
		"""
		Retrieve all student records from the database by their name and degree.

		Parameters:
			name (str): The name of the students to retrieve.
			degree_index (int): The index of the degree (0 for All, 1 for Bachelor, 2 for Master).

		Returns :
			Filtred list of dictionaries by name and degree, each containing a student's information, or Empty list if no students are found.
		"""
		if degree_index == 0:
			# All degrees
			sql_query = "SELECT * FROM student WHERE name LIKE ?"
		elif degree_index == 1:
			# Bachelor degree
			sql_query = "SELECT * FROM student WHERE name LIKE ? AND degree = 'Bachelor'"
		elif degree_index == 2:
			# Master degree
			sql_query = "SELECT * FROM student WHERE name LIKE ? AND degree = 'Master'"
		else:
			raise ValueError("Invalid degree index. Must be 0, 1, or 2.")

		connection = sq.connect(self.db_path)
		with connection:
			cursor = connection.execute(sql_query, (f"%{name}%",))
			students = cursor.fetchall()

		if students is None:
			return []

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
	
	def get_student_profile_path(self, student_name:str, student_birthday:str) ->str:
		"""
		Parameters :
			student_name (str) : student name
			student_birthday (str): student birthday in format (dd_MM_yyyy)
		Returns:
			picture_path ):profile picture path for the student
		"""
		picture_filename = f"{student_name.replace(' ', '_')}_{student_birthday}.jpg"
		picture_path = os.path.join(self.picture_directory, picture_filename)
		return picture_path
