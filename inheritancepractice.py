class Person:
    
    def get_name(self):
        return 'Joshua'

class Student(Person):

    def get_number(self):
        return '0123456789'

class International_Student(Student):
    def get_visa(self):
        return('VISA 2233332')

international_student = International_Student()
print(international_student.get_visa())
print(international_student.get_name())