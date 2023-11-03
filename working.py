#importing sys and re modules
import re,sys

def main():
    #print the return value of the convert function
    print(convert(input("Hours: ")))

def convert(s):
    #searchin that is the input in a correct pattern
    time = re.search(r"^([0-9]{0,2})(:?)([0-9]{0,2}) (AM|PM) to ([0-9]{0,2})(:?)([0-9]{0,2}) (AM|PM)$",s)
    if time:
        #split time in to two parts
        start,end = s.split("to")
        if "AM" in start:
            #removing the AM part
            start = start.replace("AM","")
            if ":" in start:
                #spliting hours and minutes
                start = start.split(":")
                if 0<=int(start[0])<=12 and 0<=int(start[1])<60:
                    #if start in a valied pattern,defining starting time
                    st = f"{int(start[0]):02}:{int(start[1]):02}"
                else:
                    #if start in a invalied pattern,exit!
                    sys.exit("Invalied")
            else:
                if 0<=int(start)<=12:
                    st = f"{int(start):02}:00"
                else:
                    sys.exit("Invalied")
        else:
            start = start.replace("PM","")
            if ":" in start:
                start = start.split(":")
                if 0<=int(start[0])<=12 and 0<=int(start[1])<60:
                    st = f"{int(start[0])+12:02}:{int(start[1]):02}"
                else:
                    sys.exit("Invalied")
            else:
                if 0<=int(start)<=12:
                    st = f"{int(start)+12:02}:00"
                else:
                    sys.exit("Invalied")

        if "AM" in end:
            end = end.replace("AM","")
            if ":" in end:
                end = end.split(":")
                if 0<=int(end[0])<=12 and 0<=int(end[1])<60:
                    en = f"{int(end[0]):02}:{int(end[1]):02}"
                else:
                    sys.exit("Invalied")
            else:
                if 0<=int(end)<=12:
                    en = f"{int(end):02}:00"
                else:
                    sys.exit("Invalied")
        else:
            end = end.replace("PM","")
            if ":" in end:
                end = end.split(":")
                if 0<=int(end[0])<=12 and 0<=int(end[1])<60:
                    en = f"{int(end[0])+12:02}:{int(end[1]):02}"
                else:
                    sys.exit("Invalied")
            else:
                if 0<=int(end)<=12:
                    en = f"{int(end)+12:02}:00"
                else:
                    sys.exit("Invalied")
        #returning the time to main function
        return f"{st} to {en}"

    else:
        return "Please Enter in a valied time"
    
if __name__=="__main__":
    main()


