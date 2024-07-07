#dictionary has key value pair form of data
#dictionaries are ordered
#does not support indexing
#data can be accessed using keys

a = {}
print(type(a))

b = dict()
print(type(b))

fruits = {"appple" : 100,
          "mango" : 200,
          "banana" : 50,
          "watermelon" : 70,
          "pineapple" : 90}

print(fruits)
print(fruits.values())
print(fruits.keys())
print(fruits.items())

    
#creating dictonaries using zip
name = ["Namir", "Ibaad", "Armaan"]
rollno = [50, 60, 70]

students = dict(zip(name,rollno))
print(type(students))
print(students)
print(len(students))

#accessing data from dictionaries
print(students["Namir"])
print(fruits["mango"])
print(students["Ibaad"])

#get method: to avoid error and give a message
print(students.get("samira", "There is no such student"))
print(students.get("Vahid", "There is no such student"))
print(fruits.get("Guava", "Not available"))
print(fruits.get("Dragonfruit", "Not availabe"))


#updating dictionaries of existing data
fruits["pineapple"] = {"small": 60, "large" : 90}
print(fruits)
fruits["mango"] = 210
print(fruits)

#uppdating dictionaries with new values
fruits["strawberry"] = 180
print(fruits)

#updating dictionaries with new dictionaries
new_fruits = {"Grapes" : 80, "Licchi" : 90, "Berries" : 130}
fruits.update(new_fruits)
print(fruits)

new_students = {"Ayaan" : 20, "Rehmaan" : 40}
students.update(new_students)
print(students)

#iteration
for i in students:
    print(students[i])

for i in students:
    print(i, students[i])


for i in students:
    for j in i:
        print(j)


for key in fruits:
    print(key)

for i in fruits:
    print(i, fruits[i])

