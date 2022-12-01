import random

# random.seed(12)

class Dice:
    _type = "dice"
    
    def __init__(self, faces=6):
        self._faces = faces
    
    def roll(self):
        return random.randint(1, self._faces)
    
    def __str__(self):
        return f"A {self._faces} faces {self._type}"
    
    def __repr__(self):
        return self.__str__()
    
class RiggedDice(Dice):
    _type = "rigged dice"
    
    def roll(self, rigged: bool = False) -> int:        
        return self._faces if rigged else super().roll()
    
    
if __name__ == "__main__": # à mettre dans tous les fichiers !
    my_dice = Dice()
    print(my_dice)
    print(my_dice.roll())

    my_rigged_dice = RiggedDice(20)
    print(my_rigged_dice)
    print(my_rigged_dice.roll(True)) # 6
    print(my_rigged_dice.roll(False)) # Valeur aléat.