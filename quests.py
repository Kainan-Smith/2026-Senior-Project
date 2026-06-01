import items

def show_quests(questList):
    for quest in questList:
        print(f"{quest.questName}:")
        print(f"{quest.item.name:<20}{quest.item.held}/{quest.needed:<8}")

def add_quest(hero, world):
    myList = hero.questList
    if world.value == 1:
        myList.append(world1Quest)
    elif world.value == 2:
        myList.append(world2Quest)
    elif world.value == 3:
        myList.append(world3Quest)
    elif world.value == 4:
        myList.append(world4Quest)
    elif world.value == 5:
        myList.append(world5Quest)
    elif world.value == 6:
        myList.append(world6Quest)
    elif world.value == 7:
        myList.append(world7Quest)
    elif world.value == 8:
        myList.append(world8Quest)
    hero.questList = list(set(myList))
    show_quests(hero.questList)

class Quest:
    def __init__(self):
        self.questName = ""
        self.item = None
        self.needed = 0
        self.completed = False

world1Quest = Quest()
world1Quest.questName = "Stupid Dog"
world1Quest.item = items.wolfClaw
world1Quest.needed = 8

world2Quest = Quest()
world2Quest.questName = "Birdbrain"
world2Quest.item = items.hawkTalon
world2Quest.needed = 8

world3Quest = Quest()
world3Quest.questName = "I'm a Goblin!"
world3Quest.item = items.goblinEye
world3Quest.needed = 8

world4Quest = Quest()
world4Quest.questName = "Mind-Boggling Effects"
world4Quest.item = items.skull
world4Quest.needed = 8

world5Quest = Quest()
world5Quest.questName = "Gort"
world5Quest.item = items.orcFang
world5Quest.needed = 8

world6Quest = Quest()
world6Quest.questName = "Basin' It"
world6Quest.item = items.golemHead
world6Quest.needed = 8

world7Quest = Quest()
world7Quest.questName = "Straight Teeth"
world7Quest.item = items.wyrmTooth
world7Quest.needed = 8

world8Quest = Quest()
world8Quest.questName = "Die"
world8Quest.item = items.demonWing
world8Quest.needed = 8