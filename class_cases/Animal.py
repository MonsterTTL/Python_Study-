class Animal:
    '动物类'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, kg):
        print("animal:", self.name, "eat", kg)
        self.weight += kg
        print("new weight is", self.weight)

class Cat(Animal):
    def __init__(self, weight):
         super().__init__("Cat", weight)

animal = Animal("zsj", 24)
animal.eat(15)
cat = Cat(25)
cat.eat(11)