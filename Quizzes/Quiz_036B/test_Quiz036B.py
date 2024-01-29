import pytest
from Quiz_036B import Person, Classroom, Student


def test_student():
    student = Student("Victor", 18, 95)
    assert student.get_name() == "Victor"
    assert student.get_age() == 18
    assert student.get_grade() == 95
    with pytest.raises(ValueError):
        student = Student(123, 20, 90)
        student.get_name()


def test_person():
    person = Person("John", 20)
    assert person.get_name() == "John"
    assert person.get_age() == 20
    with pytest.raises(ValueError):
        person2 = Person(123, "John")
        person2.get_name()
        person2.get_age()


def test_classroom():
    classroom = Classroom()
    student1 = Student("Victor", 18, 95)
    student2 = Student("Rocky", 16, 100)
    student3 = Student("Jenda", 15, 80)
    classroom.add_student(student1)
    classroom.add_student(student2)
    assert classroom.average_score() == (95 + 100) / 2
    classroom.remove_student(student1)
    assert classroom.average_score() == 100
    with pytest.raises(ValueError):
        classroom.remove_student(student3)
        classroom.average_score()
    with pytest.raises(ValueError):
        classroom.remove_student(student1)
        classroom.remove_student(student2)
        classroom.average_score()