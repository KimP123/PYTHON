class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idnumber}")
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        super().__init__(name,idnumber)
        self.salary = salary
        self.post = post
emp = Employee("Kimora", "ID1234", 20000, "Software Engineer")
emp.display()