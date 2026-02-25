newPlace = False
currentPlace = 1
visitedPlaces = []

def go_to_new_place(place):
    # place variable is where you currently are
    while newPlace == False:
        if currentPlace == 1:
            playerSelection = int(input("Where would you like to go? (2, 4, or 0[Dev Room])"))
            if playerSelection == 2:
                if 2 in visitedPlaces:
                    yesOrNo = input("You've already been to 2, go back anyways? (Type \"yes\" or \"no\")")
                    if yesOrNo == "yes":
                        print("Going to 2")
                    else:
                        continue
                currentPlace = 2