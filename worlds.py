
import items
import evil
import combat
import character
import shop
import inventory
import quests
import travel

class World:
    def __init__(self):
        self.value = 0
        self.name = ""
        self.desc = ""
        self.shop = items.allItems
        self.shopName = ""              # Shopkeeper's Name
        self.enemy = evil.testDummy

world1 = World()
world1.value = 1
world1.name = "Planet Name 1"
world1.desc = "An adverb adjective world with noun 1"
world1.shop = items.area1Items
world1.shopname = "Stoobert"
world1.enemy = evil.goblin

world2 = World()
world2.value = 2
world2.name = "Planet Name 2"
world2.desc = "An adverb adjective world with noun 2"

world3 = World()
world3.value = 3
world3.name = "Planet Name 3"
world3.desc = "An adverb adjective world with noun 3"

world4 = World()
world4.value = 4
world4.name = "Planet Name 4"
world4.desc = "An adverb adjective world with noun 4"

world5 = World()
world5.value = 5
world5.name = "Planet Name 5"
world5.desc = "An adverb adjective world with noun 5"

world6 = World()
world6.value = 6
world6.name = "Planet Name 6"
world6.desc = "An adverb adjective world with noun 6"

world7 = World()
world7.value = 7
world7.name = "Planet Name 7"
world7.desc = "An adverb adjective world with noun 7"

world8 = World()
world8.value = 8
world8.name = "Planet Name 8"
world8.desc = "An adverb adjective world with noun 8"

allWorlds = [
    world1, world2, world3, world4, world5, world6, world7, world8
]

def sleep_at_inn(hero):
    hero.currentHealth = hero.maxHealth
    hero.currentMana = hero.maxMana
    print(f"You wake up feeling very refreshed! \n(Health filled to {hero.currentHealth} and Mana filled to {hero.currentMana})")

def arrive(world, hero):
    print(f"Welcome to {world.name}!")
    print(world.desc)
    while True:
        playerChoice = input("Talk, Rest, Fight, Shop, Inventory, Quests, Stats, or Travel? ").title()
        if playerChoice == "Talk":
            continue
        elif playerChoice == "Rest":
            sleep_at_inn(hero)
        elif playerChoice == "Fight":
            while True:
                combat.combat_loop(hero, world.enemy)
                if hero.currentHealth <= 0:
                    print("You black out suddenly and a nearby traveller carries you to the closest Inn...")
                    sleep_at_inn(hero)
                    break
                choice2 = input("Fight again? (1: Yes  0: No)").title()
                if choice2 == "1" or choice2 == "Yes":
                    choice2 = 0
                else:
                    break
        elif playerChoice == "Shop":
            shop.start_shopping(world, hero.money)
        elif playerChoice == "Inventory":
            inventory.display_inentory(hero)
        elif playerChoice == "Quests":
            quests.add_quest(hero, world)
        elif playerChoice == "Stats":
            pass
        elif playerChoice == "Travel":
            # Fix Combat and Quests not changing when travelling.
            travel.go_to_new_place(hero)
arrive(world1, character.hero)