import items

class Quest:
    def __init__(self):
        self.questName = ""
        self.item = None
        self.needed = 0

world3Quest = Quest()
world3Quest.questName = "Goblin Grabber"
world3Quest.item = items.goblinEye
world3Quest.needed = 8