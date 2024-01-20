class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course_id, mark):
        self.marks[course_id] = mark

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}")


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_info(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        return Student(student_id, name, dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_info(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        return Course(course_id, name)

    def select_course_input_marks(self):
        if not self.students or not self.courses:
            print("No students or courses available. Please add students and courses first.")
            return

        course_id = input("Enter the course ID to input marks for students: ")

        if course_id not in [course.course_id for course in self.courses]:
            print("Course ID not found.")
            return

        for student in self.students:
            mark = input(f"Enter mark for {student.name} in {course_id}: ")
            student.input_marks(course_id, mark)

    def list_students(self):
        print("List of students:")
        for student in self.students:
            student.display_info()

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Name: {course.name}")


    def show_student_marks(self):
        print("Student marks for all courses:")
    
        for course in self.courses:
            print(f"\nCourse {course.course_id}: {course.name}")
        
            for student in self.students:
                if course.course_id in student.marks:
                    print(f"{student.name}: {student.marks[course.course_id]}")
                else:
                    print(f"{student.name}: No mark entered")


if __name__ == "__main__":
    school = School()

    num_students = school.input_number_of_students()
    for _ in range(num_students):
        student = school.input_student_info()
        school.students.append(student)

    num_courses = school.input_number_of_courses()
    for _ in range(num_courses):
        course = school.input_course_info()
        school.courses.append(course)

    while True:
        print("\n1. Select a course and input marks for students")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            school.select_course_input_marks()
        elif choice == '2':
            school.list_courses()
        elif choice == '3':
            school.list_students()
        elif choice == '4':
            school.show_student_marks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
