from dice import *
# from __future__ import annotations


class Caracter:
    _type = "Caracter"

    def __init__(self, name, hp_max, attack, defense, dice):
        self._name = name
        self._hp_max = hp_max
        self._hp = hp_max
        self._attack = attack
        self._defense = defense
        self._dice = dice

    def __str__(self):
        return f"Hello ! My name is {self._name}. I'm a {self._type} with {self._hp}/{self._hp_max} hp."
    
    def is_alive(self):
        return (self._hp > 0)
    
    def show_health_bar(self):
        if self._hp < 0:
            self._hp = 0
        missing_hp = self._hp_max - self._hp
        health_bar = f"[{'#'*self._hp}{' '*missing_hp}] {self._hp}/{self._hp_max}"
        print(health_bar)
        # return health_bar

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        self._hp = hp

    def get_name(self):
        return f"@{self._name}"

    def final_attack(self, result, damages, target):
        return damages

    def attack(self, target):
        if (self.is_alive() and target.is_alive()):
            damages = 0
            result = self._dice.roll()
            damages = self._attack + result
            damages = self.final_attack(result, damages, target)
            print(f"> {self._type} {self.get_name()} attack {target.get_name()} with {damages} : {self._attack} (attack) + {result} (roll)")
            target.defend(damages, self)
    
    def final_defend(self, result, wounds, attacker):
        return wounds
    
    def defend(self, damages, attacker):
        wounds = 0
        result = self._dice.roll()
        wounds = damages - self._defense - result
        wounds = self.final_defend(result, wounds, attacker)
        # utilisation de final_defend()
        print(f"< {self._type} {self.get_name()} took {wounds} wounds from {attacker.get_name()} : {damages} (damages) - {self._defense} (defense) - {result} (roll)")
        self._hp = self._hp - wounds
        self.show_health_bar()

class Warrior(Caracter):
    _type = "Warrior"
    
    def final_attack(self, result, damages, target):
        print("Coup de hache ! (bonus: +3)")
        return damages + 3
    
class Mage(Caracter):
    _type = "Mage"
    
    def final_defend(self, result, wounds, target):
        print("Armure magique ! (bonus: -3)")
        return wounds - 3

class Thief(Caracter):
    _type = "Thief"
    
    def final_attack(self, result, damages, target):
        dague = target._defense
        print(f"Coup de dague ! (bonus: +{dague})")
        return damages + dague

class Druid(Caracter):
    _type = "Druid"
    
    def defend(self, damages, attacker):
        super().defend(damages, attacker)
        heal = self._dice.roll()
        self._hp = self._hp + heal
        print(f"Vague de soin ! (bonus: +{heal} hp)")
        self.show_health_bar()
        
class Necro(Caracter):
    _type = "Necro"
    
    def defend(self, damages, attacker):
        super().defend(damages, attacker)
        life_leach = self._dice.roll()
        self._hp = self._hp + life_leach
        print(f"Vol de vie ! (bonus: +{life_leach} hp)")
        attacker.set_hp(attacker.get_hp() - life_leach)
        self.show_health_bar()

if __name__ == "__main__":
    my_new_dice = Dice()
    car1 = Warrior("Max", 20, 8, 3, my_new_dice)
    car2 = Druid("Helen", 20, 8, 3, my_new_dice)

    while car1.is_alive() and car2.is_alive():
        car1.attack(car2)
        car2.attack(car1)