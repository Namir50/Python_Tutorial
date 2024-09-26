#This block will be executed in any case
#It is helpful when you want to deallocate resources
#Like closing a file, db connection

a=5
b=0

try:
    print("Hello")
    print(a/b)
except Exception as e:
    print("There is an error", e)
finally:
    print("The execution is completed")

try:
    print("Hello")
    print(20/2)
except Exception as e:
    print("There is an error", e)
finally:
    print("The execution is completeds")