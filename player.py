class Player:
    def __init__(self, name, skill_class):
        self.name = name
        self.skill_class = skill_class
        self.health = 0
        self.strength = 0
        self.inventory = []
    
    def pick_up_item(self, item):
        print("You attained a", item.name)
        self.inventory.append(item)
        
#class Character:
    #def __init__(self, skill_class, name, strength, health, inventory, exp_rate, exp=1):

    def attack(self):
      print(f"{self.name} attacks for {self.strength*10} damage!")

    def take_damage(self, damage):
      self.health -= damage
      if self.health <= 0:
          print(f"{self.name} has been defeated!")
      else:
          print(f"{self.name} has {self.health} health remaining.")

    def add_to_inventory(item):
        inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def show_inventory():
        print("Your current inventory: ", ", ".join(inventory))

    def use_item(item):
        if item in inventory:
            print(f"You use the {item}.")
            inventory.remove(item)
        else:
            print(f"You don't have {item} in your inventory.")