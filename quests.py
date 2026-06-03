import items

def show_quests(questList):
    print("-" * 20)
    for quest in questList:
        print(f"{quest.questName}:")
        print(f"{quest.item.name:<20}{quest.item.held}/{quest.needed:<8}")
        print("-" * 20)

def add_quest(hero, world):
    for item in allQuests:
        if item.world == world.value:
            if item not in hero.questList:
                hero.questList.append(item)
    show_quests(hero.questList)

# WORLD 8 CAN'T TRAVEL

class Quest:
    def __init__(self):
        self.questName = ""
        self.item = None
        self.needed = 0
        self.completed = False
        self.world = 0

world1Quest = Quest()
world1Quest.questName = "Stupid Dog (1)"
world1Quest.item = items.wolfClaw
world1Quest.needed = 8
world1Quest.world = 1

world2Quest = Quest()
world2Quest.questName = "Birdbrain (2)"
world2Quest.item = items.hawkTalon
world2Quest.needed = 8
world2Quest.world = 2

world3Quest = Quest()
world3Quest.questName = "I'm a Goblin! (3)"
world3Quest.item = items.goblinEye
world3Quest.needed = 8
world3Quest.world = 3

world4Quest = Quest()
world4Quest.questName = "Mind-Boggling Effects (4)"
world4Quest.item = items.skull
world4Quest.needed = 8
world4Quest.world = 4

world5Quest = Quest()
world5Quest.questName = "Gort (5)"
world5Quest.item = items.orcFang
world5Quest.needed = 8
world5Quest.world = 5

world6Quest = Quest()
world6Quest.questName = "Basin' It (6)"
world6Quest.item = items.golemHead
world6Quest.needed = 8
world6Quest.world = 6

world7Quest = Quest()
world7Quest.questName = "Straight Teeth (7)"
world7Quest.item = items.wyrmTooth
world7Quest.needed = 8
world7Quest.world = 7

world8Quest = Quest()
world8Quest.questName = "Die (8)"
world8Quest.item = items.demonWing
world8Quest.needed = 8
world8Quest.world = 8

allQuests = [
    world1Quest, world2Quest, world3Quest, world4Quest, world5Quest, world6Quest, world7Quest, world8Quest
]