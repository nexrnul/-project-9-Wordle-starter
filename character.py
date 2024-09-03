from tabulate import tabulate
import pandas as pd


class Character:


   def __init__(self, skill_class, name, strength, health, inventory, exp=1):
       self.skill_class = skill_class
       self.name = name
       self.health = health
       self.exp = exp
       self.strength = strength
       self.inventory = inventory


   def introduction(self):
        data = [
            ["Mage", 60, 8, 2],
            ["Ranger", 80, 6, 4],
            ["Cleric", 100, 4, 3]]
        headers = ["Class", "Health:", "Strength:", "Experience rate:"]
        table = tabulate(data, headers=headers, tablefmt="psql", numalign="center")
        print(table)
        valid_classes = ['mage', 'ranger', 'cleric', 'Mage', 'Ranger', 'Cleric']
        while True:
            class_determination = input("Select your class:").lower()
            if class_determination in valid_classes:
                break
            print("Invalid class. Please select from mage, ranger, or cleric.")      
        self.skill_class = class_determination    
        #print(f"My name is {self.name} and I am of the {self.skill_class} class.")


   def attack(self):
       print(f"{self.name} attacks for {self.strength*10} damage!")
 
   def take_damage(self, damage):
       self.health -= damage
       if self.health <= 0:
           print(f"{self.name} has been defeated!")
       else:
           print(f"{self.name} has {self.health} health remaining.")

    def exp_rate(self, exp):
        self.exp_rate =

    def experience(self, exp, )
           
class mage(Character):
   def __init__(self, name, strength=8, health=60, exp=1):
       super().__init__('mage', name, strength, health, exp)


class ranger(Character):
   def __init__(self, name, strength=6, health=80, exp=1):
       super().__init__('ranger', name, strength, health, exp)


class cleric(Character):
   def __init__(self, name, strength=4, health=100, exp=1):
       super().__init__('cleric', name, strength, health, exp)


c1 = mage('A')
#c2 = ranger('b')
#c3 = cleric('c')
c1.introduction()
#c2.introduction()
#c3.introduction()
