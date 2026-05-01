import character

def displayMana(char):
    unit = int(char.maxMana / 25)
    checking = 0
    print(f"[{int(char.currentMana)}/{char.maxMana}]")
    print("[", end="")
    while checking < char.maxMana + 1:
        print(checking, end=" ")
        checking += unit
    print("]")

displayMana(character.hero)