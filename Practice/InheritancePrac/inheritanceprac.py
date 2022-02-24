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
    def setAddress(self, address):
        self.__address = address

    def __str__(self):
        return "Name(Address)".format(self.getName(), self.getAddress())

class Student(Person):
    def __init__(self, name, address, numCourses = 0, courses = [], grades = []):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades

    def addCourseGrade(self, course, grades):
        self.__courses = course
        self.__grades = grades

    # prints course and respective grade
    def printGrades(self):
        print("Course: {} Grade: {}".format(self.__courses, self.__grades))

    # sum of grades in list divided by the length of the list
    def getAverageGrade(self, grades):
        return sum(grades)/len(grades)

    def __str__(self):
        return "Student: name(address)".format(self.__name, self.__address)

class Teacher(Person):
    def __init__(self, name, address, numCourses = 0, courses = []):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses

    # if course is already available return false
    def addCourse(self, courses):
        self.__courses = courses
        if self.__courses in courses:
            return 0
        else:
            return 1

    # if course is not available return false
    def removeCourse(self, courses):
        self.__courses = courses
        if self.__courses in courses:
            return 1
        else:
            return 0

    def __str__(self):
        return "Teacher: name(address)".format(self.__name, self.__address)
