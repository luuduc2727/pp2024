from domains.students import Student
from domains.courses import Course
import math

def input_student(num_of_stu):
    student_list = []
    for i in range(num_of_stu):
        name = input("enter name student: ")
        id = input("enter id student: ")
        dob = input("enter dob student: ")
        student = Student(id, name, dob)
        student_list.append(student)

    return student_list
def input_course(num_of_course):
    course_list = []
    for i in range(num_of_course):
        id = input("enter id course: ")
        name = input("enter name course: ")
        credit = input("enter credit course: ")
        course = Course(id, name, credit)
        course_list.append(course)

    return course_list
def input_mark_stu(student_list, course_list):
    for student in student_list:
        for course in course_list:
            mark = float(input(f"mark for student {student.getName()} in course {course.getName()}"))
            student.input_mark(course.getName(), math.floor(mark * 10)/10)

