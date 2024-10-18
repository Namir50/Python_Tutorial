def intro(name, college):
    print("My name is",name)
    print("My college is",college)

print(intro("Namir", "Universal"))

def introduction(name, college = "None"):
    print("My Name is", name)
    print("My college is",college)

print(introduction("Namir"))

def edu(college, course, year):
    print("My college is", college)
    print("I am Studying", course)
    print("My Year is",year)

print(edu("Universal","Engineering", "Third Year"))

def education(college = "None", course = "None", year = "None"):
    print("My college is", college)
    print("I am Studying", course)
    print("My Year is",year)

print(education("Universal"))

