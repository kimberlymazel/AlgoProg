from inheritanceprac import Teacher

def addingCourse():
    print("Let's add a new course!")
    newcourse = input("Enter the course name: ")
    Teacher.addCourse(newcourse)

addingCourse()
