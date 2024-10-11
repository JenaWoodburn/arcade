import sys
from rps import rps
from guess_number import guess_number

def arcade(name='PlayerOne'):
    welcome_back = False

    while True:
        #print a welcome message when player returns to arcade after playing one of the games
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu")

        #get player choice
        player = input("\nPlease choose a game:\n" \
        "1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n")

        #if player doesn't choose one of the required options, ask again
        if player not in ["1", "2", "x", "X"]:
            print("Please enter 1, 2 or \"x\"")
            return arcade(name)
        
        welcome_back = True
        
        #game choice logic
        if player == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else: 
            print(f"See you next time, {name}!")
            sys.exit()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalised game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the player"
    )

    args = parser.parse_args()

    print(f"{args.name}, welcome to the Arcade!")

arcade(args.name)
