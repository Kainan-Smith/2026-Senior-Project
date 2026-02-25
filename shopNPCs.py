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
newSword.price = 125
newSword.amount = 1

newerSword = ShopItem()
newerSword.name = "Newer Sword"
newerSword.price = 200
newerSword.amount = 1

world1Items = [
    healthPotion, manaPotion, bomb, repel
]

world2Items = [
    healthPotion, manaPotion, bomb, repel, levelUpPotion, newSword
]
    
def displayShop(shopItems):
    print(f"{'Item' :<20}{'Price' :<8}{'Amount' :<8}")
    print("=" * 34)
    for item in range(len(shopItems)):
        print(f"{shopItems[item][0] :<20}{'$' + str(shopItems[item][1]) :<8}{shopItems[item][2] :<8}")

def openShop(world):
    if world == 1:
        displayShop(world1Items)
    if world == 2:
        displayShop(world2Items)

world = int(input())

openShop(world)