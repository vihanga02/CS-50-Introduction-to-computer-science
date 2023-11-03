import random

while True:
    try:
        level = int(input("Level:"))
        number = random.randint(1,level)
        break
    except ValueError:
        print("level must be greater than 0")
        pass

while True:
    try:
        guess = int(input("Guess:"))
        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too Large")
            pass
        elif guess < 0:
            print("Guess must be greater than 0")
            pass
        else:
            print("Too small")
            pass
    except ValueError:
        print("Invalied input")
        pass