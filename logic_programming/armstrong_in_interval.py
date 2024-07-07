
def armstrong_interval(x, y):
  for i in range(x, y +1):
    temp = i
    length = len(str(i))
    sum = 0
    while temp > 0:
        digit = temp % 10
        cube = digit ** length
        sum += cube
        temp//= 10

    print(sum == i)


x = int(input("Enter start number: "))
y = int(input("Enter end number: "))
armstrong_interval(x, y)



