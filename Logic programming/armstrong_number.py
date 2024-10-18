

num = int(input("Enter a number: "))
sum = 1
temp = num

while temp > 0 :
    digit = temp%10
    cube = digit**3
    sum +=cube
    temp //=10

if sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an armstrong number")