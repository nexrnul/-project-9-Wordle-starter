from item import Item
from character import Character
from player import Player
from puzzle import Puzzle

class Scene:
#Scene class represents scene or place in game. 
 #enter() method is called when player enters the scene. 
 #sets the player reference and calls the describe() to print the scene description.
   def __init__(self, description):
       self.description = description

   def enter(self, player):
        self.player = player
        self.describe()
       
   def describe(self):
       print(self.description)

class IntroScene(Scene):
    def enter(self, player):
        print(self.description)
        choice = input("    do you wish to travel north, or continue foward (N/F)").upper()
        if choice == 'N':
            return "north"
        elif choice == 'F':
            return "forest"
        else:
            print("    Invalid choice, try again.")
            return(self.enter(player))
        
class NorthScene(Scene):
    def enter(self, player):
        print(self.description)
        choice = input("    Do you want to solve the riddle and retrieve the staff? (Y/N): ").upper()
        staff_of_hermes = Item(
            name="Staff of Hermes",
            description="A mystical staff that holds great power, but retrieving it requires solving an ancient riddle. You consider yourself quite lucky today as items of such caliber usually hold dangerous hexes to ward of thieves",
            is_special=True)
        if choice == 'Y':
            if self.solve_riddle(player) == True:
                print("     The staff glows blue as you pull it from the stone. You now possess the Staff of Hermes.")
                player.pick_up_item(staff_of_hermes)
                return "final"
            else:
                player.early_death("    You failed to solve the riddle, a powerful hex protecting the staff strikes you down from the heavens.")
                return "end"
        elif choice == 'N':
            print("     You decide to move forward, leaving the Staff of Hermes behind.")
            return "final"
        else:
            print("    Invalid choice, try again.")
            return self.enter(player)
    def solve_riddle(self, player):
        encrypted_msg = Puzzle.encrypt_msg("frozen", 2)
        msg = "frozen"
        if encrypted_msg == msg:
            return True
        else:
            return False

class ForestScene(Scene):
    def enter(self, player):
        print(self.description)
        choice = input("Do you want to (A)ttack or (D)efend?: ").upper()
        if choice == 'A':
            print("You attack the apparition.")
            self.attack_enemy(player)
        elif choice == 'D':
            print("You defend against the apparition's attack.")
            self.defend_enemy(player)
        else:
            print("    Invalid choice, try again.")
            return self.enter(player)
        return "final"

    def attack_enemy(self, player):
        if "    Mythril Sword" in player.inventory:
            print("    With the Mythril Sword, you swiftly strike into the apparition instantly defeating it.")
        else:
            player.early_death("    Without a proper weapon, the apparition overwhelms you.")
            return "end"

    def defend_enemy(self, player):
        print("     You atempt to defend, but the guardian is too strong.")
        player.take_damage(20)
        if player.health <= 0:
            player.early_death("    You couldn't hold off the guardian's assault.")
            return "end"

class FinalScene(Scene):
    def enter(self, player):
        print(self.description)
        if "Staff of Hermes" in player.inventory:
            print("    You wield the Staff of Hermes and cast a powerful spell, banishing the celestial mantid.")
            return self.game_won(player)
        elif "Mythril Sword" in player.inventory:
            print("    You engage the mantid with the Mythril Sword.")
            return self.fight_mantid(player)
        else:
            player.early_death("    lacking anything to defend yourself, the celestial mantid overpowers you and preys upon your soul.")
            return "end"

    def fight_mantid(self, player):
        choice = input("    Do you want to (A)ttack or (D)efend?: ").upper()
        if choice == 'A':
            print("    You attack the mantid.")
            if self.battle_outcome(success=True):
                return self.game_won(player)
            else:
                player.early_death("    The celestial mantid overpowers you.")
                return "end"
        elif choice == 'D':
            print("    You defend against the mantid's strikes, but it's futile.")
            player.take_damage(70)
            if player.health <= 0:
                player.early_death("    You couldn't hold off the celestial mantid.")
                return "end"
        else:
            print("    Invalid choice, try again.")
            return self.fight_mantid(player)

    def battle_outcome(self, success):
        #CODY ASSISTED
        from random import randint
        outcome = randint(0,1)
        if outcome == 1:
            print("""     With one final resounding blow, the celestial mantid fades into dust.
                          The chamber falls eerily silent...
                          Before you lays the Cosmic Egg rest upon a stone pedestal, its otherwordly glow leaves you overcome with wonder.
                          The relic is yours at last, the key towards untold knowledge of old.""")
            return True
        else: 
            return False

    def game_won(self, player):
  
        return "end"