import items
currentWeapon = 0

def displayInventory():
    # Prints the table view of the inventory.
    print(f"{'Item' :<20}{'Held' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 28}{'|'}{'=' * 40}")
    for item in range(len(items.allItems)):
        if items.allItems[item].held > 0:
            print(f"{items.allItems[item].name :<20}{items.allItems[item].held :<8}{'|' :<8}{items.allItems[item].desc :<32}")
    print(f"Money: {money}")
    global currentWeapon
    print(f"Current Weapon: {currentWeapon}")
    answer = input("Change Weapons? (Yes or No) ").title()
    if answer == "Yes":
        weaponChange = False
        while weaponChange == False:
            newWeapon = input("Select New Weapon: ").title
            for item in items.allItems:
                if item.name == newWeapon and item.weapon:
                    currentWeapon = item
                    weaponChange == True
        displayInventory()

    

money = 500