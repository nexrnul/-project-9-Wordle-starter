class Character:

    # init method or constructor
    def __init__(self, skill_class, name, strength, health, exp=1):
        self.skill_class = skill_class
        self.name = name
        self.health = health
        self.exp = exp
        self.strength = strength

    def introduction(self):
        print(f"My name is {self.name} and I am a {self.skill_class}")

    def attack(self):
        print(f"{self.name} attacks for {self.strength*10} damage!")

# Creating different objects


class Mage(Character):
    def __init__(self, name, strength=8, health=60, exp=1):
        super().__init__('Mage', name, strength, health, exp)


class Ranger(Character):


class Cleric(Character):


c1 = Character('Mage', 'A', 8, 60)
c2 = Character('Ranger', 'B', 6, )
c3 = Character('Cleric', 'C', 4, )
c1.introduction()
c2.introduction()
c3.introduction()
