import character
import evil
import spells

from colorama import Back
import random

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

def userTurn(round, player, enemy, conEnds):
    print("What will you do?")
    userAction = input(f"{"1. Attack":<12}{"2. Spell":<12}\n{"3. Guard":<12}").title()
    spell = None
    if userAction == "Attack" or userAction == "1":
        attackFunction(player, enemy)
    elif userAction == "Spell" or userAction == "2":
        spell, conEnds = spellFunction(round, player, enemy, conEnds)
    elif userAction == "Guard" or userAction == "3":
        player.defenseMod = guardFunction(player.defenseMod)
        print("Blocking.")
    elif userAction == "Items" or userAction == "4":
        pass
    return spell, conEnds

def attackFunction(char, opp):
    # TODO: Figure out what to do for enemy damage, unless you just want to give them regular items.  You may need to redo the Current Weapon mechanic
    damage = int((char.currentWeapon.number * char.physicalAttackMod) * opp.defenseMod)
    opp.currentHealth -= damage
    print(char.name, "attacked", opp.name, "for", damage, "damage.")

def spellFunction(round, char, opp, conEnds):
    # This first code block is just for choosing a spell
    spellCast = False
    while spellCast == False:
        for item in spells.allSpells:
            if item.known == True:
                print(item.name)
        playerChoice = input("Choose a spell: ").title()
        for item in spells.allSpells:
            if playerChoice == item.name and item.known == True:
                spell = item
                spellCast = True
    char.currentMana -= spell.manaCost
    if spell.healing == True:
        healing = int((spell.number * char.spellMod) * char.currentStaff.number)
        char.currentHealth += healing
        print(char.name, "casted", spell.name, "and healed for", healing, "HP.")
    if spell.damage == True:
        damage = int(((spell.number * char.spellMod) * char.currentStaff.number) * opp.defenseMod)
        randomNumber = random.randint(1, 100)
        if randomNumber <= spell.chance:
            opp.condition = spell.condition
            conEnds = round + spell.lasts + 1
            if spell.condition == "Crit":
                damage += damage
        opp.currentHealth -= damage
        print(char.name, "casted", spell.name, "on", opp.name, "for", damage, "damage.")
    return spell, conEnds

# TODO: Change Guard Action to Potion Action
def guardFunction(defMod):
    defMod /= 2
    return defMod

def enemyTurn(round, enemy, player, conEnds, spell):
    attackFunction(enemy, player)
    if round == conEnds:
        enemy.condition = None
    if enemy.condition == "Frozen":
        pass
    elif enemy.condition == "Burned":
        enemy.currentHealth -= spell.damage
    return enemy.condition

def combatLoop(player, enemy):
    round = 1
    conditionEnds = None
    while player.currentHealth > 0 and enemy.currentHealth > 0:
        print(f"{player.name}: ", end="")
        displayHealth(player)
        displayMana(player)
        print(f"{enemy.name}: ", end="")
        displayHealth(enemy)
        spell, conditionEnds = userTurn(round, player, enemy, conditionEnds)
        enemy.condition = enemyTurn(round, enemy, player, conditionEnds, spell)
        print(enemy.condition, round, conditionEnds)
        player.defenseMod = 1 - (player.endurance / 10)
        round += 1

combatLoop(character.hero, evil.goblin)

