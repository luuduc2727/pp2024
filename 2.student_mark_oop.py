class Student():
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}
    
    def _get_name(self):
        return self.name

    def _get_id(self):
        return self.id

    def _get_dob(self):
        return self.dob

    def add_mark(self, course_id, mark):
        self.mark[course_id] = mark 

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Dob: {self.dob}")

class Courses():
    def __init__(self, name_course, course_id):
        self.name_course = name_course
        self.course_id = course_id

    def _get_name_course(self):
        return self.name_course

    def _get_course_id(self):
        return self.course_id

   
class School:  
    def __init__(self):
        self.students = []
        self.courses = []
    def input_number_of_student(self):
        return int(input("Enter number of student: "))
    
    def input_student_infor(self):
        id = int(input("enter id student: "))
        name = str(input("enter name of student: "))
        dob = input("enter date of birth of student: ")
        return Student(id, name, dob)
    
    def input_number_of_course(self):
        return int(input("Enter number of course: "))

