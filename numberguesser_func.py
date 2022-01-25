import random
name = input("Type your guesser name: ")
print(f"Hi {name} . Welcome to the number guesser game!!!")
option = input("Type user for user mode and computer for computer mode: ").lower()
if option == "user":
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
        print(guess(10))

elif option == "computer":
    def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != "c":
            if low != high:
                guess = random.randint(low,high)
            else:
                guess = low
            feedback = input(f"Is {guess} it low , high or correct? ")
            if feedback == "L":
                guess = guess() + 1
            elif feedback == "H":
                guess = guess() - 1

        print(f"The computer guessed your number {guess} correctly")
    print(computer_guess(10))
else:
    print("Type 'user' or 'computer' to access a mode: ")