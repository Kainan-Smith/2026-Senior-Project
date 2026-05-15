import character

currentWorld = 1
visitedWorlds = [2, 3, 4]

def check_worlds(currentArea):
    '''Uses the availableWorlds variable to determine which areas the player can travel to.'''
    availableWorlds = []
    if currentArea == 1:
        availableWorlds = [2, 4]
    if currentArea == 2:
        availableWorlds = [1, 3, 5]
    if currentArea == 3:
        availableWorlds = [2, 4]
    if currentArea == 4:
        availableWorlds = [1, 3, 5, 7]
    if currentArea == 5:
        availableWorlds = [2, 4, 6]
    if currentArea == 6:
        availableWorlds = [6, 7]
    if currentArea == 7:
        availableWorlds = [4, 6, 8]
    if currentArea == 8:
        availableWorlds = [7]
    if currentArea == 0 and :
        availableWorlds = [1, 2, 3, 4, 5, 6, 7, 8]
    return availableWorlds

def go_to_new_place(place, visited):
    # place variable is where you currently are
    # Try using the "availableWorlds" list to try and condense this code into less lines.
    # Try using Xaiden's dictionary method (Just ask him)
    global visitedWorlds
    moving = False
    available = check_worlds(place)
    numAvail = len(available)
    while moving == False:
        print("Would you like to go to ", end="")
        if numAvail > 2:
            for count in range(numAvail - 1):
                print(f"{available[count]}, ", end="")
            print(f"or {available[-1]}?")
        else:
            print(f"{available[0]} or {available[1]}?")
        playerSelection = int(input())
        if playerSelection not in available:
            print(playerSelection, "not available.")
            continue
        if playerSelection in visited:
            print(f"You've already been to {playerSelection}, go anyways? ('yes' or 'no')")
            yesOrNo = input()
            if yesOrNo == "no":
                continue
        print("Traveling to", playerSelection, "now.")
        moving = True
    newPlace = playerSelection
    visited.append(place)
    visited.sort()
    return newPlace

currentWorld = go_to_new_place(currentWorld, visitedWorlds)
print("Current world:", currentWorld)
print("Worlds you've visited:", visitedWorlds)