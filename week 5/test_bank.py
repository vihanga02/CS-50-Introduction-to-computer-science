def main():
    greet = input("greeting:")
    print(value(greet))

def value(greeting):
    n = greeting.lower()
    if n[0] == 'h':
        if greeting == 'hello':
            return '0'
        else:
            return '20'
    else:
        return '100'
    
if __name__ == "__main__":
    main()