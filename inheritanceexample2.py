class Person:
    
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class Student(Person):

    def __init__(self, name, number):
        super().__init__(name)
        self._number = number

    def set_number(self, number):
        self._number = number

    def get_number(self):
        return self._number

student = Student('Jane Doe', 12234)
name = student.get_name()
number = student.get_number()
print(name, number)