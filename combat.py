import character
import items
import inventory

playerTotal = character.stats["Health"]
playerHealth = playerTotal
enemyTotal = 100
enemyHealth = enemyTotal
userAction = ""

def displayHealth(total, current):
    unit = total / 25
    checking = 0
    print(f"{int(current)}/{total}")
    print("[", end="")
    while checking < total:
        if checking <= current:
            print("I", end="")
        else:
            print("-", end="")
        checking += unit
    print("]")

# Delete this function
def userTurn(enemy):
    guarding = False
    print("What will you do?")
    userAction = input(f"{"Attack":<12}{"Spell":<12}\n{"Guard":<12}{"Items"}\n").title()
    if userAction == "Attack":
        userDmg = (inventory.currentWeapon.number * character.stats["Physical Attack Mod."])
        enemyHealth -= userDmg
    elif userAction == "Spell":
        pass
    elif userAction == "Guard":
        guarding = True
    elif userAction == "Items":
        pass

def attack(atkMod):

def spell(psiMod):

def guard(defMod):

def items():


def enemyTurn(player):
    damage = 30
    print("Enemy Attacks Player for", damage, " damage!")
    return damage

def combatLoop(playerH, playerT, enemyH, enemyT)
    while playerHealth > 0 and enemyHealth > 0:
        print("Player: ", end="")
        displayHealth(playerTotal, playerHealth)
        print("Enemy: ", end="")
        displayHealth(enemyTotal, enemyHealth)
        
        playerHealth -= enemyTurn(playerHealth)