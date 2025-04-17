from treasure_art import treasure_art
print(treasure_art)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a cross road. Where do you want to go? \n Type 'left' or 'right' ").lower()

if (choice == "left".lower()):
    choice = input("You've come to a lake. There is an island in the middle of the lake. \n Type 'wait' to wait for a boat.  Type 'swim' to swim across. ").lower()
    if(choice == "wait".lower()):
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. \n Which colour do you choose? ").lower()
        if(choice == "yellow".lower()):
            print("You found the treasure! You win!")
        elif(choice == "red".lower()):
            print("Burned by fire. Game over.")
        elif(choice == "blue".lower()):
            print("Eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("Attacked by an angry trout. Game over.")
else:
    print("Fall into a hole. Game over.")



