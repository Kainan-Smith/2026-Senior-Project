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

healthPotion = Item()
healthPotion.name = "Health Potion"
healthPotion.held = 1
healthPotion.price = 25
healthPotion.amount = 5
healthPotion.number = 20
healthPotion.desc = f"Heals {healthPotion.number} HP."

manaPotion = Item()
manaPotion.name = "Mana Potion"
manaPotion.held = 1
manaPotion.price = 25
manaPotion.amount = 5
manaPotion.number = 20
manaPotion.desc = f"Recovers {manaPotion.number} MP."

bomb = Item()
bomb.name = "Bomb"
bomb.price = 50
bomb.amount = 3
bomb.number = 25
bomb.desc = f"Deals {bomb.number} damage when thrown at an enemy."

repel = Item()
repel.name = "Repel"
repel.price = 100
repel.amount = 2
repel.number = "N/A"
repel.desc = "Skips next encounter."

experiencePotion = Item()
experiencePotion.name = "Experience Potion"
experiencePotion.price = 100
experiencePotion.amount = 2
experiencePotion.number = "N/A"
experiencePotion.desc = "Levels up your character 1 time."

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

area1Items = [
    healthPotion, bomb
]

area2Items = [
    healthPotion, manaPotion, bomb, repel
]

area3Items = [
    healthPotion, manaPotion, bomb, repel, experiencePotion
]

area4Items = [
    healthPotion, manaPotion, bomb, repel, experiencePotion, newSword, newStaff
]

area5Items = [
    healthPotion, manaPotion, bomb, repel, experiencePotion, newerSword, newerStaff
]

area6to8Items = [
    healthPotion, manaPotion, bomb, repel, experiencePotion, newestSword, newestStaff
]

allItems = [
    healthPotion, manaPotion, bomb, repel, experiencePotion
]

weaponsAndStaffs = [
    newSword, newerSword, newestSword, newStaff, newerStaff, newestStaff
]


hawkTalon = Item()
hawkTalon.name = "Hawk Talon"

direWolfClaw = Item()
direWolfClaw.name = "Dire Wolf Claw"

goblinEye = Item()
goblinEye.name = "Goblin Eye"

skeletonSkull = Item()
skeletonSkull.name = "Skeleton Skull"

orcFang = Item()
orcFang.name = "Orc Fang"

golemHead = Item()
golemHead.name = "Golem Head"

wyrmTooth = Item()
wyrmTooth.name = "Wyrm Tooth"

demonWing = Item()
demonWing.name = "Demon Wing"