from core.models.users import User
from core.models.students import Student
from core.models.teachers import Teacher
from core.models.assignments import Assignment

def test_create_student():
    username = 'student_3'
    student_user_1 = User(email='student3@fylebe.com', username=username)
    student_1 = Student(id = 3,user_id=User.get_by_email('student1@fylebe.com').id)
    repr_test_user = f'<User \'{student_user_1.username}\'>'
    repr_test_student = f'<Student {student_1.id}>'
    assert student_user_1.username == username
    assert student_1.user_id ==User.get_by_email('student1@fylebe.com').id
    assert student_1.id ==3
    assert repr(student_1) == repr_test_student
    assert repr(student_user_1) == repr_test_user

def test_create_teacher():
    username = 'teacher_3'
    teacher_user_1 = User(email='teacher1@fylebe.com', username=username)
    teacher_1 = Teacher(id=1,user_id=User.get_by_email('teacher1@fylebe.com').id)
    repr_test_teacher = f'<Teacher {teacher_1.id}>'
    
    assert teacher_1.user_id == User.get_by_email('teacher1@fylebe.com').id
    assert repr(teacher_1) == repr_test_teacher



def test_create_assignment():
    username = 'student_3'
    student_user_1 = User(email='student3@fylebe.com', username=username)
    student_1 = Student(id = 3,user_id=User.get_by_email('student1@fylebe.com').id)
    assignment_1 = Assignment(id=1,student_id=student_1.id)
    repr_assignment_test = f'<Assignment {assignment_1.id}>'

    assert repr(assignment_1) == repr_assignment_test