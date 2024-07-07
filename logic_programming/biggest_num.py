a = float(input("Enter value of A: "))
b = float(input("Enter value of B: "))
c = float(input("Enter value of C: "))

if a > b and a > c:
    print(a, "is the largest number among them")
elif b >a and b > c: 
    print(b, "is the largest number among them")
else:
    print(c, "is the largest number among them")