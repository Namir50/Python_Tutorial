#if else statement
x = 20
if x>10:
    print ("x is bigger")
else:
    print ("x is smaller")


x = "Namir"
if x == "Namir":
    print("Namir's Surname is Shah")
else :
    print("I dont know the surname")

#
a = 100
if a !=100: 
    print("The Number is not 100")
else:
    print("The Number is 100")

#
age = int(input("What's your age?"))
if age>18:
        print("You are eligible to get a driving license")
else:
    print("You are not eligible to get a driving license")
   

#if elif else statement
x = 500
if x>100:
    print("Bigger than 100")
elif x>600:
    print("Bigger than 300")
elif x>800:
    print("Bigger than 600")
else:
    print("Smaller than 100")


#
roll_num = int(input("What is your roll number?"))
if roll_num>=1 and roll_num<=30:
    print("You are in Division A")
elif roll_num>=31 and roll_num<=60:
    print("You are in division B")
elif roll_num>=61 and roll_num<=90:
    print("You are in division C")
else:
    print("You are in division D")



#Nested if else statement
age = int(input("What's your age?"))
if age>18:
    if age>80:
        print("Your driver's license has expired, please renew it.") 
    else:
        print("You are eligible to get a driving license")
else:
    print("You are not eligible to get a driving license")