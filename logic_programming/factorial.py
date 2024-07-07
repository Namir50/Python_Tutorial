#for loop approach
num = int(input("Enter a number to get its factorial: "))

fact = 1

if num < 0 :
    print("Facotrial of number less than 0 does not exist")
elif num == 0 :
    print("Factorial of 0 is 1")
else:
    for i in range(1,num +1):
        fact = fact * i
    print("Factorial of",num,"is",fact)


#recursion : calling function inside the same function
def func(a):
    if a == 0:
        return 1
    else:
        return a * func(a-1)

x = int(input("Enter number: "))
print("Factorial of x is",func(x))