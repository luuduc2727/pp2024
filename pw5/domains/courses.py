class Course:
    def __init__(self, id="", name="", credit=0):
        self.__id = id
        self.__name = name
        self.__credit = credit
  
    def getId(self):
        return self.__id
        
    def getName(self):
        return self.__name

    def getCredit(self):
        return self.__credit

    def __str__(self):
        return "Course: " + self.__name + " id " + self.__id + " credit " + str(self.__credit)

    def describe(self):
        print(self.__str__())