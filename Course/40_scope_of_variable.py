#There are two scope of variable: global and local
#Global variavle can be used anywhere in the program
#Local variable can only be used in that particular function

a = 100   #a is global variable
def num():
    return a
print(num())

def exp():
    x = 200  #x i local variable
    return x
print(exp())
#print(x) #this will cause an error as x is local variable and it cannot be used outside the function

#changing the value of global variable using inside part of the function
b = 500
def func():
    global b 
    b = 300
    return b
print(func())