
a = 0 
b = 1
print(a,end = " ")
print(b, end = " ")
for i in range(0,10):
    c = a + b
    a = b 
    b = c
    print(c, end = " ")



def fib(n):
    if n <=1:
        return n
    else:
        return (n-1) + (n-2)

n = int(input("Enter upto: "))
if n < 0:
    print("Enter positive number: ")
else:
    for i in range(n):
        print(fib(i))


