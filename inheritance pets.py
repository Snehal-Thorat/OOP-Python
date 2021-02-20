class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Speak general method")


class Cat(Pet): #inheriting upper class Pet
    def __init__(self, name, age, color):
        super().__init__(name,age) #super class is the class that we inherit from here
        self.color = color

    def speak(self):
        print("Meowwww")

    def get_color(self):
        return self.color

class Dog(Pet):
    def speak(self):
        print("Bark")

class Deer(Pet):
    pass

if __name__ == "__main__":
    p1 = Pet('Cheddar',10)
    p1.show()

    c1 = Cat("Snowbell",20,"White")
    c1.show()
    c1.speak()
    print(c1.get_color())

    d1 = Dog("Rocky",30)
    d1.show()
    d1.speak()

    de1 = Deer("Joe",50)
    de1.show()
    de1.speak()
