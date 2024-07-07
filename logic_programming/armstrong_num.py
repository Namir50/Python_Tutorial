
def is_armstrong(num):
    sum = 0
    temp = num
    num_digits = len(str(num))

    while temp > 0:
        digit = temp %10
        cube = digit ** num_digits
        sum +=cube
        temp//= 10

    return sum == num
    

while True:  
  num = int(input("Enter a number: "))
  if is_armstrong(num):
    print("It is an armstrog number")
    continue
  else:
    print("It is not an armstrong number")
    break
