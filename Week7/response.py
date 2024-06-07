from validator_collection import validators,checkers,errors

def main():
    print(check(input("Email:")))

def check(s):
    if checkers.is_email(s) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()