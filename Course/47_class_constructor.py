#A constructor is a special method used to create and initialize an object of a class
#This method is defined in the class
#Construtor is executed automatically at the time of obect creation

class Person:
    def __init__(self, name, age, address):   #this double underscore is called Dunder
        self.name = name
        self.age = age
        self.address = address

Namir = Person("Namir",20,"Jogeshwari")
print(f"{Namir.name}'s Age is {Namir.age}, Address is {Namir.address}")

Shah = Person("Shah", 19, "Andheri")
print(f"{Shah.name}'s Age is {Shah.age}, Address is {Shah.address}")

class Teacher:
    def __init__(self, name, qualification, addr):
        self.name = name
        self.qualification = qualification
        self.addr = addr

Damini = Teacher("Damini", "Msc.Maths", "Mumbai")
print(f"{Damini.name}'s qualification is {Damini.qualification}, Address is {Damini.addr}")

Silviya = Teacher("Silviya", "Mtech", "Mumbai")
print(f"{Silviya.name}'s qualification is {Silviya.qualification}, Address is {Silviya.addr}")


