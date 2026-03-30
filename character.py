import inventory

class Character:
    def __init__(self):
        self.level = 1      # I think you can infer what Level is
        self.vitality = 0        # Vitality - Affects Health
        self.arcana = 0        # Arcana - Affects Mana
        self.accuracy = 0        # Accuracy - Affects Hit Chance
        self.intelligence = 0        # Intelligence - Affects Spell Attack Modifier
        self.strength = 0        # Strength - Affects Physical Attack Modifier
        self.endurance = 0        # Endurance - Affects Defense Modifier

def LevelUp(char):
    points = 4
    while points > 0:
        print("Leveled Up!")
        print("Upgrade Points Remaining:", points)
        print(f"VIT: {char.vitality}    ARC: {char.arcana}    ACC: {char.accuracy}    INT: {char.intelligence}    STR: {char.strength}    END: {char.endurance}")
        upgrade = input("Enter a stat to put your points into: ").upper()

        if upgrade == "VIT":
            char.vitality += 1
        elif upgrade == "ARC":
            char.arcana += 1
        elif upgrade == "ACC":
            char.arcana += 1
        elif upgrade == "INT":
            char.intelligence += 1
        elif upgrade == "STR":
            char.strength += 1
        elif upgrade == "END":
            char.endurance  += 1
        else:
            continue
        points -= 1
    char.level += 1
    print(f"Level: {char.level - 1} ==> {char.level}")
    print(f"VIT: {char.vitality}    ARC: {char.arcana}    ACC: {char.accuracy}    INT: {char.intelligence}    STR: {char.strength}    END: {char.endurance}")
    output = check_modifiers(char)
    return output

def check_modifiers(char):
    maxHealth = 100 + (char.vitality * 20)
    maxMana = 100 + (char.arcana * 20)
    hitChance = 75 + (char.accuracy * 5)
    spellAttackModifier = (char.intelligence * 20)
    physicalAttackModifier = (char.strength * 20)
    defenseModifier = (char.endurance * 10)
    modifiers = {
        "Health": maxHealth,
        "Mana": maxMana,
        "Hit Chance": hitChance, 
        "Spell Attack Mod.": spellAttackModifier,
        "Physical Attack Mod.": physicalAttackModifier,
        "Defense Mod.": defenseModifier
        }
    return modifiers

def print_modifiers(mods):
    print(f"Max Health: {mods["Health"]}")
    print(f"Max Mana: {mods["Mana"]}")
    print(f"Hit Chance: {mods["Hit Chance"]}")
    print(f"Spell Attack Mod.: {mods["Spell Attack Mod."]}")
    print(f"Physical Attack Mod.: {mods["Physical Attack Mod."]}")
    print(f"Defense Mod.: {mods["Defense Mod."]}")

warrior = Character()
warrior.vitality = 5
warrior.arcana = 1
warrior.accuracy = 3
warrior.intelligence = 2
warrior.strength = 5
warrior.endurance = 4

mage = Character()
mage.vitality = 2
mage.arcana = 5
mage.accuracy = 4
mage.intelligence = 5
mage.strength = 1
mage.endurance = 3

paladin = Character()
paladin.vitality = 4
paladin.arcana = 3
paladin.accuracy = 3
paladin.intelligence = 3
paladin.strength = 3
paladin.endurance = 4

def chooseCharacter(choice):
    if choice == "warrior":
        character = warrior
    if choice == "mage":
        character = mage
    if choice == "paladin":
        character = paladin
    return character

playerChoice = input("Choose a character (Warrior, Mage, or Paladin):\n").lower()
playerCharacter = chooseCharacter(playerChoice)
stats = check_modifiers(playerCharacter)