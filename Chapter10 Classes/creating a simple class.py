class Student:
    def __init__(self, python, Java):
        self.python = python
        self.Java = Java
    
    def __add__(self, other):
        m1 = self.python+other.python
        m2 = self.Java+other.Java
        s3 = m1+m2
        return s3
    
    def __gt__(self, other):
        if self.python>other.python:
            print('s1 is gteater')


mark1 = Student(100, 99)
mark2 = Student(94, 97)

if mark1.python>mark2.python:
    print('pppp')