from Animal import *

class Dog(Animal):
    def __init__(self, breed: str):
        self.breed = breed

    def speak(self):
        return f"Woof! I am a {self.breed}."

class Cat(Animal):
    def __init__(self, color: str):
        self.color = color

    def speak(self):
        return f"Meow! I am a {self.color} cat."