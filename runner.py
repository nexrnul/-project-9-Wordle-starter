from character import create_player
from item import Item
from player import Player
from puzzle import encrypt_msg
from scene import Scene, North, West, East, InteractionS, TravelS


player = create_player()

staff_of_hermes = Item(
    name="Staff of Hermes",
    description="A mystical staff that holds great power, but retrieving it requires solving an ancient riddle. You consider yourself quite lucky today as items of such caliber usually hold dangerous hexes to ward of thieves",
    is_special=True)

aetheric_compass = Item(
    name="Aetheric Compass",
    descritpion="ancient navigational device that guides the user through the currents of magic, revealing hidden paths and realms.",
    is_special=False)

mythril_sword = Item (
    name = "Mythril Sword",
    description = "Forged from rare mythril metal, this sword has a lightweight feel while being incredibly powerful. Its blade has a blue glow when within the hands of the virtuous.",
    is_special=True)

into_lore = "\nYou are an adventurer travelling the realm of Gelidria, the frostbitten tundra.\nYou have been tasked with discovering the Cosmic Egg, a relic said to hold the secrets of the universe.\nArmed with nothing but your skills, you set forth on your journey.\nAs you stand in front of a cold and still forest, the path before you splits into three directions"
destinations = ["North"]

intro_scene = TravelS(into_lore, destinations)

while True:
    intro_scene.enter(player)
    choice = input("\nYou may head north towards the mountains").lower()
    #,n\ncontinue west entering the forest,
    #or travel east towards the glacier."
    #input(TravelS)
    if choice in ("n", "north"):
        north_scene = North()
        north_scene.enter(player)
        
    #elif choice in ("w", "west"):
        #west_scene = West()
        #west_scene.enter(player)

    #elif choice in ("e", "east"):
        #east_scene = East()
        #east_scene.enter(player)