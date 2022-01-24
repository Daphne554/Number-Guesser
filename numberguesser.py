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
