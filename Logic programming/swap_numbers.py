#using 3rd variable
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

temp = a  #so temp is a
a = b #so a is b
b = temp # so b is temp

print("Value after swap: \na=",a,"\nb=",b)


#replacing variables
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

x, y = y , x

print("Value after swap: \nx=",x,"\ny=",y)

