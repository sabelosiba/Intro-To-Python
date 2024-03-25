class Person:
    
    def __init__(self, fname, lname ):
        self.fname = fname
        self.lname = lname
        
    def full_name(self):
        return "{0} {1}".format(self.fname, self.lname)

p = Person("John", "Doe")
print( p.full_name() )   # Outputs: John Doe</s>


'''     self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)'''

#x = Person("John", "Doe")
#x.printname()

class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self.grade = grade

    def print_info(self):
         """Print the student's information."""
         print("Student name: ", self.full_name())
         print("Grade level: ", self.grade)


    ''' def __init__(self, fname, lname, year):
        super().__init__(self,fname,lname)
        self.year = year'''


y = Student( "Jane", "Smith", 75 )
print(y.grade)
y.print_info()