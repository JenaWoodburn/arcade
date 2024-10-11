import sys
import random


def guess_number(name='PlayerOne'):
    #variables to track game statistics 
    game_count = 0  
    player_wins = 0
    computer_wins = 0

    def play_guess_number():  
        nonlocal name
        nonlocal player_wins
        #get player's choice
        player = int(input("\nGuess which number I'm thinking of: 1, 2 or 3:\n"))

        #check player has provided correct input
        if player not in [1, 2, 3]:
            print("The number must be either 1, 2 or 3")
            return play_guess_number()

        computer = random.choice([1, 2, 3])

        print(f"You chose {player}")
        print(f"I was thinking of {computer}")

        #game logic
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            if player == computer:
                player_wins += 1
                return "You won!"
            else:
                computer_wins += 1
                return "Sorry, you lose"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        #output statistics
        print(f"\nTotal games played: {game_count}")
        print(f"Player wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"Your winning percentage: {player_wins/game_count:.2%}")
        

        #ask whether player wants to continue or quit
        while True:
            play_again = input("\nPlay again? Enter y for yes or q to quit:\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == 'y':
            return play_guess_number()
        else:
            print("Thanks for playing!")
            if __name__ == "__main__":
                sys.exit()
            else:
                return
    
    return play_guess_number     

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Takes a user name for personalised game play")

    parser.add_argument(
        "-n", "--name", metavar="name", help="The name of the person playing the game", required=True
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()


