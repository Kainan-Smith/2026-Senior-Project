import items
currentWeapon = items.basicSword
currentStaff = items.basicStaff
money = 500

def displayInventory():
    # Prints the table view of the inventory.
    print(f"{'Item' :<20}{'Held' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 28}{'|'}{'=' * 40}")
    for item in range(len(items.allItems)):
        if items.allItems[item].held > 0:
            print(f"{items.allItems[item].name :<20}{items.allItems[item].held :<8}{'|' :<8}{items.allItems[item].desc :<32}")
    global money
    print(f"Money: {money}")
    global currentWeapon
    print(f"Current Weapon: {currentWeapon.name}")
    global currentStaff
    print(f"Current Staff: {currentStaff.name}")
    answer = input("Change Weapons? (Yes or No) ").title()
    if answer == "Yes":
        weaponChange = False
        while weaponChange == False:
            newWeapon = input("Select New Weapon: ").title()
            for item in items.allItems:
                if item.name == newWeapon and item.weapon == True:
                    currentWeapon = item
                    print(currentWeapon.name)
                    weaponChange = True
    answer = input("Change Staff? (Yes or No) ").title()
    if answer == "Yes":
        staffChange = False
        while staffChange == False:
            newStaff = input("Select New Staff: ").title()
            for item in items.allItems:
                if item.name == newStaff and item.staff == True:
                    currentStaff = item
                    print(currentStaff.name)
                    staffChange = True

