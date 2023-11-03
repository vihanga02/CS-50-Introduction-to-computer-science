def main():
    time = input("What is the time? ")

    mm = convert(time)
    
    if 7.0 <= mm <= 8.0:
        print("breakfast time")
    elif 12.0 <= mm <= 13.0:
        print("lunch time")
    elif 18.0 <= mm <= 19.0:
        print("dinner time")
    else:
        print("don't eat")

def convert(t):
    hours,minutes = t.split(":")

    time1 = float(hours) + float(minutes)/60
    return time1

main()