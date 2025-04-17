# Rules
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

from options import rock, paper, scissors
import random

options = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_option = int(input("What do you choose? "))

computer_option = random.randint(0, 2)

if user_option == 0 and computer_option == 1:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("You lose")
elif user_option == 0 and computer_option == 2:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("You win")
elif user_option == 1 and computer_option == 0:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("You win")
elif user_option == 1 and computer_option == 2:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("You lose")
elif user_option == 2 and computer_option == 0:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("You lose")
elif user_option == 2 and computer_option == 1:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("You win")
elif user_option == computer_option:
    print("player:")
    print(options[user_option])
    print("computer:")
    print(options[computer_option])
    print("It's a draw")





