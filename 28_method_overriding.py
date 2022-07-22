from re import L


class Animal:
    def __init__(self):
        self.age = 2


class Mammal(Animal):
    def __init__(self):
        super().__init__()   # calling base class constructor
        self.weight = 1