import character
import items
import inventory

playerTotal = character.stats["Health"]
playerHealth = playerTotal
enemyTotal = 100
enemyHealth = enemyTotal
attack = character.stats["Physical Attack Mod."]
spell = character.stats["Spell Attack Mod."]
defense = character.stats["Defense Mod."]
userAction = ""

def displayHealth(total, current):
    unit = total / 25
    checking = 0
    print(f"[{int(current)}/{total}]")
    print("[", end="")
    while checking < total:
        if checking <= current:
            print("I", end="")
        else:
            print("-", end="")
        checking += unit
    print("]")

def userTurn():
    global defense
    defense = character.stats["Defense Mod."]
    print("What will you do?")
    userAction = input(f"{"1. Attack":<12}{"2. Spell":<12}\n{"3. Guard":<12}{"4. Items"}\n").title()
    if userAction == "Attack" or userAction == "1":
        pass
    elif userAction == "Spell" or userAction == "2":
        pass
    elif userAction == "Guard" or userAction == "3":
        defense = guardFunction(defense)

    elif userAction == "Items" or userAction == "4":
        pass

def attackFunction(atkMod):
    damage = (inventory.currentWeapon.number * attack)
    return damage
def spellFunction(psiMod):
    spellDamage = (inventory.currentWeapon.number * spell)
    return spellDamage
def guardFunction(defMod):
    guarding = (defMod / 2)
    return guarding
def items():
    pass

def enemyTurn(player):
    damage = int(30 * defense)
    print("Enemy Attacks Player for", damage, "damage!")
    return damage

def combatLoop(playerH, playerT, enemyH, enemyT):
    global defense
    while playerH > 0 and enemyH > 0:
        print("Player: ", end="")
        displayHealth(playerT, playerH)
        print("Enemy: ", end="")
        displayHealth(enemyT, enemyH)
        userTurn()
        playerH -= enemyTurn(playerH)

combatLoop(playerHealth, playerTotal, enemyHealth, enemyTotal)