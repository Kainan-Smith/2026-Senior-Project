class InventoryAndShopItem:
    ''' The InventoryAndShopItem class describes items that can be found in Shops or the player's Inventory. '''
    def __init__(self):
        self.name = ""      # The name of the item.
        self.price = 0      # The cost of the item in a shop.
        self.amount = 0     # The amount of the item sold in a shop.
        self.held = 0       # The amount of the item the player is holding
        self.number = 0     # The number associated with the item, either Attack Modifier, Defense Modifier, or Healing.
        self.desc = ""      # A brief description of the item

healthPotion = InventoryAndShopItem()
healthPotion.name = "Health Potion"
healthPotion.price = 25
healthPotion.amount = 5
healthPotion.number = 20
healthPotion.desc = f"Heals {healthPotion.number} HP."

manaPotion = InventoryAndShopItem()
manaPotion.name = "Mana Potion"
manaPotion.price = 25
manaPotion.amount = 5
manaPotion.number = 20
manaPotion.desc = f"Recovers {manaPotion.number} MP."

bomb = InventoryAndShopItem()
bomb.name = "Bomb"
bomb.price = 50
bomb.amount = 3
bomb.number = 25
bomb.desc = f"Deals {bomb.number} damage when thrown at an enemy."

repel = InventoryAndShopItem()
repel.name = "Repel"
repel.price = 100
repel.amount = 2
repel.number = "N/A"
repel.desc = "Skips next encounter."

experiencePotion = InventoryAndShopItem()
experiencePotion.name = "Experience Potion"
experiencePotion.price = 100
experiencePotion.amount = 2
experiencePotion.number = "N/A"
experiencePotion.desc = "Levels up your character 1 time."

newSword = InventoryAndShopItem()
newSword.name = "New Sword"
newSword.price = 150
newSword.amount = 1
newSword.number = 15
newSword.desc = "A new sword."

newerSword = InventoryAndShopItem()
newerSword.name = "Newer Sword"
newerSword.price = 200
newerSword.amount = 1
newerSword.number = 20
newerSword.desc = "A newer sword!"

newestSword = InventoryAndShopItem()
newestSword.name = "Newest Sword"
newestSword.price = 250
newestSword.amount = 1
newestSword.number = 25
newestSword.desc = "The newest sword !!"

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
    healthPotion, manaPotion, bomb, repel, experiencePotion, newSword
]

area5Items = [
    healthPotion, manaPotion, bomb, repel, experiencePotion, newerSword
]

area6to8Items = [
    healthPotion, manaPotion, bomb, repel, experiencePotion, newestSword
]

allItems = [
    healthPotion, manaPotion, bomb, repel, experiencePotion, newSword, newerSword, newestSword
]