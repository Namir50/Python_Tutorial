#in : Citizen ship operator
planets = {"Earth" : 400, "Venus": 200, "Neptune": 300, "Saturn" : 600, "Uranus" : 500, "Jupiter" : 600}
name = {"shah":90,"Vahid":80,"Samira": 90}
print("Earth" in planets)
print("Venus" in planets)

#pop : deleting data from dictionary
planets.pop("Uranus")
print(planets)

planets.pop("Jupiter")
print(planets)

#popitem : deletes last data from the dictionary
planets.popitem()
print(planets)

#del : deletes the whole dictionary even from the memory
del name
print(name)
