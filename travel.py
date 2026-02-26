currentPlace = 0
global visitedPlaces
visitedPlaces = [2, 3, 4]

def checkPlaces(currentArea):
    '''Uses the availablePlaces variable to determine which areas the player can travel to.'''
    availablePlaces = []
    if currentArea == 1:
        availablePlaces = [2, 4]
    if currentArea == 2:
        availablePlaces = [1, 3, 5]
    if currentArea == 3:
        availablePlaces = [2, 4]
    if currentArea == 4:
        availablePlaces = [1, 3, 5, 7]
    if currentArea == 5:
        availablePlaces = [2, 4, 6]
    if currentArea == 6:
        availablePlaces = [6, 7]
    if currentArea == 7:
        availablePlaces = [4, 6, 8]
    if currentArea == 8:
        availablePlaces = [7]
    if currentArea == 0:
        availablePlaces = [1, 2, 3, 4, 5, 6, 7, 8]
    return availablePlaces

def go_to_new_place(place):
    # place variable is where you currently are
    # Try using the "availablePlaces" list to try and condense this code into less lines.
    # Try using Xaiden's dictionary method (Just ask him)
    global visitedPlaces
    moving = False
    available = checkPlaces(place)
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
        if playerSelection in visitedPlaces:
            print(f"You've already been to {playerSelection}, go anyways? ('yes' or 'no')")
            yesOrNo = input()
            if yesOrNo == "no":
                continue
        print("Traveling to", playerSelection, "now.")
        moving = True
    newPlace = playerSelection
    visitedPlaces.append(place)
    return newPlace

go_to_new_place(currentPlace)
print("Current Area:", currentPlace)
print("Area you've been:", visitedPlaces)