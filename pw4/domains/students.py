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
    
    
  

    
        