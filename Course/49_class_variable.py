#These are common to the class
#Example: Population of Human class is common to all objects of that class

class Human:
    population = 0
    data = []

    def __init__(self, name, age, alive = True):
        self.name = name
        self.age = age
        self.alive = alive
        Human.population+= 1
        Human.data.append(self.name)
    
    def dead(self):
        if self.alive:
         print(self.name,"is dead")
         Human.population -=1
         self.alive = False
        else:
            print("The person is already dead")

Namir = Human("Namir", 20)
Ginger = Human("Ginger", 21)
Vahid = Human("Vahid",56)
Samira = Human("Samira", 49)
Ibaad = Human("Ibaad", 10)
Armaan = Human("Armaan", 15)

print(Human.population)
print(Human.data)

