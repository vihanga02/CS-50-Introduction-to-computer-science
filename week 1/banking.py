def main():
    greet = str(input("Enter a greeting: "))
    money(greet)

def money(n):

    if n[0] == 'h' or n[0] == 'H':
        nn = n.split(' ')  
        match nn[0]:
            case "hello":
                return print("0$")
            case _:
                return print("20$")
    else:
        return print("100$")
        
main()
 


