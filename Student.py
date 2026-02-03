# Create a class Student that keeps track of the total number of students created using a class variable.

class Student:
    number_of_students = 0

    def __init__(self, name):
        self.name = name
        Student.number_of_students += 1

s1 = Student('Anna')
s2 = Student('Vahe')
s3 = Student('Vardanush')

print(Student.number_of_students)