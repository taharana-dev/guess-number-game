# import random so the computer can pick a number
import random

# computer chooses a number between 1 and 10
number = random.randint(1, 10)

# keep track of how many guesses the user makes
attempts = 0

# run the game until the user guesses correctly
while True:

    # ask user for a guess and convert it to a number
    guess = int(input("Guess a number between 1 and 10: "))

    # increase attempt count
    attempts += 1

    # check if guess is correct
    if guess == number:
        print("Correct! you win congrats buddy")
        print("It took you", attempts, "tries")
        break  # stop the loop

    # if guess is too high
    elif guess > number:
        print("Too High")

    # if guess is too low
    else:
        print("Too low")
