# These lists consist of the item's name, price, and quantity in the shop
healthPotion = [
    "Health Potion", 25, 5
]

healthPotion = ShopItem():
healthPotion.name = "Health Potion"
h

manaPotion = [
    "Mana Potion", 25, 5
]

bomb = [
    "Bomb", 50, 3
]

repel = [
    "Repel", 100, 2
]

levelUpPotion = [
    "Level-Up Potion", 100, 1
]

newSword = [
    "New Sword", 125, 1
]

newerSword = [
    "Newer Sword", 200, 1
]

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