#Functions is a user defined piece of code that can be called from anywhere in the program.
#It helps in reusability of code and reduces errors
#Makes code managebale and organized
#There are tow types of functions which are built in functions and user defined functions

def greeting(): #defining a function
    print("Hey good morning!")

greeting() #Calling function
print(type(greeting))

def year():
    print("This is 2023")
year()
 
def greeting(name):  #there is parameter in bracket while defining a function
    print("Have a Good day",name)

greeting("Namir")   #there is argument in the bracket while calling a function
greeting("Ibaad")
greeting("Ginger")

def add(a,b):
    sum = a+b
    print(sum)

add(10,15)
add(10,2000)
add(100,1456)

def sub(a,b):
    sub = a-b
    print(sub)

sub(10,8)
sub(10,29)
sub(190,230)

# create a for loop fro printing numberw from 1 to 10