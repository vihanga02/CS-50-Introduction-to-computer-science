import csv
import sys

def main():
    if is_valied_command_line_argument(sys.argv):
        new_csv(sys.argv[1],sys.argv[2])

def is_valied_command_line_argument(arg):
    try:
        if len(arg) != 3:
            sys.exit("You must enter 2 csv file names in command line argument")
        elif arg[1].startswith(".csv",len(arg[1])-5,len(arg[1])):
            sys.exit("1st file is not a csv file")
        elif arg[2].startswith(".csv",len(arg[2])-5,len(arg[2])):
            sys.exit("2nd file is not a csv file")
    except FileNotFoundError:
        sys.exit("Enter a valied csv file")
    return True

def new_csv(arg1,arg2):
    ls = []
    with open(arg1) as file:
        lines = csv.DictReader(file)
        for _ in lines:
            ls.append(_)
        for line in ls:
            last,first = line['name'].split(",")
            first = first.replace(" ","")
            name1 = f"{first},{last}"
            with open(arg2,"a",newline="") as new:
                writer = csv.DictWriter(new,fieldnames=["Name" , "House"])
                writer.writerow({"Name":name1,"House":line['house']})
    return 0

if __name__ == "__main__":
    main()