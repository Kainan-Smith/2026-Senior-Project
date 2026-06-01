
import items
import evil
import combat
import character
import shop
import inventory

class World:
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.shop = items.allItems
        self.shopName = ""              # Shopkeeper's Name
        self.enemies = []

world1 = World()
world1.name = "Planet Name 1"
world1.desc = "An adverb adjective world with noun 1"
world1.shop = items.area1Items
world1.shopname = "Stoobert"
world1.enemy = evil.goblin

def 

def arrive(world):
    print(f"Welcome to {world.name}!")
    print(world.desc)
    while True:
        playerChoice = input("Talk, Fight, Shop, Inventory, Quests, or Travel? ").title()
        if playerChoice == "Talk":
            continue
        elif playerChoice == "Fight":
            while True:
                combat.combat_loop(character.hero, world1.enemy)
                choice2 = input("Fight again? (1: Yes  0: No)").title()
                if choice2 == "1" or choice2 == "Yes":
                    choice2 = 0
                else:
                    break
        elif playerChoice == "Shop":
            shop.start_shopping(world, character.hero.money)
        elif playerChoice == "Inventory":
            inventory.display_inentory(character.hero)
        elif playerChoice == "Quests":
            pass
        elif playerChoice == "Travel":
            pass
arrive(world1)