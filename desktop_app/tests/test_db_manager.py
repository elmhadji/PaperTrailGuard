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

    students = db_setup.get_all_students()
    assert len(students) == 2, f"Expected 2 students, but got {len(students)}"
    assert students[0]['name'] == 'Alice Smith', "Name mismatch for the first student."
    assert students[0]['university'] == 'University Y', "University mismatch for the first student."

def test_modify_student_with_no_picture(db_setup):
    # Your test logic here
    student_id = 1  # Assuming this is Alice's ID
    modified_info = {'name': 'Alice Johnson', 'speciality': 'Astrophysics and Cosmology'}
    db_setup.modify_student(student_id, modified_info)
    alice = db_setup.get_student_by_id(student_id)
    assert alice[1] == 'Alice Johnson', "Name not updated correctly."
    assert alice[5] == 'Astrophysics and Cosmology', "Speciality not updated correctly."

def test_modify_student_with_picture(db_setup):
    # Your test logic here
    student_id = 1  # Assuming this is Alice's ID
    student_info = db_setup.get_student_by_id(student_id)
    student_name = student_info[1].replace(' ', '_')
    student_birthday = student_info[2]
    student_picture_path = f'{db_setup.picture_directory}/{student_name}_{student_birthday}.jpg'
    prev_time = os.stat(student_picture_path).st_ctime
    modified_info = {'name': 'Johnson', 'speciality': 'Informatics','picture_path': "/home/abdelhake/Pictures/Wallpapers/SAVE_20231117_150231.jpg"}
    db_setup.modify_student(student_id, modified_info)
    alice = db_setup.get_student_by_id(student_id)
    student_info = db_setup.get_student_by_id(student_id)
    student_name = student_info[1].replace(' ', '_')
    student_birthday = student_info[2]
    student_picture_path = f'{db_setup.picture_directory}/{student_name}_{student_birthday}.jpg'
    current_time = os.stat(student_picture_path).st_ctime
    assert alice[1] == 'Johnson', "Name not updated correctly."
    assert alice[5] == 'Informatics', "Speciality not updated correctly."
    assert prev_time != current_time, "Picture wasn't updated "

def test_delete_student(db_setup):
    student_id = 1
    student_info = db_setup.get_student_by_id(student_id)
    db_setup.delete_student(student_id)
    student_name = student_info[1].replace(' ', '_')
    student_birthday = student_info[2]
    student_picture_path = f'{db_setup.picture_directory}/{student_name}_{student_birthday}.jpg'
    picture_not_existe = True
    if os.path.exists(student_picture_path):
        picture_not_existe = False
    print(picture_not_existe)
    assert db_setup.get_student_by_id(student_id) is None , \
        f"Student didn't deleted Expected None but got {db_setup.get_student_by_id(student_id)}"
    assert picture_not_existe, "Image wasn't deleted successfully!" 

    
    

