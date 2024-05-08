from minigames import rock_paper_scissors
from minigames import dice_roll
from minigames import hangman
import time

def select(selection):
    
    if selection == "0":
        return
    elif selection == "1":
        print("Loading Rock-Paper-Scissors...")
        time.sleep(2)
        rock_paper_scissors()
    elif selection == "2":
        print("Loading Dice Roll...")
        time.sleep(2)
        dice_roll()
    elif selection == "3":
        print("Loading Hangman...")
        time.sleep(2)
        hangman()
    

def main():
    while True:
        print(""" 

~= PyMinigames =~

    Choose the game you want to play:      

    1. Rock-Paper-Scissors
    2. Dice Roll
    3. Hangman (Pokemon Edition)
    4. Black Jack (Coming soon)
    5. Tic Tac Toe (Coming soon)
    6. Quit

""")

        selection = input("Select Game: ")
        if selection == "6":
            break
        select(selection)

main()
