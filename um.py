#import re,sys module
import re,sys

def main():
    #print the um count
    print(count(input("Text:")))

def count(s):
    #count how many um in the string
    hm = len(re.findall(r'(\b(um)|(Um)|(UM)\b)',s))
    return hm

if __name__ == "__main__":
    main()


