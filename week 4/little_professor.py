import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l > 3 or l < 1:
                pass
            else:
                return l
        except ValueError:
            pass

def generate_integer(n):
    score = 0
    attempt = 0
    Q_no = 0
    while Q_no < 10:
        try:
            x = random.randint(0,10**n)
            y = random.randint(0,10**n)
            while attempt < 3:
                z = int(input(f"{x} + {y} = "))
                if z == x + y:
                    print("correct")
                    Q_no += 1
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
                if attempt == 3:
                    print(x+y)
                    Q_no += 1
                    attempt = 0
                    break
            pass
        except ValueError:
                pass

    if Q_no == 10:
        print(f"Score = {score} /10")
        return 0

if __name__ == "__main__":
    main()