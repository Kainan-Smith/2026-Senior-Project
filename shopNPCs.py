import items
import travel
import inventory 

def displayShop(shopArea):
    print(f"{'Item' :<20}{'Price' :<8}{'Amount' :<8}{'Held' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 44}{'|'}{'=' * 50}")
    for item in range(len(shopArea)):
        print(f"{shopArea[item].name :<20}{'$' + str(shopArea[item].price) :<8}{shopArea[item].amount :<8}{shopArea[item].held :<8}{'|' :<8}{shopArea[item].desc :<32}")

def checkShop(area):
    if area == 1:
        shopArea = items.area1Items
    elif area == 2:
        shopArea = items.area2Items
    elif area == 3:
        shopArea = items.area3Items
    elif area == 4:
        shopArea = items.area4Items
    elif area == 5:
        shopArea = items.area5Items
    elif area == 6 or area == 7 or area == 8:
        shopArea = items.area6to8Items
    elif area == 0:
        shopArea = items.allItems
    return shopArea

def startShopping(area, money):
    playerChoice = ""
    itemList = checkShop(area)
    print('"Welcome to my shop!"')
    while playerChoice != "Leave":
        print("Enter an item's name to purchase it or type 'Leave' to exit the shop.")
        print(f"You have ${money}")
        displayShop(itemList)
        playerChoice = input().title()
        for item in itemList:
            if item.name == playerChoice:
                if item.price > money:
                    print("You don't have enough money.")
                    break
                item.amount -= 1
                item.held += 1
                money -= item.price
                print(f"{playerChoice} purchased for ${item.price}.  You have ${money} remaining.")
    print("Enjoy!")

area = travel.currentPlace

startShopping(area, inventory.money)