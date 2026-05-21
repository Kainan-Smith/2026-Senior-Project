import character
import evil
import spells

from colorama import Back
import random

def display_health(char):
    unit = char.maxHealth / 25
    checking = 0
    count = 0
    yellow = Back.YELLOW + " "
    green = Back.GREEN + " "
    red = Back.RED + " "
    print(f"[{int(char.currentHealth)}/{char.maxHealth}]", end="")
    if char.condition != None and char.condition != "Crit":
        print(f" ({char.condition})")
        print("[", end="")
    else:
        print("\n[", end="")
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

def display_mana(char):
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

def user_turn(round, player, enemy, conEnds):
    print("What will you do?")
    actionDone = False
    while actionDone == False:
        userAction = input(f"{"1. Attack":<12}{"2. Spell":<12}").title()
        spell = None
        if userAction == "Attack" or userAction == "1":
            attack_function(player, enemy)
        elif userAction == "Spell" or userAction == "2":
            spell, conEnds = spell_function(round, player, enemy, conEnds)
            if spell == "cancelled":
                continue
        else:
            continue
        actionDone = True
    return spell, conEnds

def attack_function(char, opp):
    damage = int((char.currentWeapon.number * char.attackMod) * opp.defenseMod)
    opp.currentHealth -= damage
    print(char.name, "attacked", opp.name, "for", damage, "damage.")

def spell_function(round, char, opp, conEnds):
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
        if spellCast == False:
            print("Invalid Spell")
            return "cancelled", conEnds
        elif spell.manaCost > char.currentMana:
            print("Not enough Mana")
            return "cancelled", conEnds
    char.currentMana -= spell.manaCost
    if spell.healing == True:
        healing = int((spell.number * char.spellMod) * char.currentStaff.number)
        char.currentHealth += healing
        if char.currentHealth > char.maxHealth:
            char.currentHealth = char.maxHealth
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
                print(char.name, "casted", spell.name, "on", opp.name, "for", damage, "damage.      (It's a Crit!)")
                return spell,conEnds
        opp.currentHealth -= damage
        print(char.name, "casted", spell.name, "on", opp.name, "for", damage, "damage.")
    return spell, conEnds

def enemy_turn(round, enemy, player, conEnds, spell):
    if round == conEnds:
        enemy.condition = None
    if enemy.condition == "Frozen":
        pass
    elif enemy.condition == "Burned":
        enemy.currentHealth -= spell.damage
    attack_function(enemy, player)
    return enemy.condition

def combat_loop(player, enemy):
    round = 1
    conditionEnds = None
    print((player.attackMod))
    while True:
        print(f"{player.name}: ", end="")
        display_health(player)
        display_mana(player)
        print(f"{enemy.name}: ", end="")
        display_health(enemy)
        if player.currentHealth <= 0:
            break
        spell, conditionEnds = user_turn(round, player, enemy, conditionEnds)
        if enemy.currentHealth <= 0:
            break
        enemy.condition = enemy_turn(round, enemy, player, conditionEnds, spell)
        round += 1
    enemy.currentHealth = enemy.maxHealth
    player.currentXp += enemy.xpGiven
    player.money += enemy.moneyGiven
    print(f"{player.currentXp}/{player.nextLevelXp}")
    print(f"{player.money}")
    character.level_up(player)
