class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise
        NotImplementedError("Conductor we have a problem!")

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Crow(Animal):
    def speak(self):
        return f"{self.name} says Kraa"
    
class Fox(Animal):
    def speak(self):
        return f"what does {self.name} say? Ding ding ding ding ding di-ding"


def printer(x):
    if x == 1:
        name = input("What's his/her name? ")
        animus = Cat(name)
        print(animus.speak())
    elif x == 2:
        name = input("What's his/her name? ")
        animus = Dog(name)
        print(animus.speak())
    elif x == 3:
        name = input("What's his/her name? ")
        animus = Crow(name)
        print(animus.speak())
    elif x == 4:
        name = input("What's his/her name? ")
        animus = Fox(name)
        print(animus.speak())

print("1: Cat")
print("2: Dog")
print("3: Crow")
print("4: Fox")
x = int(input("Chose an animal!! "))
printer(x)
