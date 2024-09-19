
#Provides character class and create_player function for managing player characters

#Character class handles introduction and selection of class choice. 
# create_player creates a new player object with selected class and initializes health and strength

from tabulate import tabulate
from player import Player

class Character:
    def introduction(self):
        data = [["Mage", 60, 8, 2],
                ["Ranger", 80, 6, 4]]
        headers = ["Class", "Health:", "Strength:"]
        table = tabulate(data, headers=headers, tablefmt="psql", numalign="center")
        print(table)

        valid_classes = ['mage', 'ranger']
        while True:
            class_input = input("Select your class:").lower()
            if class_input in valid_classes:
                return class_input
            else:
                print("Invalid class. Please select from mage or ranger.")     
        
def create_player():
    temp_character = Character()
    skill_class = temp_character.introduction()

    if skill_class == 'mage':
        player = Player('Sora the Mystic', 'mage')
        player.health=60
        player.strength=8

    elif skill_class == 'ranger':
        player = Player('Lirael, Wanderer of Waste', 'ranger')
        player.health=80
        player.strength=6

    #print(f""" "My name is {player.name} and I am of the {player.skill_class} class." """)
    return player
