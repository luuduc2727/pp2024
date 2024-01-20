def input_number_of_students():
    while True:
        try:
            num_students = int(input("Enter the number of students in the class: "))
            
        except ValueError:
            print("Please enter a valid integer for the number of students.")
        else:
            break 
    return num_students


def input_student_info():
    student_info = {}
    student_info['id'] = input("Enter student ID: ")
    student_info['name'] = input("Enter student name: ")
    student_info['dob'] = input("Enter student date of birth: ")
    return student_info

def input_number_of_courses():
    while True:
        try:
            num_course = int(input("Enter the number of courses: "))
            
        except ValueError:
            print("Please enter a valid integer for the number of courses.")
        else:
            break 
    return num_course

def input_course_info():
    course_info = {}
    course_info['id'] = input("Enter course ID: ")
    course_info['name'] = input("Enter course name: ")
    return course_info

def input_student_marks(students, courses, marks):
    course_id = input("Enter the course ID to input marks for students: ")
    
    if course_id not in courses:
        print("Course ID not found.")
        return None  # Return None or some indicator to handle the case of an invalid course ID

    if course_id not in marks:
        marks[course_id] = {}  # Initialize an empty dictionary for the course if not present

    for student in students:
        mark = input(f"Enter mark for {student['name']} in {courses[course_id]['name']}: ")
        marks[course_id][student['id']] = mark

    return marks



def list_courses(courses):
    print("List of courses:")
    for course_id, course_info in courses.items():
        print(f"Course ID: {course_id}, Name: {course_info['name']}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks(marks, courses, students):
    course_id = input("Enter course ID to show student marks: ")
    if course_id not in courses: 
        print("Course ID not found.")
        return

    if course_id in courses:
        print(f"Student marks for {courses[course_id]['name']}:")

        for student_id, mark in marks[course_id].items():
            student_name = next((student['name'] for student in students if student['id'] == student_id), None)
            if student_name:
                print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")
            else:
                print(f"Student ID: {student_id}, Mark: {mark}")
    else:
        print("No marks entered for this course yet.")


def main():
    students = []
    courses = {}
    marks = {}

    num_students = input_number_of_students()
    
    
    
    for i in range(num_students):
        student_info = input_student_info()
        students.append(student_info)

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_info()
        courses[course_info['id']] = course_info

    while True:
        print("\n1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            marks = input_student_marks(students, courses, marks)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)        
        elif choice == '4':
            show_student_marks(marks, courses, students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
