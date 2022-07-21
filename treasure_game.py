print("Welcome to treasure Island.\n Your mission is to find the treasure")
s1 = input("Do you wanna go left or right:").lower()
if s1 == 'left':
    print("you fell in hole")
elif s1 == 'right':
    s2 = input("You reached a lake. There is a castle in the lake do you wanna swim or take a boat: ").lower()
    if s2 == 'boat':
        print("You reached the castle enter it and take the treasure")
    elif s2 == 'swim':
        print("Crocodiles ate you, stupid!")
    else:
        print("wrong input! Game over")
else:
    print("wrong input start again")