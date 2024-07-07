x = int(input("Number till which you want prime numbers"))

for i in range(1, x+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
          print(i,"is a prime number")
        


int = int(input("Enter a number: "))
if int < 1:
    print("It is not a prime number")
else:
    for i in range(2, int+1):
        if int % i == 0:
            print("It is not a prime number")
            break
        else:
          print("It is a prime number")
          break
        