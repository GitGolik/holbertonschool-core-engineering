#!/usr/bin/env python3

class Animal:
    def speak(self):
        raise Exception("speak() is not implemented")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(Dog, Animal))
