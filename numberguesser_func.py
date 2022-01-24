import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Make a guess between 1 and {x}: "))
        if guess > random_number:
            print("Too high, try again")
        elif guess < random_number:
            print("Too low, try again")
        else:
            print("Good job! You guessed right!")

print(guess(7))

