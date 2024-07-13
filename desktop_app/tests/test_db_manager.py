import pytest
import shutil
import os
from ..db.db_manager import DbManager

# Fixture for setting up the database and manager instance
@pytest.fixture(scope="module")
def db_setup():
    db_path = './test_student.db'
    picture_directory = './test_student_images'
    db_manager = DbManager(db_path=db_path, picture_directory=picture_directory)
    
    yield db_manager  # This is where the test function will run
    
    # Cleanup code here will run after the test function completes
    if os.path.exists(db_path):
        os.remove(db_path)
    if os.path.exists(picture_directory):
        shutil.rmtree(picture_directory)

def test_add_students(db_setup):
    test_data = [
        {
        'name': 'Alice Smith',
        'birthday': '1990-03-20',
        'birth_place': 'City B',
        'university': 'University Y',
        'speciality': 'Physics',
        'domain': 'Astrophysics',
        'sector': 'Science',
        'department': 'Physics',
        'degree': 'PhD',
        'preparation_year': '2010',
        'registration_year': '2011',
        'deliberation_date': '2015',
        'note': 'Top student',
        'picture_path': './test_images/alice.jpg'
        },
        {
        'name': 'Bob Johnson',
        'birthday': '1992-07-10',
        'birth_place': 'City C',
        'university': 'University Z',
        'speciality': 'Medicine',
        'domain': 'Neurology',
        'sector': 'Health',
        'department': 'Medicine',
        'degree': 'MD',
        'preparation_year': '2012',
        'registration_year': '2013',
        'deliberation_date': '2017',
        'note': 'Dedicated student',
        'picture_path': './test_images/bob.jpg'
        }
        ]
    for student_info in test_data:
        db_setup.add_student(student_info)
    

def test_get_all_students(db_setup):
    # Your test logic here
    students = db_setup.get_all_students()
    assert len(students) == 2, "Expected 2 students, but got {}.".format(len(students))
    assert students[0]['name'] == 'Alice Smith', "Name mismatch for the first student."
    assert students[0]['university'] == 'University Y', "University mismatch for the first student."

def test_modify_student(db_setup):
    # Your test logic here
    alice_id = 1  # Assuming this is Alice's ID
    modified_info = {'name': 'Alice Johnson', 'speciality': 'Astrophysics and Cosmology'}
    db_setup.modify_student(alice_id, modified_info)
    alice = db_setup.get_student_by_id(alice_id)
    assert alice[1] == 'Alice Johnson', "Name not updated correctly."
    assert alice[5] == 'Astrophysics and Cosmology', "Speciality not updated correctly."
