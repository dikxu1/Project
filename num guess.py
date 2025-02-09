#python number guessing game
import random

n = random.randint(1,100)
guesses = 0
is_running = True

print("Python Number Guessing Game.")
print("Select a number between 1 to 100.")

while is_running:
    guess=input("Enter your guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess < 0 or guess > 100:
            print("Invalid Input!")
            print("Enter a number between 1 to 100.")
        elif guess > n:
            print("Guess is too high.")
        elif guess < n:
            print("Guess is too low.")
        else:
            print(f"{guess} is the correct guess.")
            print(f"The number of guess took was {guesses}")
            is_running = False

    else:
        print("Invalid Input!")
        print("Enter a number between 1 to 100.")
        

