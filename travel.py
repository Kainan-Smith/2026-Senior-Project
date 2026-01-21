currentPlace = 1
visitedPlaces = []

def go_to_new_place(place):
    # place variable is where you currently are
    if place == 1:
        choice = input("Where would you like to go? (2 or 4) ")
        visitedPlaces.append(1)
        if choice == "2":
            place = 2
        elif choice == "4":
            place = 4
    
    elif place == 2:
        print("Where would you like to go? (1, 3 or 5) ")
        visitedPlaces.append(2)
        if choice == "1":
            place = 1
        elif choice == "3":
            place = 3
        elif choice == "5":
            place = 5

    elif place == 3:
        print("Where would you like to go? (2 or 4) ")
        visitedPlaces.append(3)
        if choice == "2":
            place = 2
        elif choice == "4":
            place = 4

    elif place == 4:
        print("Where would you like to go? (1, 3, 5, or 7) ")
        visitedPlaces.append(4)
        if choice == "1":
            place = 1
        elif choice == "3":
            place = 3
        elif choice == "5":
            place = 5
        elif choice == "7":
            place = 7

    elif place == 5:
        print("Where would you like to go? (2, 4, or 6) ")

    elif place == 6:
        print("Where would you like to go? (5 or 7) ")

    elif place == 7:
        print("Where would you like to go? (4, 6, or 8) ")

    elif place == 8:
        print("Can't go anywhere else.")

    elif place == "dev":
        print("Go wherever")
    

    return place

if __name__ == "__main__":
    currentPlace = (go_to_new_place(currentPlace))
    print(currentPlace)