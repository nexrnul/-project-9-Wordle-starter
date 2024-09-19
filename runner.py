from character import create_player
from item import Item
from player import Player
from puzzle import Puzzle
from scene import FinalScene, NorthScene, ForestScene, IntroScene, Scene


#function creates the player from player.py, initializes the game scenes, and runs main game loop.

#game scenes defined as dictionary, keys are scene names and values are Scene objects. 
def main():
    player = create_player()
    scenes = {
    "intro": IntroScene(""" 
    you are an adventurer travelling the realm of Gelidria, the frostbitten tundra.
    You have been tasked with discovering the Cosmic Egg, a relic said to hold the secrets of the universe.
    Armed with nothing but your wits and skills, you set forth on your journey.
    As you stand in front of a cold and still forest, the path before you splits into two directions"""),

    "north": NorthScene("""
    the air grows colder as you ascend the mountain. The path becomes narrow, and you see a shimmering object embedded in stone.
    It's the Staff of Hermes, but to retrieve it, you must solve a riddle carved into the rock: "HTQBGP - 2". """),

    "forest": ForestScene("""
    You venture deep into the forest, where the trees grow thicker and the air more oppressive.
    A shadowy figure looms ahead, blocking your path. It is a wandering apparition of the forest."""),

    "final": FinalScene("""
    After some days of uneventful travel you reach the final chamber, where the Cosmic Egg lies guarded by the celestial mantid.
    Its claws shimmer with an unnatural radiance, you find yourself stuck in a trance as it slowly advances closer. """)}
    #code represents main game loop for game. Starts the player in the "intro" scene, and then enters each scene, 
    #updating the current_scene variable with next scene to visit, until end scene is reached.
    #CODY ASSISTED
    current_scene = "intro"
    while current_scene != "end":
        scene = scenes[current_scene]
        next_scene = scene.enter(player)
        current_scene = next_scene
    print("game over")

if __name__ == "__main__":
    main()


#UNUSED ITEMS
aetheric_compass = Item(
    name="Aetheric Compass",
    description="ancient navigational device that guides the user through the currents of magic, revealing hidden paths and realms.",
    is_special=False)

mythril_sword = Item (
    name = "Mythril Sword",
    description = "Forged from rare mythril metal, this sword has a lightweight feel while being incredibly powerful. Its blade has a blue glow when within the hands of the virtuous.",
    is_special=True)

