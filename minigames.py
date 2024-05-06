import random
import re


def rock_paper_scissors():
    print("~= ROCK-PAPER-SCISSORS =~")

    score = 0
    score2 = 0

    while(True):
        choices = ["rock", "paper", "scissors"]
        again = "y"
        p1 = input("Enter choice: ")
        p2 = random.choice(choices)

        print(f"You chose {p1}, CPU chose {p2}. \n")

        if p1 == p2:
            print(f"Both players selected {p1}. It's a tie!")
        elif p1 == "rock":
            if p2 == "scissors":
                print("Rock smashes scissors! You win!")
                score += 1
            else:
                print("Paper covers rock! You lose.")
                score2 += 1
        elif p1 == "paper":
            if p2 == "rock":
                print("Paper covers rock! You win!")
                score += 1
            else:
                print("Scissors cuts paper! You lose.")
                score2 += 1
        elif p1 == "scissors":
            if p2 == "paper":
                print("Scissors cuts paper! You win!")
                score += 1
            else:
                print("Rock smashes scissors! You lose.")
                score2 += 1

        print(f"Your Score: {score}")
        print(f"CPU Score: {score2}")

        if score == 2 or score2 == 2:
            break

    
def dice_roll():
    print("~= DICE ROLL =~")
    tries = 0
    max_tries = 3
    dice = random.randint(1,6)
    
    while (True):
        player = int(input("Guess the number: "))

        if player != dice:
            print("Wrong")
            tries += 1
        else:
            print(f"The number was {dice}. YOU WIN")
            break
        
        if tries == max_tries:
            print(f"The number was {dice}. YOU LOSE")
            break
        
def hangman():
    print("~= HANGMAN =~")
    
    with open("pokemon.txt", "r") as file:
        word_list = file.read().splitlines()

    random_num = random.randint(0, len(word_list) - 1)  
    word_chosen = word_list[random_num]
    word = word_chosen.lower()
    
    encoded_word = re.sub('[0-9a-zA-Z]', '-', word)

    lives = 5
    tries = 0
    
    while lives > 0 and tries != 5:
        
        print_hangman(tries)
        print(encoded_word)

        guessed_letter = input("Guess a letter: ")
        letter_found, encoded_word = guess(guessed_letter, word, encoded_word)

        if not letter_found:
            lives -= 1
            tries += 1
            
            if lives == 0:
                print_hangman(5)
                print("\nGame over, you lost! :( The Pokemon was '%s'" % word)
                break
            else:
                print("\nWhoops! That letter was not found. You now have %d lives remaining." % lives)
        else:
            if "-" not in encoded_word:
                print("\nHooray! You won with %d lives remaining. The Pokemon was '%s'" % (lives, word))
                break
            else:
                print("\nGood job! That letter was found. You still have %d lives remaining." % lives)
                

    




def print_hangman(tries):

    
    picture_array = ["""
    ________
    |       |
    |       O
    |     
    |
    |_________
                     
""", """
    ________
    |       |
    |       O
    |       |
    |
    |_________
                
""", """
    ________
    |       |
    |       O
    |      l|
    |
    |_________
""","""
    ________
    |       |
    |       O
    |      l|l
    |
    |_________
""","""
    ________
    |       |
    |       O
    |      l|l
    |      /
    |_________
""", """
    ________
    |       |
    |       O
    |      l|l
    |      //
    |_________
"""]
    
    print(picture_array[tries])

def guess(letter, word, encoded):
    found = False
    if letter in word:
        found = True

        for i in range(0, len(word)):
            if word[i] == letter:
                encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
    return (found, encoded)

