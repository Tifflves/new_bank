class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, hobby, name, age):
        super().__init__(name, age)
        self.hobby = hobby



a = Child()