from abc import ABC, abstractmethod
class Animal (ABC):
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def move(self):
        print("The dog runs on four legs.")
class Cat(Animal):
    def move(self):
        print("All cats are cute.")
dog = Dog()
cat = Cat()
dog.move()
cat.move()