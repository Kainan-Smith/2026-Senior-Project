import items
import evil
import combat
import character
import shop
import inventory
import quests

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
world1.name = "Greenhaven (1)"
world1.desc = "The largest city in the world, known for its lush fauna and diverse ecosystem."
world1.shop = items.area1Items
world1.shopName = "Mira"
world1.enemy = evil.wolf

world2 = World()
world2.value = 2
world2.name = "Westbarrow (2)"
world2.desc = "A small village known mostly as a midpoint between GreenHhaven and Thornhollow."
world2.shopName = "Dorian"
world2.shop = items.area2Items
world2.enemy = evil.hawk

world3 = World()
world3.value = 3
world3.name = "Thornhollow (3)"
world3.desc = "A city to the North of the Western Plains."
world3.shopname = "Stoobert"
world3.shop = items.area3Items
world3.enemy = evil.goblin

world4 = World()
world4.value = 4
world4.name = "Thornhollow Catacombs (4)"
world4.desc = "Dank cave systems just outside of Thornhollow, it's said to hold the tomb of the founder of the village."
world4.shopName = "Earl the Grey"
world4.shop = items.area4Items
world4.enemy = evil.skeleton

world5 = World()
world5.value = 5
world5.name = "Dewpoint (5)"
world5.desc = "A small town on the outskirts of the snowy mountains."
world5.shopName = "Kael"
world5.shop = items.area5Items
world5.enemy = evil.orc

world6 = World()
world6.value = 6
world6.name = "Highwind Pass (6)"
world6.desc = "A village deep in the heart of the Northern Mountains."
world6.shopName = "Garett (Short for Cigarette)"
world6.shop = items.area6to8Items
world6.enemy = evil.golem

world7 = World()
world7.value = 7
world7.name = "Dunewatch (7)"
world7.desc = "A large city in the center of the Eastern Desert."
world7.shopName = "Victor"
world7.shop = items.area6to8Items
world7.enemy = evil.wyrm

world8 = World()
world8.value = 8
world8.name = "Hell's Maw (8)"
world8.desc = "A manmade canyon designed to guard King Averitt's palace."
world8.shopName = "Jarl"
world8.shop = items.area6to8Items
world8.enemy = evil.demon

world9 = World()
world9.value = 9
world9.name = "Corrupted King's Palace (9)"
world9.desc = "Final Boss"

world0 = World()
world0.value = 0
world0.name = "Dev Area"
world0.desc = "Dev Area"

allWorlds = [
    world1, world2, world3, world4, world5, world6, world7, world8, world9, world0
]

def check_worlds(currentArea):
    #   Uses the availableWorlds variable to determine which areas the player can travel to.
    availableWorlds = []
    if currentArea == world1:
        availableWorlds = [world2, world4]
    elif currentArea == world2:
        availableWorlds = [world1, world3, world5]
    elif currentArea == world3:
        availableWorlds = [world2, world4]
    elif currentArea == world4:
        availableWorlds = [world1, world3, world5, world7]
    elif currentArea == world5:
        availableWorlds = [world2, world4, world6]
    elif currentArea == world6:
        availableWorlds = [world6, world7]
    elif currentArea == world7:
        availableWorlds = [world4, world6, world8]
    elif currentArea == world8:
        availableWorlds = [world7, world9]
    elif currentArea == world0:
        availableWorlds = [world1, world2, world3, world4, world5, world6, world7, world8]
    if currentArea != world0 and character.hero.name == "Chris Bar":
        availableWorlds.append(world0)
    return availableWorlds

def go_to_new_place(hero, allWorlds):
    # place variable is where you currently are
    moving = False
    available = check_worlds(hero.currentWorld)
    numAvail = len(available)
    if len(hero.visitedWorlds) > 0:
        print("Type \"Cancel\" to go back.")
        print("World(s) you've visited: ", end="")
        if len(hero.visitedWorlds) > 1:
            for count in range(len(hero.visitedWorlds) - 1):
                print(f"{hero.visitedWorlds[count].name}, ", end="")
            print(f"and {hero.visitedWorlds[-1].name}")
        else:
            print(hero.visitedWorlds[0].name)
    while moving == False:
        print("Would you like to go to ", end="")
        if numAvail > 2:
            for count in range(numAvail - 1):
                print(f"{available[count].name}, ", end="")
            print(f"or {available[-1].name}?")
        elif numAvail == 1:
            print(f"{available[0].name}?")
        else:
            print(f"{available[0].name} or {available[1].name}?")
        while True:
                playerSelection = input()
                if playerSelection.isdigit():
                    playerSelection = int(playerSelection)
                    break
                else:
                    playerSelection = playerSelection.title()
                    if playerSelection == "Cancel":
                        return
        worldChecked = allWorlds[playerSelection - 1]
        if worldChecked not in available:
            print(worldChecked.name, "not available.")
            continue
        print("Traveling to", playerSelection, "now.")
        moving = True
    newPlace = worldChecked
    hero.visitedWorlds.append(hero.currentWorld)
    hero.currentWorld = newPlace

def sleep_at_inn(hero):
    hero.currentHealth = hero.maxHealth
    hero.currentMana = hero.maxMana
    print(f"You wake up feeling very refreshed! \n(Health filled to {hero.currentHealth} and Mana filled to {hero.currentMana})")

def arrive(hero):
    if hero.currentWorld == None:
        hero.currentWorld = world1
    print(f"Welcome to {hero.currentWorld.name}!")
    print(hero.currentWorld.desc)
    while True:
        if hero.currentWorld == world0:
            hero.vitality = int(input())
            hero.arcana = int(input())
            hero.strength = int(input())
            hero.intelligence = int(input())
            hero.endurance = int(input())
        if hero.currentWorld == world5 and evil.gargoyle.defeated == False:
            combat.combat_loop(hero, evil.gargoyle)
        if hero.currentWorld == world9:
            if items.finalBossKey.held == 0:
                print("Bad Ending")
                print("You reached the Corrupted King's palace, but you can't get in.  (Try doing all the quests next time)")
                break
            else:
                combat.combat_loop(hero, evil.king)
        playerChoice = input("Talk, Rest, Fight, Shop, Inventory, Quests, Stats, or Travel? ").title()
        if playerChoice == "Rest":
            sleep_at_inn(hero)
        elif playerChoice == "Fight":
            while True:
                combat.combat_loop(hero, hero.currentWorld.enemy)
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
            shop.start_shopping(hero.currentWorld, hero.money)
        elif playerChoice == "Inventory":
            inventory.display_inentory(hero)
        elif playerChoice == "Quests":
            quests.add_quest(hero, hero.currentWorld)
        elif playerChoice == "Stats":
            character.print_stats(hero)
            print("-" * 30)
            character.check_modifiers(hero)
            character.print_modifiers(hero)
        elif playerChoice == "Travel":
            # Fix Combat and Quests not changing when travelling.
            go_to_new_place(hero, allWorlds)