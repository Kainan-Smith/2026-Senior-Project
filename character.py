import inventory

class Character:
    def __init__(self):
        self.level = 1
        self.vitality = 0
        self.arcana = 0
        self.accuracy = 0
        self.intelligence = 0
        self.strength = 0
        self.endurance = 0

warrior = Character()
warrior.vitality = 5
warrior.arcana = 1
warrior.accuracy = 3
warrior.intelligence = 1
warrior.strength = 4
warrior.endurance = 3

mage = Character()
mage.vitality = 1
mage.arcana = 5
mage.accuracy = 2
mage.intelligence = 1
mage.strength = 4
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
print(f"{playerCharacter.vitality}")