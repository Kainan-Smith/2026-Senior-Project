import items

def displayInventory():
    # Prints the table view of the inventory.
    print(f"{'Item' :<20}{'Held' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 28}{'|'}{'=' * 40}")
    for item in range(len(items.allItems)):
        if items.allItems[item].held > 0:
            print(f"{items.allItems[item].name :<20}{items.allItems[item].held :<8}{'|' :<8}{shopArea[item].desc :<32}")

money = 100

displayInventory()