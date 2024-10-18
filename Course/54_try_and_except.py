#try : this block handles the error in the code if any of it exists
#except: this block gives the output that you want to show if your code is faulty

a = 5
b = 0
c = 2

try:
    print(a/b)

except:
    pass

try:
    print(a/b)

except:
    print("There is an error you must correct")


try:
    print("Hello there")
    print(a/b)
except:
    print("Check your code")


try:
    print(a/c)
except:
    print("Error")

try:
    print(a/b)
except Exception as e:    #Exception defined the type of error
    print("There is an error", e)

try:
    print(hello)
except Exception as e:
    print('there was a problem',e)