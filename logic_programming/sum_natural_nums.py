x =int(input("Enter start number: "))
y = int(input("Enter end date: "))
sum = 0

for i in range(x, y+1):
    sum += i

print(sum)


#Using recursion
def sum_recusion(x,y):
    if x == y:
        return x
    else:
        return x + sum_recusion(x+1, y)


while True:
    x = int(input("Enter start number: "))
    y = int(input("Enter end number: "))
    if x < 0 or y< 0:
        print("Enter Natural/Positive number")
        continue
    else:
       print(sum_recusion(0,10))
       break

