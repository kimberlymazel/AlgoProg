class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    # getter methods
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    # setter method
    def setAddress(self, addressnew):
        self.__address = addressnew

    def __str__(self):
        return "Name(Address)".format(self.getName(), self.getAddress())

class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []

    def addCourseGrade(self, courses, grades):
        self.__courses.append(courses)
        self.__grades.append(grades)
        self.__numCourses += 1

    # prints course and respective grade
    def printGrades(self):
        print(self.__grades)

    # sum of grades in list divided by the length of the list
    def getAverageGrade(self, grades):
        return sum(grades)/len(grades)  # or /numCourses

    def __str__(self):
        return "Student: name(address)".format(self.__name, self.__address)

class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []

    # if course is already available return false
    def addCourse(self, courses):
        if courses in self.__courses:
            return False
        self.__courses.append(courses)  # adds inputted course into list
        self.__numCourses += 1  # updates number of courses

    # if course is not available return false
    def removeCourse(self, courses):
        if courses not in self.__courses:
            return False
        self.__courses.remove(courses)  # removes inputted course into list
        self.__numCourses -= 1  # updates number of courses

    def printCourses(self):
        print(self.__courses)

    def __str__(self):
        return "Teacher: name(address)".format(self.__name, self.__address)
