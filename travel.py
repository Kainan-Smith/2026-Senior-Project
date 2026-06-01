# TODO: REWORK TRAVEL.PY.  MAKE IT SO IN THE CHECK_WORLDS FUNCTION, YOU USE THE ACTUAL VARIABLE FOR THE WORLDS RATHER THAN JUST SINGLE DIGIT NUMBERS.
#       MAY NEED TO COMBINE TRAVEL.PY AND WORLDS.PY TO MAKE THIS WORK.

import character
import worlds

def check_worlds(currentArea):
    #   Uses the availableWorlds variable to determine which areas the player can travel to.
    availableWorlds = []
    if currentArea == 1:
        availableWorlds = [2, 4]
    elif currentArea == 2:
        availableWorlds = [1, 3, 5]
    elif currentArea == 3:
        availableWorlds = [2, 4]
    elif currentArea == 4:
        availableWorlds = [1, 3, 5, 7]
    elif currentArea == 5:
        availableWorlds = [2, 4, 6]
    elif currentArea == 6:
        availableWorlds = [6, 7]
    elif currentArea == 7:
        availableWorlds = [4, 6, 8]
    elif currentArea == 8:
        availableWorlds = [7]
    # You can probably delete the second condition and just make it so that you can only get to World 0 if hero.name == "Chris Bar"
    elif currentArea == 0 and character.hero.name == "Chris Bar":
        availableWorlds = [1, 2, 3, 4, 5, 6, 7, 8]
    return availableWorlds

def go_to_new_place(hero):
    # place variable is where you currently are
    
    moving = False
    available = check_worlds(hero.currentWorld)
    numAvail = len(available)
    print("Worlds you've visited:", hero.visitedWorlds)
    while moving == False:
        print("Would you like to go to ", end="")
        if numAvail > 2:
            for count in range(numAvail - 1):
                print(f"{available[count]}, ", end="")
            print(f"or {available[-1]}?")
        else:
            print(f"{available[0]} or {available[1]}?")
        playerSelection = int(input())
        worldChecked = worlds.allWorlds[playerSelection - 1]
        if playerSelection not in available:
            print(playerSelection, "not available.")
            continue
        print("Traveling to", playerSelection, "now.")
        moving = True
    newPlace = playerSelection
    hero.visitedWorlds.append(hero.currentWorld)
    hero.visitedWorlds.sort()
    hero.currentWorld = newPlace