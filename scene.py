from item import Item

class Scene:
   def __init__(self, description):
       self.description = description

   def enter(self, player):
       self.describe()
       
   def describe(self):
       print(self.description)


class TravelS(Scene):
   def __init__(self, lore, destinations):
       super().__init__(lore)
       self.destinations = destinations


   def enter(self, player):
       self.describe()
       #CODY
       print("Paths:")
       for index, destination in enumerate(self.destinations, 1):
            print(f"{index}. {destination}")


class InteractionS(Scene):
    def __init__(self, lore, enemy, item):
       super().__init__(lore)
       self.enemy = enemy
       self.item = item
    def enter(self, player):
        self.describe()
        if self.enemy:
            self.char_interaction(player)
        if self.item:
            self.item_interaction(player)

    def char_interaction(self,player):
        print(f"You encounter a {self.enemy}!!!")
        choice = input("Defend or attack? (D/A)")
        if choice == "D":
            print("You successfully defended yourself")
        if choice == "A":
            print("You successfully attack the enemy")


    def item_interaction(self, player):
        if self.item.is_special:
            choice= input("Do you wish to insert it in your inventory or examine it? (I/E)")
            if choice == "I":
                print(f"You hastily pick up the {self.item.name}... It was a trap!")
                player.take_damage(10)
                player.pick_up_item(self.item)

            elif choice == "E":
                print(f"You disovered a {sef.item.name}...")
                print(f"You examine it carefully: {self.item.description}")
                print(f"As you were distracted, a ghoul lunged at your before you could react!")
                player.take_damage(10)
        else:   
            print(f"You discover a {self.item.name} and insert it into your inventory")
            print(f"Description: {self.item.description}")

