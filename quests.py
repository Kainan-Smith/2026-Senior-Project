import items

class Quest:
    def __init__(self):
        self.questName = ""
        self.item = None
        self.needed = 0

world1Quest = Quest()
world1Quest.quest.name = "Stupid Dog"
world1Quest.item = items.wolfClaw
world1Quest.needed = 8

world2Quest = Quest()
world2Quest.quest.name = "Birdbrain"
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