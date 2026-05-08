import character
import items
import inventory
import evil
import spells

from colorama import Back
import random

character.hero.currentWeapon = items.basicSword
character.hero.currentStaff = items.basicStaff

def displayHealth(char):
    unit = char.maxHealth / 25
    checking = 0
    count = 0
    yellow = Back.YELLOW + " "
    green = Back.GREEN + " "
    red = Back.RED + " "
    print(f"[{int(char.currentHealth)}/{char.maxHealth}]")
    print("[", end="")
    while count < 25:
        if checking <= char.currentHealth:
            if char.currentHealth <= char.maxHealth / 4:
                print(red, end="")      # Health bar is yellow if 25-50%
            elif char.currentHealth < char.maxHealth / 2:
                print(yellow, end="")   # Health bar is red if 0-25%
            else:
                print(green, end="")
        else:
            print(Back.RESET + " ", end="")
        checking += unit
        count += 1
    print(Back.RESET + "]")

def displayMana(char):
    unit = char.maxMana / 25
    checking = 0
    count = 0
    print(f"[{int(char.currentMana)}/{char.maxMana}]")
    print("[", end="")
    while count < 25:
        if checking <= char.currentMana:
            print(Back.BLUE + " ", end="")
        else:
            print(Back.RESET + " ", end="")
        checking += unit
        count += 1
    print(Back.RESET + "]")

def userTurn(player, enemy):
    print("What will you do?")
    userAction = input(f"{"1. Attack":<12}{"2. Spell":<12}\n{"3. Guard":<12}").title()
    if userAction == "Attack" or userAction == "1":
        attackFunction(player, enemy)
    elif userAction == "Spell" or userAction == "2":
        spellFunction(player, enemy)
    elif userAction == "Guard" or userAction == "3":
        player.defenseMod = guardFunction(player.defenseMod)
        print("Blocking.")
    elif userAction == "Items" or userAction == "4":
        pass

def attackFunction(char, opp):
    # TODO: Figure out what to do for enemy damage, unless you just want to give them regular items.  You may need to redo the Current Weapon mechanic
    damage = int((inventory.currentWeapon.number * char.physicalAttackMod) * opp.defenseMod)
    opp.currentHealth -= damage
    print(char.name, "attacked", opp.name, "for", damage, "damage.")

def spellFunction(char, opp):
    # This first code block is just for choosing a spell
    spellCast = False
    while spellCast == False:
        for item in spells.allSpells:
            if item.known == True:
                print(item.name)
        playerChoice = input("Choose a spell: ").title()
        for item in spells.allSpells:
            if playerChoice == item.name:
                spell = item
                spellCast = True
    char.currentMana -= spell.manaCost
    damage = int(((spell.number * char.spellAttackMod) * inventory.currentStaff.number) * opp.defenseMod)
    opp.currentHealth -= damage
    print(char.name, "casted", spell.name, "on", opp.name, "for", damage, "damage.")

    

def guardFunction(defMod):
    defMod /= 2
    return defMod

def enemyTurn(enemy, player):
    attackFunction(enemy, player)

def combatLoop(player, enemy):
    round = 1
    while player.currentHealth > 0 and enemy.currentHealth >= 0:
        print(f"{player.name}: ", end="")
        displayHealth(player)
        displayMana(player)
        print(f"{enemy.name}: ", end="")
        displayHealth(enemy)
        userTurn(player, enemy)
        enemyTurn(enemy, player)
        player.defenseMod = 1 - (player.endurance / 10)
        round += 1

combatLoop(character.hero, evil.goblin)

