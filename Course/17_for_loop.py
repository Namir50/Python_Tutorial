#i is iterator
#range() is iterable
#the whole function is iteration

for i in range(1,11):
    print(i)

x=0
for i in range(x,100,1):
    if x%5==0:
        print(x)
    x+=1

m = int(input("Multiplication table of?"))
for i in range(1,11):
    print(i*m)


h = int(input("Number of design tag:"))
for i in range(h):
 for i in range(h):
    print("@",end = " ")
 print()
        
s = int(input("Pyramid Number?"))
for i in range(1, s+1):
    for j in range(i):
        print("*",end = " ")
    print()


def star_pattern(n):
    for i in range(1, n+1):
        for i in range(1,n-1):
         for i in range(1, i+1):
            print("*", end=" ")
        print()

star_pattern(5)
     

  
     


    