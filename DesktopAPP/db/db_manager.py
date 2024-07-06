import sqlite3 as sq
import os

class DbManager:
	 
	def __init__ (self, db_path='./student.db'):
		if not os.path.isfile(db_path):
			open(db_path ,'w').close()
		self.connection = sq.connect(db_path)
		self.create_student_table()
	
	def create_student_table (self):
		with self.connection:
			self.connection.execute(
								"""
								CREATE TABLE IF NOT EXISTS student (
									Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
									Name TEXT NOT NULL UNIQUE,
									Birthday TEXT NOT NULL UNIQUE,
									Birth_Place TEXT NOT NULL UNIQUE,
									University TEXT NOT NULL UNIQUE,
									Speciality TEXT NOT NULL UNIQUE,
									Domain TEXT NOT NULL UNIQUE,
									Sector TEXT NOT NULL UNIQUE,
									Department TEXT NOT NULL UNIQUE,
									Degree TEXT NOT NULL UNIQUE,
									Preparation_Year TEXT NOT NULL UNIQUE,
									Registration_Year TEXT NOT NULL UNIQUE,
									Deliberation_Date TEXT NOT NULL UNIQUE,
									Note TEXT NOT NULL UNIQUE,
								);
								"""
						   )
			self.connection.commit()

	def add_student(self, info:dict[str:str]):
		pass

	def delete_student(self, student_id):
		pass
	
	def modify_student(self, student_id, info:dict[str:str]):
		pass