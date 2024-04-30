import random


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

        again = input("Wanna play again? (y/n): ")
        if again.lower() != 'y':
            break

    
def dice_roll():
    print("~= DICE ROLL =~")
    tries = 0
    max_tries = 3
    again = "y"
    dice = random.randint(1,6)
    player = input("Guess the number: ")

    while tries < max_tries and again == "y":
        if int(player) == dice:
            print("You Win")
            break
        else:
            print("Wrong")
            tries += 1
        
        if tries == max_tries:
            print("You Lose")
            break

        again = input("Wanna Try Again? ")
        if again != 'y':
            break
     





