import sys
import inflect

#define variables
p = inflect.engine()
lt = []

#infinite loop till broken
while True:
    try:
        #get the user inputs
        name = str(input("Name:").strip().title())

        #if invalieed names,exit programm
        if len(name) < 1:
            sys.exit()
        #append names to the array
        lt.append(name)

    #except control-D was passed
    except EOFError:
        print(f"Adieu,adieu to {p.join(lt)}")
        break