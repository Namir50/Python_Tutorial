#When Number of values you want to pass is not known
#Like we pass multiple values in the print fucntion
#The value are stored in tuple

def test(*args):
    print(args)
print(test(1,2,3))

def testing(*args):
    print(args)
    print(type(args))
print(testing(1,2,3,4,"Namir",100,"Shah"))

def tests(*args):
    for i in args:
        print(i , end = " ")
print(tests(1,2,3,4,"Namir", 80, "Hello"))

def t(*args):
    for i in args:
        print(i*i,end = " ")
print(t(1,2,3,4,5,6,7,8,9))
