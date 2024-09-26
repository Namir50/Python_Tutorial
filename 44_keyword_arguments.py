#Variable number of keyword arguments
#It stores data in dictionary

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

print(func(name = "Namir", age = 18))

def function(**kwargs):
    for key,value in kwargs.items():
        print(key, value)
    print(type(kwargs))
print(function(college = "Universal", degree = "Btech", year = "3rd"))

def fun(**kwargs):
    for key,value in kwargs.items():
        print(key, value,sep = ": ")
    print(type(kwargs))
print(fun(Name = "Namir", age = 18, hobbies = ["Football", "Singing", "Gaming"]))

def mix(a,b,c, age = 25, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(age)
    print(args)
    print(kwargs)

print(mix(5,6,9)) #here we have to pass values for a,b,c compulsorily as they are non default
print(mix(5,6,9,10,60,50,name = "Namir"))
