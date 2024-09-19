class Player:
#Mostly unused code which was initally intended to be implemented-    
    def __init__(self, name, skill_class):
        self.name = name
        self.skill_class = skill_class
        self.health = 100
        self.strength = 10
        self.inventory = []
    
    def pick_up_item(self, item):
        print("You attained a", item.name)
        self.inventory.append(item)
    
    #Death trigger
    def early_death(self, message):
        print(f"{message}\nYOU DIED")
        exit()
        
    def attack(self):
        print(f"{self.name} attacks for {self.strength*10} damage!")

    def take_damage(self, damage):
      self.health -= damage
      if self.health <= 0:
        print(f"{self.name} has been defeated!")
        self.early_death("You have met your demise")
      else:
        print(f"{self.name} has {self.health} health remaining.")

    #CODY ASSISTED
    def show_inventory(self):
        print("Your current inventory: ", ", ".join([item.name for item in self.inventory]))

    def use_item(self, item):
        if item in self.inventory:
            print(f"You use the {item.name}.")
            self.inventory.remove(item)
        else:
            print(f"You don't have {item.name} in your inventory.")