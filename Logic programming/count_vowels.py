v = ['a','e','i','o','u','A','E','I','O','U']
vowels =[]

x = str(input("Enter a string: "))

for i in x:
    if i in v:
        vowels.append(i)

print(vowels)
print(len(vowels))