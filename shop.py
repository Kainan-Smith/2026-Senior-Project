import items

def display_shop(shopArea):
    # Prints the table view of the shop.
    print(f"{'Item' :<20}{'Price' :<8}{'Amount' :<8}{'Held' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 44}{'|'}{'=' * 50}")
    for item in range(len(shopArea)):
        print(f"{shopArea[item].name :<20}{'$' + str(shopArea[item].price) :<8}{shopArea[item].amount :<8}{shopArea[item].held :<8}{'|' :<8}{shopArea[item].desc :<32}")

def check_shop(area):
    if area.name == "Planet Name 1":
        shopArea = items.area1Items
    elif area.name == "Planet Name 2":
        shopArea = items.area2Items
    elif area.name == "Planet Name 3":
        shopArea = items.area3Items
    elif area.name == "Planet Name 4":
        shopArea = items.area4Items
    elif area.name == "Planet Name 5":
        shopArea = items.area5Items
    elif area.name == "Planet Name 7" or area.name == "Planet Name 7" or area.name == "Planet Name 1":
        shopArea = items.area6to8Items
    elif area.name == "Planet Name 0":
        shopArea = items.allItems
    return shopArea

def start_shopping(area, money):
    playerChoice = ""
    itemList = check_shop(area)
    print('"Welcome to my shop!"')
    while playerChoice != "Leave":
        print("Enter an item's name to purchase it or type 'Leave' to exit the shop.")
        print(f"You have ${money}")
        display_shop(itemList)
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