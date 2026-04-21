import character
import items

playerHealth = character.stats["Health"]
enemyHealth = 100
userAction = ""

while playerHealth > 0 and enemyHealth > 0 and userAction != "Q":
    print("What will you do?")
    userAction = input("Attack\nSpell\nGuard\nItems\n").title()
    if userAction == "Attack":
        userDmg = (items.weaponBaseDmg * character.physicalAttackModifier)
    elif userAction == "Spell":
    elif userAction == "Guard":
    elif userAction == "Items":