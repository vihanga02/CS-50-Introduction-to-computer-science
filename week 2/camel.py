def main():
    camelCase = input("camelCase: ")
    snake_case(camelCase)

def snake_case(n):
    for character in n:
        if character.islower():
            print(character,end="")
        else:
            char1 = character.lower()
            char2 = "_" + char1
            print(char2,end="")
    return 0

main()