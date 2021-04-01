import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')

print("""Ground Rules of this game:
1. Rock beats Scissor
2. Scissor beats paper
3. Paper beats Rock""")

while(1 < 2):
    print("\n")
    print("Rock, Paper, Scissors -Start")

    userChoice = input("Pick a Choice [R]ock, [P]paper, or [S]cissores: ")


    print("You chose: "+userChoice)
    Choices = ['R','P','S']
    opponentsChoice = random.choice(Choices)
    print("I chose: "+opponentsChoice)
    if opponentsChoice == userChoice:
        print("Tie!")
    elif opponentsChoice == str("R") and str.upper(userChoice) == "p":
        print("I Win!")
    elif opponentsChoice == str("P") and str.upper(userChoice) == "S":
        print("I Win!")
    elif opponentsChoice == str("S") and str.upper(userChoice) == "R":
        print("I Win!")
    else:
        print("You Win!")
