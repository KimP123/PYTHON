class Dog:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a Dog. My name is {self.name} and I am {self.age} years old.')
    def make_sound(self):
        print('Woof Woof')
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a Cat. My name is {self.name} and I am {self.age} years old.')
    def make_sound(self):
        print('Meow Meow')

obj1 = Dog('Rover', 5)
obj2 = Cat('Goldie', 4)

for animal in (obj1,obj2):
    animal.info()
    animal.make_sound()