currentPlace = 1
visitedPlaces = []
availablePlaces = []

def go_to_new_place(place):
    # place variable is where you currently are
    # Try using the "availablePlaces" list to try and condense this code into less lines.
    # Try using Xaiden's dictionary method (Just ask him)
    newPlace = False
    while newPlace == False:
        if place == 1:
            playerSelection = int(input("Where would you like to go? (2, 4, or 0[Dev Room])"))
            if playerSelection == 2:
                if 2 in visitedPlaces:
                    yesOrNo = input("You've already been to 2, go back anyways? (Type \"yes\" or \"no\")")
                    if yesOrNo == "no":
                        continue
                print("Going to 2")
                place = 2
                newPlace = True
            elif playerSelection == 4:
                if 4 in visitedPlaces:
                    yesOrNo = input("You've already been to 2, go back anyways? (Type \"yes\" or \"no\")")
                    if yesOrNo == "no":
                        continue
                print("Going to 2")
                place = 4
                newPlace = True
        return place

currentPlace = go_to_new_place(currentPlace)
print(currentPlace)