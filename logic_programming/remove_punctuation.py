x = str(input("Enter a string to remove punctuations: "))

y = '''';:.,<>?/[]!@#$%^&*()_+`~'''

string = " "

for i in x:
    if i not in y:
        string+=i
print(string)