def factors(x):
    for i in range(1,x+1):
        if x%i==0:
         print(i,end=" ")

a = int(input("Enter a number: "))
factors(a)