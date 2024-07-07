#capatalize: capatilizes starting alphabet
#title: cpapitalizes starting alphabet of every word
#upper: converts the whole string in upper case
#lower: converts the whole string in lower case
#find: returns the index of the first occurence of the string
#count: returns the number of occurences of a string
##index
#replace: replaces a particular string
#split: seperates string
#islower: return boolean based on the string lowercase
#isupper: returns boolean based on th string uppercase
#isnumeric: returns boolean based on the pure numeric string
#isalpha: returns boolean based on the alphanumeric string

name = "namir shah"

print(name.capitalize()) 

print(name.title())

print(name.upper())

print(name.lower())

print(name.find("a"))
print(name.find("h"))

print(name.count("a"))
print(name.count("b"))

print(name.replace("n", "s"))

print(name.split())

print(name.islower())

print(name.isupper())

print("21".isnumeric())
print("21n".isnumeric())

print(name.isalpha())   #because there's a space in between
print("namir".isalpha())


