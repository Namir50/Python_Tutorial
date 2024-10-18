#Class is a bluepprint to create objects
#The class keyword is used to create classes
#We start name of the class with capital letter
#Objects are instances or entities of a class
#It has all properties of its class

#create a class
class Bike:
    name = " "
    gear = 0

#craete object of that class
bike1= Bike()
print(type(bike1))

#access attributes of thec class and assign new values
bike1.name = "Royal Enfield"
bike1.gear = 5

print(f"Name of the Bike is {bike1.name} and it has {bike1.gear} gears ")

class Employee:
    e_name = " "
    e_id = 0
    e_address = " "

employee1 = Employee()
employee1.name = "Namir"
employee1.id = 1
employee1.address = "Jogeshwari"

employee2 = Employee()
employee2.name = "Shah"
employee2.id = 2
employee2.address = "Andheri"

print(f"Employee Id and Employee Address of {employee1.name} is {employee1.id} and {employee1.address}")
print(f"Employee Id and Employee Address of {employee2.name} is {employee2.id} and {employee2.address}")

class Students:
    s_name = " "
    s_rollno = 0
    s_std = 0
    s_div = " "

student1 = Students()
student1.s_name = "Ron"
student1.s_rollno = 50
student1.s_std = 5
student1.s_div = "B"

print(f"Roll Number of {student1.s_name} is {student1.s_rollno}, Standard is {student1.s_std}, Division is {student1.s_div}")

student2 = Students()
student2.s_name = "Harry"
student2.s_rollno = 60
student2.s_std = 7
student2.s_div = "A"

print(f"Roll Number of {student2.s_name} is {student2.s_rollno}, Standard is {student2.s_std}, Division is {student2.s_div}")

student3 = Students()
student3.s_name = "Voldemort"
student3.s_rollno = 70
student3.s_std = 10
student3.s_div = "A"

print(f"Roll Number of {student3.s_name} is {student3.s_rollno}, Standard is {student3.s_std}, Division is {student3.s_div}")