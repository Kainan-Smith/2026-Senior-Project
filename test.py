import character

from colorama import Fore, Back, Style

def displayHealth(char):
    unit = char.maxHealth / 25
    checking = 0
    count = 0
    yellow = "\x1b[33mI\x1b[0m"
    green = Back.GREEN + " "
    red = Fore.RED + Back.RED + "I"
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
            print(" ", end="")
        checking += unit
        count += 1
    print(Back.RESET + "]")

displayHealth(character.hero)