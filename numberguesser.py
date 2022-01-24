import random

range_limit = input("Type a limit for number range: ")

if range_limit.isdigit():
    range_limit = int(range_limit)

elif range_limit <= 0:
    print("Type a number larger than zero")
    quit()

else:
    print("Type a number next time!")
    quit()

random_number = random.randint(0, range_limit)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Type in your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time. ")
        continue
    if user_guess == random_number:
        print("You guessed right!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    elif user_guess < random_number:
        print("You were below the number")

print(f"You got it in {str(guesses)} guess(es)!!")