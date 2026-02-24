# These lists consist of the item's name, price, and quantity in the shop
healthPotion = [
    "Health Potion", 25, 5
]
manaPotion = [
    "Mana Potion", 25, 5
]

class ShopNPCs:
    def __init__(self):
        self.itemsInShop = {"Health Potion": [25, 5], "Mana Potion": 25, "Bomb": 50, "Repel": 100, "Level-Up Potion": 200}

world1Shop = ShopNPCs
world2Shop = ShopNPCs
world3Shop = ShopNPCs
world4Shop = ShopNPCs
world5Shop = ShopNPCs
world6Shop = ShopNPCs
world7Shop = ShopNPCs
world8Shop = ShopNPCs

def openShop(world):
    pass
    if world == 1:
        for item in range(len(world1Items)):
            shopItem = list(world1Items.keys())[item]
            price = list(world1Items.values())[item]
            print(f"Item: {world1Items}")