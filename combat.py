import character
import items
import inventory

playerHealth = character.stats["Health"]
enemyTotal = 100
enemyHealth = enemyTotal
userAction = ""

def displayHealth(total, current):
    unit = total / 25
    checking = 0
    print("[", end="")
    while checking < total:
        if checking <= current:
            print("|", end="")
        else:
            print("-", end="")
        checking += unit
    print("]")

while playerHealth > 0 and enemyHealth > 0 and userAction != "Q":
    displayHealth(enemyTotal, enemyHealth)
    guarding = False
    print("What will you do?")
    userAction = input("Attack\nSpell\nGuard\nItems\n").title()
    if userAction == "Attack":
        userDmg = (inventory.currentWeapon.number * character.stats["Physical Attack Mod."])
        enemyHealth -= userDmg
    elif userAction == "Spell":
        pass
    elif userAction == "Guard":
        guarding = True
    elif userAction == "Items":
        pass