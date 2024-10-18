#When a class derives every attributes and methods from other class
#I gets access to all methods and attributes
#This helps in reusability of code
#Base class: Parent class
#Derived class: Child class

class Person:
    name = " "
    age = 0
    address = " "

class Teacher(Person):
    pass
Damini = Teacher()
Damini.name = "Damini"
Damini.age = 35
Damini.address = "Mumbai"

print(f"{Damini.name}'s age is {Damini.age} and address is {Damini.address}")

Silviya = Teacher()
Silviya.name = "Silviya"
Silviya.age = 38
Silviya.address = "Thane"

print(f"{Silviya.name}'s age is {Silviya.age} and address is {Silviya.address}")

class Employee:
    def __init__(self, e_name, e_id, e_dept):
        self.e_name = e_name
        self.e_id = e_id
        self.e_dept = e_dept
    
class e(Employee):
    pass
emp_1= e("Namir", 20, "Information Technology")
print(f"Employee 1's name is {emp_1.e_name}, id is {emp_1.e_id} and department is {emp_1.e_dept}")

emp_2 = e("Shah", 21, "Electronics")
print(f"Employee 2's name is {emp_2.e_name}, id is {emp_2.e_id} and department is {emp_2.e_dept}")

class Person():
    def __init__(self, name, age, bloodgroup):
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
    
    def greet(self):
        return(f"{self.name} your bloodgroup is {self.bloodgroup}")

class p(Person):
    pass

p1 = p("Namir", 20, "AB+")
print(p1.greet())
p2 = p("Ginger", 2, "B+")
print(p2.greet())
p3 = p("Ibaad",5,"B+")
print(p3.greet())


#Adding more attributes in derived class
class HumanBeing():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(HumanBeing):
    def __init__(self, name, age, company, post):
        super().__init__(name,age)
        self.company = company
        self.post = post

e1 = Employee("Namir", 20, "Google", "Machine Learning Engineer")
print(f"{e1.name}'s company and post is {e1.company} and {e1.post}")

e2 = Employee("Shah", 21, "Microsoft", "Artificial Intelligence Engineer")
print(f"{e2.name}'s company and post is {e2.company} and {e2.post}")




    








