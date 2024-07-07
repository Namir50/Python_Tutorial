x = int(input("Enter divsor: "))

for i in range(1, 100):
    if i %x ==0:
        print(i,"is divisible by",x)
    else:
        print(i,"is not divisible by",x)