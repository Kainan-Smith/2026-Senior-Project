import character

playerHealth = character.stats["Health"]
enemyHealth = 100
userAction = ""

while playerHealth > 0 and enemyHealth > 0 and userAction != "Q":
    print("What will you do?")
    userAction = input("Attack\nSpell\nGuard\nItems\n").upper()
    if userAction == "ATTACK":
    elif userAction == "SPELL":
    elif userAction == "GUARD":
    elif userAction == "ITEMS":