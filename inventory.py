import items
import character


def update_weapon(char):
    for item in items.weaponsAndStaffs:
        if item.held > 0:
            if item.weapon == True:
                char.currentWeapon = item
            elif item.staff == True:
                char.currentStaff = item

def display_inentory(char):
    # Prints the table view of the inventory.
    print(f"{'Item' :<20}{'Held' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 28}{'|'}{'=' * 40}")
    for item in items.allItems:
        if item.held > 0:
            print(f"{item.name :<20}{item.held :<8}{'|' :<8}{item.desc :<32}")
    char.money
    print(f"Money: {char.money}")
    update_weapon(char)
    print(f"Current Weapon: {char.currentWeapon.name}")
    print(f"Current Staff: {char.currentStaff.name}")

display_inentory(character.hero)