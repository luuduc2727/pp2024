
def display_stu_list(student_list):
    for student in student_list:
        student.describe()

def display_course_list(course_list):
    for course in course_list:
        course.describe()

"""def display_gpa(student_list):
    print("GPA for each student:")
    for student in student_list:
        print(f"{student.getName()}: {student.get_gpa()}")
"""