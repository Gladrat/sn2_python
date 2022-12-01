from dice import *


my_besace = []

for _ in range(0, 15):
    one_dice = Dice(10)
    print(one_dice)
    my_besace.append(one_dice)
    
print(my_besace)
print(my_besace[7].roll())

for des in my_besace:
    for i in range(0, 10):
        print(des.roll())
        
# etudiants = ["Bernard", "Josiane", "Philippe"]
# print(etudiants[0])
# print(etudiants[1])
# print(etudiants[2])

eleve = {
    "nom": "Max",
    "age": 27,
    "genre": "h"
}
print(eleve["age"])
etudiant = [
    {
    "nom": "Max",
    "age": 27,
    "genre": "h"
    },
    {
    "nom": "Helen",
    "age": 23,
    "genre": "f"
    }
]
print(etudiant[1]["age"])