class CharacterA:

    # init method or constructor
    def __init__(self, skill_class, name):
        self.skill_class = skill_class
        self.name = name

    # Sample Method
    def introcution(self):
        print('Hello, my name is', self.name)
        print('I am a', self.skill_class)
# Creating different objects
c1 = CharacterA('Mage', 'A')
c1.introcution()

class CharacterA:
    # init method or constructor
    def __init__(self, skill_class, name):
        self.skill_class = skill_class
        self.name = name
    # Sample Method
    def introcution(self):
        print('Hello, my name is', self.name)
        print('I am a', self.skill_class)

c2 = CharacterA('Warrior', 'B')
c2.introcution()