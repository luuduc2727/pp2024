class Mark:
    def __init__(self, studentName, course, mark=0, credit=0, GPA=0):
        self.__studentName = studentName
        self.__course = course
        self.__credit = credit
        self.__mark = mark
        self.__GPA = GPA

    def input(self):
        print(f"Enter Student's mark for {self.__studentName}")
        self.__mark = float(input(f"in {self.__course}: "))
        self.__credit = Course.getCredit(course)

    def getMark(self):
        return self.__mark * 10 / 10

    def getCourse(self):
        return self.__course

    def getGPA(self):
        return self.__GPA * 10 / 10

    def setGPA(self, GPA):
        self.__GPA = GPA

    def getName(self):
        return self.__studentName

    def getCredit(self):
        return self.__credit

    def __str__(self):
        return "Student " + self.getName() + " has a mark of " + str(
            self.getMark()) + " in " + self.getCourse()

    def describe(self):
        print(self.__str__())