# TODO: Do something about the consumables, look at the assignmnt details to see what is required.

class Item:
    ''' The Item class describes items that can be found in Shops or the player's Inventory. '''
    def __init__(self):
        self.name = ""      # The name of the item.
        self.price = 0      # The cost of the item in a shop.
        self.amount = 0     # The amount of the item sold in a shop.
        self.held = 0       # The amount of the item the player is holding.
        self.number = 0     # The number associated with the item, either Attack Modifier, Defense Modifier, or Healing.
        self.desc = ""      # A brief description of the item.
        self.weapon = False
        self.staff = False


basicSword = Item()
basicSword.name = "Basic Sword"
basicSword.held = 1
basicSword.amount = 1
basicSword.number = 15
basicSword.desc = "A basic sword..."
basicSword.weapon = True

newSword = Item()
newSword.name = "New Sword"
newSword.price = 150
newSword.amount = 1
newSword.number = 20
newSword.desc = "A new sword."
newSword.weapon = True

newerSword = Item()
newerSword.name = "Newer Sword"
newerSword.price = 200
newerSword.amount = 1
newerSword.number = 40
newerSword.desc = "A newer sword!"
newerSword.weapon = True

newestSword = Item()
newestSword.name = "Newest Sword"
newestSword.price = 250
newestSword.amount = 1
newestSword.number = 80
newestSword.desc = "The newest sword !!"
newestSword.weapon = True

basicStaff = Item()
basicStaff.name = "Basic Staff"
basicStaff.held = 1
basicStaff.amount = 1
basicStaff.number = 1
basicStaff.desc = "A basic staff..."
basicStaff.staff = True

newStaff = Item()
newStaff.name = "New Staff"
newStaff.price = 150
newStaff.amount = 1
newStaff.number = 1.25
newStaff.desc = "A new staff."
newStaff.staff = True

newerStaff = Item()
newerStaff.name = "Newer Staff"
newerStaff.price = 200
newerStaff.amount = 1
newerStaff.number = 1.5
newerStaff.desc = "A newer staff!"
newerStaff.staff = True

newestStaff = Item()
newestStaff.name = "Newest Staff"
newestStaff.price = 250
newestStaff.amount = 1
newestStaff.number = 2
newestStaff.desc = "The newest staff !!"
newestStaff.staff = True


hawkTalon = Item()
hawkTalon.name = "Hawk Talon"

wolfClaw = Item()
wolfClaw.name = "Wolf Claw"

goblinEye = Item()
goblinEye.name = "Goblin Eye"

skull = Item()
skull.name = "Skull"

orcFang = Item()
orcFang.name = "Orc Fang"

golemHead = Item()
golemHead.name = "Golem Head"

wyrmTooth = Item()
wyrmTooth.name = "Wyrm Tooth"

demonWing = Item()
demonWing.name = "Demon Wing"

finalBossKey = Item()
finalBossKey.name = "Mysterious Key"

questItems = [
    wolfClaw, hawkTalon, goblinEye, skull, orcFang, golemHead, wyrmTooth, demonWing
]

area1Items = [
    newSword, newStaff
]

area2Items = [
    newSword, newStaff
]

area3Items = [
    newSword, newStaff
]

area4Items = [
    newerSword, newerStaff
]

area5Items = [
    newerSword, newerStaff
]

area6to8Items = [
    newestSword, newestStaff
]

allItems = [
    wolfClaw, hawkTalon, goblinEye, skull, orcFang, golemHead, wyrmTooth, demonWing
]

weaponsAndStaffs = [
    newSword, newerSword, newestSword, newStaff, newerStaff, newestStaff
]