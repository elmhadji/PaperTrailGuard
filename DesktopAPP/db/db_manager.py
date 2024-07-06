import sqlite3 as sq
import os

class DbManager:
	 
	def __init__ (self, db_path='./student.db'):
		if not os.path.isfile(db_path):
			open(db_path ,'w').close()
		self.connection = sq.connect(db_path)
	
	def create_student_table (self):
		pass

	def add_student(self, info:dict[str:str]):
		pass

	def delete_student(self, student_id):
		pass
	
	def modify_student(self, info:dict[str:str]):
		pass