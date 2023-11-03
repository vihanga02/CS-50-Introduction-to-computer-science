#import the regular expression module
import re

def main():
    #print the return value of parse function
    print(parse(input("HTML:")))

def parse(s):
    #checking the url is in a correct pattern
    url = re.search(r'src="(https?://)?(www\.)?(youtube)\.com/embed/(.+)"',s)
    if url:
        #if the url is in a correct pattern,extract the youtube ID
        return f"https://youtu.be/{url.group(4)}"
    else:
        #if the url is in a incorrect pattern retun the error massege
        return "HTML code is not a correct youtube url"
    
if __name__ == "__main__":
    main()