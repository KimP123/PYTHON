class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(f"Full Name: {self.fname} {self.lname}")
class Student(Person):
    def __init__(self, fname,lname,year):
        super().__init__(fname,lname)
        self.year = year
student1 = Student("Kimora", "Payne", "2025")
student1.printname()
print(student1.year)