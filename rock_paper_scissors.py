import random

def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- New Round ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            user_score += 1
            print("You win!")
        elif result == "lose":
            computer_score += 1
            print("You lose!")
        else:
            print("It's a tie!")

        print("Your score:", user_score)
        print("Computer score:", computer_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
