def main():
    x = get_fraction() 
    print(f"{x}%")

def get_fraction():
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            if int(x)/int(y) <= 0.01:
                return "E"
            elif int(x)/int(y) >= 0.99:
                return "F"
            else:
                z = round((int(x)/int(y))*100)
                return z

        except ValueError or ZeroDivisionError:
            print("Error")
            pass

main()