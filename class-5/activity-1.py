import random
print("Welcome to Rock, Paper, Scissors!")
options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("rock, paper, or scissors: ").strip().lower()
    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(options)
    print("you chose: ", user_choice)
    print("computer chose: ", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("rock smashes scissors. You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("paper covers rock. You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("scissors cut paper. You win!")
    else:
        print("You lose! Better luck next time.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

