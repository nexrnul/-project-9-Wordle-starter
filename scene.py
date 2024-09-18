from item import Item
from character import Character
from player import Player
from puzzle.py import encrypt_msg

class Scene:
   def __init__(self, description):
       self.description = description

   def enter(self, player):
        self.player = player
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
       print("Paths: " + ", ".join(self.destinations))

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
        print(f"you encounter a {self.enemy}!!!")
        choice = input("defend or attack? (D/A)")
        if choice == "D":
            print("you successfully defended yourself")
        if choice == "A":
            print("You successfully attack the enemy")

    def item_interaction(self, player):
        if self.item.is_special:
            print (f" You have encountered a rare {self.item.name}")
            choice= input("Do you wish to insert it in your inventory or examine it? (I/E)")
            if choice == "I":
                print(f"You hastily pick up the {self.item.name}... It was cursed!")
                #player.take_damage(10)
                #player.pick_up_item(self.item)

            elif choice == "E":
                print(f"You disovered a rare{sef.item.name}...")
                print(f"You examine it carefully: {self.item.description}")
                msg = "frozen"
                shift = 2
                if encrypt_msg(msg, shift):
                    self.add_to_inventory(player)
                    print("You witness the staff glow blue and proceed to slide it out from the stone")
                else: 
                    player.early_death("You failed to solve the riddle and the hexxed staff struck you down from the heavens")

        else:   
            print(f"You discover a {self.item.name} and insert it into your inventory")
            print(f"Description: {self.item.description}")

class North(InteractionS):
    def __init__(self):
        super().__init__((f"""You feel the air growing colder as you ascend the mountain\nAs you reach a narrow ledge, you spot a shimmering object in the distance...\nIt is the staff of Hermes, \nit is embedded into a stone. To retrieve it, you must solve a riddle carved into the rock.\nAs you reach for your knife to engrave your answer, you notice a small message embedded into the stone "{csrShift(shift, characters)} - 2"..."""),
        None,
        staff_of_hermes)
        
    def enter(self, player):
        super().enter(player)
        self.item_interaction(player)
        
#class West(Scene):
    #def __init__(self):
        #Scene.__init__(self, "You head west, your visibility worsening as you walk foward.")
    #def enter(self, player):
        #super().enter(player)

#class East(Scene):
    #def __init__(self):
        #Scene.__init__(self, "You head east, the air growing colder as you approach the glaccier.")
    #def enter (self, player):
        #super().enter(player)