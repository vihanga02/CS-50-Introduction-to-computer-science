#import re 
import re

#define a main function
def main():
    #print the return value of validate function
    print(validate(input("IPv4 Address: ")))

#define a function called validate
def validate(IP):
    #split the IP address to 4 parts
    ip = IP.split(".")
    #search the regular expression pattern
    matches = re.search(r"^(\d*)\.(\d*)\.(\d*)\.(\d*)$",IP)
    #check the length of the splited ip address
    if len(ip) != 4:
        return False
    #check the ip address whether in correct pattern
    elif matches:  
        if 0<=int(matches.group(1))<256 and 0<=int(matches.group(2))<256 and 0<=int(matches.group(3))<256 and 0<=int(matches.group(4))<256:
            return True
        else:
            return False

#recall the main function
if __name__ == "__main__":
    main()


