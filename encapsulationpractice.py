class Student:

    def __init__(self, fname, lname):
        self._firstname = fname
        self._lastname = lname

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @firstname.setter
    def firstname(self,fname):
        self._firstname = fname
    
    def set_firstname(self,fname):
        self._firstname = fname

    def show_name(self):
        return f'{self._firstname} {self._lastname}'

mike = Student('Mike','McConnehey')
print(mike.show_name())
print(mike.firstname)
mike.firstname = 'bob'
print(mike.show_name())