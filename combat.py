import character
import items
import inventory
import enemy

character.hero.currentWeapon = items.basicSword
character.hero.currentStaff = items.basicStaff

def displayHealth(char):
    unit = char.maxHealth / 25
    checking = 0
    yellow = "\x1b[33mI\x1b[0m"
    green = "\x1b[32mI\x1b[0m"
    red = "\x1b[31mI\x1b[0m"
    print(f"[{int(char.currentHealth)}/{char.maxHealth}]")
    print("[", end="")
    while checking < char.maxHealth:
        if checking <= char.currentHealth:
            if char.currentHealth <= char.maxHealth / 4:
                print(red, end="")   # Health bar is yellow if 25-50%
            elif char.currentHealth < char.maxHealth / 2:
                print(yellow, end="")      # Health bar is red if 0-25%
            else:
                print(green, end="")
        else:
            print("-", end="")
        checking += unit
    print("]")

def displayMana(char):
    unit = char.maxMana / 25
    checking = 0
    print(f"[{int(char.currentMana)}/{char.maxMana}]")
    print("[", end="")
    while checking <= char.maxMana:
        if checking <= char.currentMana:
            print("\x1b[34mI\x1b[0m", end="")
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
    player.currentHealth -= damage

def combatLoop(player, enemy):
    while player.currentHealth > 0 and enemy.currentHealth >= 0:
        print("Player: ", end="")
        displayHealth(player)
        displayMana(player)
        print("Enemy: ", end="")
        displayHealth(enemy)
        userTurn(player, enemy)
        enemyTurn(enemy, player)
        player.defenseMod = 1 - (player.endurance / 10)

combatLoop(character.hero, enemy.goblin)

