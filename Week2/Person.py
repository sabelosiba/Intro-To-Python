class Person:
    def __init__(self, fname, lname ):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(self,fname,lname)
        self.graduationyear = year


y = Student( "Jane", "Smith", 2019 )
print(y.graduationyear)
#x.printname()