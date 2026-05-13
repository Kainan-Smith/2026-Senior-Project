import items

class Character:
    def __init__(self):
        self.name = "Gort"
        self.level = 1          # I think you can infer what Level is
        self.currentXp = 0
        self.nextLevelXp = 100
        self.vitality = 0       # Vitality - Affects Health
        self.arcana = 0         # Arcana - Affects Mana
        self.accuracy = 0       # Accuracy - Affects Hit Chance
        self.intelligence = 0   # Intelligence - Affects Spell Modifier
        self.strength = 0       # Strength - Affects Physical Attack Modifier
        self.endurance = 0      # Endurance - Affects Defense Modifier
        self.maxHealth = 100
        self.maxMana = 100
        self.spellMod = 1
        self.attackMod = 1
        self.defenseMod = 1
        self.currentHealth = 100
        self.currentWeapon = items.newSword
        self.currentStaff = items.basicStaff
        self.condition = None


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
    char.maxHealth = 100 + (char.vitality * 20)
    char.maxMana = 100 + (char.arcana * 20)
    char.spellMod = 1 + (char.intelligence * 0.2)
    char.attackMod = 1 + (char.strength * 0.2)
    char.defenseMod = 1 - (char.endurance / 10)

def print_modifiers(mods):
    print(f"Max Health: {mods["Health"]}")
    print(f"Max Mana: {mods["Mana"]}")
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
warrior.maxHealth = 100 + (warrior.vitality * 20)
warrior.maxMana = 100 + (warrior.arcana * 20)
warrior.currentHealth = warrior.maxHealth
warrior.currentMana = warrior.maxMana
warrior.spellMod = 1 + (warrior.intelligence * 0.2)
warrior.attackMod = 1 + (warrior.strength * 0.2)
warrior.defenseMod = 1 - (warrior.endurance / 10)

mage = Character()
mage.vitality = 2
mage.arcana = 5
mage.accuracy = 4
mage.intelligence = 5
mage.strength = 1
mage.endurance = 3
mage.maxHealth = 100 + (mage.vitality * 20)
mage.maxMana = 100 + (mage.arcana * 20)
mage.currentHealth = mage.maxHealth
mage.currentMana = mage.maxMana
mage.spellMod = 1 + (mage.intelligence * 0.2)
mage.attackMod = 1 + (mage.strength * 0.2)
mage.defenseMod = 1 - (mage.endurance / 10)

paladin = Character()
paladin.vitality = 4
paladin.arcana = 3
paladin.accuracy = 3
paladin.intelligence = 3
paladin.strength = 3
paladin.endurance = 4
paladin.maxHealth = 100 + (paladin.vitality * 20)
paladin.maxMana = 100 + (paladin.arcana * 20)
paladin.currentHealth = paladin.maxHealth
paladin.currentMana = paladin.maxMana
paladin.spellMod = 1 + (paladin.intelligence * 0.2)
paladin.attackMod = 1 + (paladin.strength * 0.2)
paladin.defenseMod = 1 - (paladin.endurance / 10)

def chooseCharacter(choice):
    if choice == "warrior":
        character = warrior
    if choice == "mage":
        character = mage
    if choice == "paladin":
        character = paladin
    return character

#    playerChoice = input("Choose a character (Warrior, Mage, or Paladin):\n").lower()
#    playerCharacter = chooseCharacter(playerChoice)
hero = paladin
#   stats = check_modifiers(hero)
check_modifiers(hero)