class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.gpa = 0

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def input_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def __str__(self):
        return "Student: " + self.__name + ", id: " + self.__id + "dob:" + self.__dob

    def describe(self):
        print(self.__str__())
    
    """def calculate_gpa(self):
        total_course = 0
        weighted_sum = 0
        gpa = weighted_sum / 3
        for  mark in self.__marks.items():   
            weighted_sum += mark 

        if total_course == 0:
            return 0

        return gpa
    
    def get_gpa(self):
        return self.calculate_gpa()"""

    
        