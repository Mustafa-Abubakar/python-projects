"""Creating a dictionary"""
Student_marks = {
    'Python': 99,
    'Web design': 95,
    'English': 94,
    'Computer': 97
}
# retrieving all the items in the dictionary
print(Student_marks)
# retrieving all the values in the dictionary
print('Python:', Student_marks['Python'])
print('Web design:', Student_marks['Web design'])
print('English:', Student_marks['English'])
print('Computer:', Student_marks['Computer'])
# Adding elements to a dictionary
Student_marks['Islamic study'] = 100
print(Student_marks)
# deleting elements to a dictionary
del Student_marks['English']
print(Student_marks)
# Getting length f the dic
print(len(Student_marks))
