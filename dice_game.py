import random


# Function to simulate rolling a six-sided dice
def roll_dice():
    return random.randint(1, 6)


# Function to play a single round of the game
def play_round():
    # Roll the dice for the user and computer
    user_roll = roll_dice()
    computer_roll = roll_dice()

    # Display the results of the dice rolls
    print(f"User rolled: {user_roll}")
    print(f"Computer rolled: {computer_roll}")

    # Determine the winner of this round
    if user_roll > computer_roll:
        return "user"
    elif user_roll < computer_roll:
        return "computer"
    else:
        return "tie"


# Main game function
def main():
    user_score = 0
    computer_score = 0

    # Play 3 rounds of the game
    for round_num in range(1, 4):
        print(f"Round {round_num}:")
        winner = play_round()

        # Update scores and announce the winner of the round
        if winner == "user":
            user_score += 1
            print("User wins this round!\n")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!\n")
        else:
            print("It's a tie in this round!\n")

    # Announce the final winner of the game
    print("Game Over!")
    if user_score > computer_score:
        print("User wins the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")


# Entry point of the program
if __name__ == "__main__":
    main()