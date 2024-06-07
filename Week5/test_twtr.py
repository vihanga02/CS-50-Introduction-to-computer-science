import test1

def main():
    user_input = input("Enter a prhase:")
    print(shorten(user_input))

def shorten(word):
    vowels = ["a","e","i","o","u"]
    no_vowels = ""
    for n in word:
        if n.lower() not in vowels:
            no_vowels += n
    return no_vowels
            
if __name__ == "__main__":
    main()