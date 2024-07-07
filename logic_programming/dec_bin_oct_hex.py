x = int(input("Enter a number: "))

print(x,"in binary is",bin(x),"\n")
print(x,"in octal is",oct(x),"\n")
print(x,"in hexadiecimal",hex(x),"\n")

def conver_binary(num):
    if num >1:
        conver_binary(num//2)
    print(num%2,end = ' ')
x = int(input("Enter a number to convert it into binary: "))
(conver_binary(x))
    

