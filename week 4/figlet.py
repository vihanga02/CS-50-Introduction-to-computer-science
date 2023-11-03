from pyfiglet import Figlet
import sys

#check if invalied argument
if sys.argv[1] not in ["-f","-font"]:
    sys.exit("invalied input")

#prompt user for a imput
a = input("phres:")

#initialize figlet modules and setting a font
f = Figlet(font=sys.argv[2])

#prinnt the output
print(f.renderText(a))