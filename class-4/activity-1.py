print("Welcome to the Number Guessing Game!")
import random 
lower_bound = 1
upper_bound = 10
max_attempts = 12
def get guess():
while True:
     guess = int(input("guess a number between 1 and 10: "))
if lower_bound <= guess <= upper_bound:
return guess 
else:
print(f"Please enter a number between {lower_bound} and {upper_bound}.")
def check_guess(guess, secret_number):
    if guess < secret_number:
        return "higher"
    elif guess > secret_number:
        return "lower"
    else:
        return "correct"
    
    def play_game():
        attempts = 0
        won = False
        while attempts < max_attempts:

atempts += 1
guess = getguess()
result = check_guess(guess, secret_number)
     if result correct
        print("Congratulations! You've guessed the number!")
        won = True
        break
else:
print(f"{result}. try again.")
if not won:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
    if __name__ == "__main__":
        print("welcome to the number guessing game!")
        play_game()