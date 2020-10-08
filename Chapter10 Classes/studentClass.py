class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.course = self.Course()
    
    def get_studentInfo(self):
        print('This is student information')
        print('Name: ' + self.name + '\n',
              'Age: ' + str(self.age) + '\n',
              'Grade: ' + str(self.grade))
        print()
        self.course.showInfo()
        
    class Course:
        def __init__(self):
            self.name = 'Python beginner'
            self.max_students = 250
            self.prereq = 'A student must have a laptop and an internet'
        
        def showInfo(self):
            print('Course name: ' + self.name + '\nMax students: ' + str(self.max_students) + '\nPre-requirement: ' + self.prereq)


student = Student('Ascad', 20, 12)
student.get_studentInfo()