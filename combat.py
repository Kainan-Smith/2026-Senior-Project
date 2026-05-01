import character
import items
import inventory
import enemy

def displayHealth(char):
    unit = char.maxHealth / 25
    checking = 0
    print(f"[{int(char.currentHealth)}/{char.maxHealth}]")
    print("[", end="")
    while checking < char.maxHealth:
        if checking <= char.currentHealth:
            print("I", end="")
        else:
            print("-", end="")
        checking += unit
    print("]")

def userTurn(player, enemy):
    print("What will you do?")
    userAction = input(f"{"1. Attack":<12}{"2. Spell":<12}\n{"3. Guard":<12}{"4. Items"}\n").title()
    if userAction == "Attack" or userAction == "1":
        pass
    elif userAction == "Spell" or userAction == "2":
        pass
    elif userAction == "Guard" or userAction == "3":
        player.defenseMod = guardFunction(player.defenseMod)

    elif userAction == "Items" or userAction == "4":
        pass

def attackFunction(atkMod):
    damage = (inventory.currentWeapon.number * atkMod)
    return damage
def spellFunction(psiMod):
    spellDamage = (inventory.currentWeapon.number * psiMod)
    return spellDamage
def guardFunction(defMod):
    defMod /= 2
    return defMod
def items():
    pass

def enemyTurn(enemy, player):
    damage = int(enemy.damage * player.defenseMod)
    print("Enemy Attacks Player for", damage, "damage!")
    return damage

def combatLoop(player, enemy):
    while player.currentHealth > 0 and enemy.currentHealth >= 0:
        print("Player: ", end="")
        displayHealth(player)
        print(player.currentHealth, player.maxHealth)
        print("Enemy: ", end="")
        displayHealth(enemy)
        userTurn(player, enemy)
        enemyTurn(enemy, player)
        player.defenseMod = 1 - (player.endurance / 10)

combatLoop(character.hero, enemy.goblin)