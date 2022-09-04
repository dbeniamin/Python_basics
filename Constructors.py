class Person:
    def __init__(self, name):  # constructor used to pass the argument
        self.name = name

    def talk(self):  # self should be the very first parameter of every method
        print(f"Hi, i am {self.name}")


jhon = Person(" Jhon Smith")
jhon.talk()

bob = Person("Bob Smith")
bob.talk()

#  each object is a different instance of a person class

# constructor is a function that gets called at the time of creating an object
