class ShopItem:
    '''The ShopItem class makes a template for items that will appear in the shop'''
    def __init__(self):
        self.name = ""
        self.price = 0
        self.amount = 0

healthPotion = ShopItem()
healthPotion.name = "Health Potion"
healthPotion.price = 25
healthPotion.amount = 5

manaPotion = ShopItem()
manaPotion.name = "Mana Potion"
manaPotion.price = 25
manaPotion.amount = 5

bomb = ShopItem()
bomb.name = "Bomb"
bomb.price = 50
bomb.amount = 3

repel = ShopItem()
repel.name = "Repel"
repel.price = 100
repel.amount = 2

levelUpPotion = ShopItem()
levelUpPotion.name = "Level-Up Potion"
levelUpPotion.price = 100
levelUpPotion.amount = 2

newSword = ShopItem()
newSword.name = "New Sword"
newSword.price = 150
newSword.amount = 1

newerSword = ShopItem()
newerSword.name = "Newer Sword"
newerSword.price = 200
newerSword.amount = 1

newestSword = ShopItem()
newestSword.name = "Newest Sword"
newestSword.price = 250
newestSword.amount = 1

area1Items = [
    healthPotion, bomb
]

area2Items = [
    healthPotion, manaPotion, bomb, repel
]

area3Items = [
    healthPotion, manaPotion, bomb, repel, levelUpPotion
]

area4Items = [
    healthPotion, manaPotion, bomb, repel, levelUpPotion, newSword
]

area5Items = [
    healthPotion, manaPotion, bomb, repel, levelUpPotion, newerSword
]

area6to8Items = [
    healthPotion, manaPotion, bomb, repel, levelUpPotion, newestSword
]

devAreaItems = [
    healthPotion, manaPotion, bomb, repel, levelUpPotion, newSword, newerSword, newestSword
]

def displayShop(shopItems):
    print(f"{'Item' :<20}{'Price' :<8}{'Amount' :<8}")
    print("=" * 34)
    for item in range(len(shopItems)):
        print(f"{shopItems[item].name :<20}{'$' + str(shopItems[item].price) :<8}{shopItems[item].amount :<8}")

def openShop(area):
    if area == 1:
        displayShop(area1Items)
    elif area == 2:
        displayShop(area2Items)
    elif area == 3:
        displayShop(area3Items)
    elif area == 4:
        displayShop(area4Items)
    elif area == 5:
        displayShop(area5Items)
    elif area == 6 or area == 7 or area == 8:
        displayShop(area6to8Items)
    elif area == 0:
        displayShop(devAreaItems)

area = int(input())

openShop(area)