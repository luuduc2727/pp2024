from input import input_student, input_course, input_mark_stu
from output import display_stu_list, display_course_list
from domains.students import Student
from domains.courses import Course
from  zipfile import ZipFile, ZIP_DEFLATED



NumberStd = int(input("Enter number of Students: "))

stu_list = input_student(NumberStd)

NumberOfCourse = int(input("Enter number of Courses: "))

course_list = input_course(NumberOfCourse)


display_stu_list(stu_list)
display_course_list(course_list)

input_mark_stu(stu_list, course_list)

zip_path = '22bi13088.zip'
file_to_zip = ['./courses.txt', './students.txt', './marks.txt']
with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
        for file in file_to_zip:
            zip.write(file)