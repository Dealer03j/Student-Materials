import pytest
import System
import json

realUsername1 = 'akend3'
realPassword1 = '123454321'

realUsername2 = 'hdjsr7'
realPassword2 = 'pass1234'

realUsername3 = 'yted91'
realPassword3 = 'imoutofpasswordnames'


#Tests if the program can handle a wrong username
def test_login(grading_system):
    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.check_grades("comp_sci")

    if grades[1][1] == 99:
        assert True
    else:
        assert False

## not sure if I am too interpert this as if the passWord is ment to be non case sensitive
def test_check_password(grading_system):
    test = grading_system.check_password(realUsername2,realPassword2)
    test1 = grading_system.check_password(realUsername2,'Pass2345')

    if test == test1:
        assert False
    else:
        assert True

def test_change_grade(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.change_grade('akend3','databases','assignment1',24)

    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.check_grades("databases")
    print(grades)

    if grades[1][1] == 24:
        assert True
    else:
        assert False


def test_create_assignment(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.create_assignment('assignment3','1/3/4','databases')

    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.view_assignments("databases")

    if grades[0][0] == 'assignment3':
        assert True
    else:
        assert False

def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')

    grading_system.usr.add_student('yted91','databases')

    grading_system.login(realUsername3, realPassword3)
    grades = grading_system.usr.view_assignments("databases")

def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')

    grading_system.usr.add_student('yted91','databases')

    grading_system.login(realUsername3, realPassword3)
    grades = grading_system.usr.view_assignments("databases")

def test_submit_assignment(grading_system):
    grading_system.login(realUsername1, realPassword1)
    grading_system.usr.submit_assignment('databases',"assignment3","lkfsjdslfj","3/3/50")
    grades = grading_system.usr.view_assignments("databases")
    
    if grades[0][1] == '3/3/50':
        assert True
    else:
        assert False

def test_check_ontime(grading_system):
    grading_system.login(realUsername1, realPassword1)
    grading_system.usr.check_ontime("databases",'assignment1')

def test_check_grades(grading_system):
    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.check_grades("databases")
    print(grades)

    if grades[0][1] == 46:
        assert True
    else:
        assert False

def test_view_assignments(grading_system):
    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.view_assignments("databases")
    print(grades)

    if grades[0][1] == '2/10/20':
        assert True
    else:
        assert False


def test_view_assignments_forbadCalss(grading_system):
    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.view_assignments("databases")
    
    if grades[0][1] == '2/10/20':
        assert False

def test_create_assignment_unauthorized(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.create_assignment('assignmentbad','1/3/4','comp_sci')

    grading_system.login(realUsername1, realPassword1)
    grades = grading_system.usr.view_assignments("compsci")

    if grades[1][0] == 'assignmentbad':
        assert False

def test_change_grade_negative(grading_system):
    with pytest.raises(Exception):
        grading_system.login('goggins', 'augurrox')
        grading_system.usr.change_grade('akend3','databases','assignment1',-25)


def test_change_Too_long_usernmae(grading_system):
    with pytest.raises(Exception):
        grading_system.login('goggins', 'augurroxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

def test_view_nonExistentCourse(grading_system):
            with pytest.raises(Exception):
                grading_system.login(realUsername1, realPassword1)
                grades = grading_system.usr.view_assignments("blahalskfflkdsjf")



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
