#Apart from special methods you can make yoour custom methods
#Example: Humans can speak, think, eat

class Teacher:
    def __init__(self, name, qualification, addr):
        self.name = name
        self.qualification = qualification
        self.addr = addr
    
    def order(self):
        return(f"{self.name} You must go to your alotted class to teach")
    
damini = Teacher("Damini", "MSc.Maths", "Mumbai")
print(f"{damini.name}'s qualification is {damini.qualification}, Address is {damini.addr}")
print(damini.order())

Silviya = Teacher("Silviya", "Mtech", "Mumbai")
print(f"{Silviya.name}'s qualification is {Silviya.qualification}, Address is {Silviya.addr}")
print(Silviya.order())

class Employee:
    def __init__(self, name, age, address):   
        self.name = name
        self.age = age
        self.address = address
    
    def command(self):
        return(f"{self.name} complete your work ASAP")

Raj = Employee("Raj", 34, "Jogeshwari")
print(f"{Raj.name}'s Age is {Raj.age}, Address is {Raj.address}")
print(Raj.command())


