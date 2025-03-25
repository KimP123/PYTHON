class Student:
    grade = 12
    name = "Kimora"

    def introduction(self):
        print("I am a student")
    def details(self):
        print("My name is", self.name)
        print("I am in", self.grade)
obj = Student()
obj.introduction()
obj.details()           