import items

class Quest:
    def __init__(self):
        self.questName = ""
        self.item = None
        self.needed = 0

world2Quest = Quest()
world2Quest.questName = "Goblin Grabber"
world2Quest.item = items.goblinEye