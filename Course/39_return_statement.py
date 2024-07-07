#a function call ends when return statement is executed
#It returns the expression back to the function
#The code after the return statement is not execuded
#If there is no return value then the function returns None

def add(a,b):
    c = a+b
    return c
print(add(3,4))

def func():
    return
c = func()
print(type(func))

def new():
    print("Before return")
    return "Executed"
print(new())

def intro(name, age, address):
    return name, age, address

c, d, e = intro("Namir", 20, "Jogeshwari")
print(c, d, e)

def edu(college, course, year):
    return college, course, year

a, b, c = edu("Universal", "Data Engineering", "Third Year")
print(a,b,c)
