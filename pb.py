class Parrot:
    species = "bird"
    def __init__(self, color, age):
        self.color = color
        self.age = age
Rio = Parrot("Blue", 10)
Macaw = Parrot("Yellow", 20)

print("Rio is a {}".format(Rio.species))
print("Macaw is a {}".format(Macaw.species))

print("Rio is {} in color and he is {} years old".format(Rio.color, Rio.age))
print("Macaw is {} in color and he is {} years old".format(Macaw.color, Macaw.age))