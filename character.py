import inventory

class Character:
    def __init__(self):
        self.level = 1      # I think you can infer what Level is
        self.vit = 0        # Vitality - Affects character Health
        self.arc = 0        # Arcana - Affects character Mana
        self.acc = 0        # Accuracy
        self.int = 0        # Intelligence
        self.str = 0        # Strength
        self.end = 0        # Endurance

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
            char.endurance  == 1
        else:
            continue
        points -= 1
    char.level += 1
    print(f"Level: {char.level - 1} ==> {char.level}")
    print(f"VIT: {char.vitality}    ARC: {char.arcana}    ACC: {char.accuracy}    INT: {char.intelligence}    STR: {char.strength}    END: {char.endurance}")

warrior = Character()
warrior.vitality = 5
warrior.arcana = 1
warrior.accuracy = 3
warrior.intelligence = 1
warrior.strength = 5
warrior.endurance = 3

mage = Character()
mage.vitality = 1
mage.arcana = 5
mage.accuracy = 3
mage.intelligence = 5
mage.strength = 1
mage.endurance = 3

paladin = Character()
paladin.vitality = 3
paladin.arcana = 3
paladin.accuracy = 3
paladin.intelligence = 3
paladin.strength = 3
paladin.endurance = 3

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
