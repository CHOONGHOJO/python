class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("AA", 36)
p1.myfunc()
 
del p1.name
p1.myfunc()