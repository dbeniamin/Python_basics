# DRY - Don't Repeat Yourself

# use inheritance , dog / cat class inherit all the methods defined in the parent class
# 2 blank lines after each class
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass

dog1=Dog()
dog1

# creating a dog / cat object , type object. the methods defined will appear

class Dog:
    def walk(self):
        print("walk")


class Cat:
    def walk(self):
        print("walk")
