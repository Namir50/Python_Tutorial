#lambda functions are mainly used when we need nameless functions for a short period of times
def add(a,b):
    return a+b
print(add(5,6))

print((lambda c, d: c*d)(10,20))

print((lambda x, y: x %y) (30,5))

def larger(A,B):
    if A>B:
        return 
    else:
        return B
print(larger(30,50))

print((lambda X,Y: X if X>Y else Y) (90,70))

def evenorodd(n):
    if n%2==0:
        return ("The Number is Even")
    else:
        return ("Number Is Odd ")
print(evenorodd(76))

num = (lambda N: "The Number is Even" if N%2==0 else "The Number is Odd")
print(num(87))

