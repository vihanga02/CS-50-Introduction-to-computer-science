from tabulate import  tabulate
import sys
import csv

def main():
    if is_valied_cmd_line_arg(sys.argv):
        list = get_line(sys.argv[1])
        print(tabulate(list,headers="keys",tablefmt="grid"))
        #print(list)
def is_valied_cmd_line_arg(arg):
    try:
        if len(arg) != 2:
            sys.exit("Enter a valied argument")
    except FileNotFoundError:
        sys.exit("Enter a valied file name")
    return True

def get_line(csvf):
    ls = []
    with open(csvf) as file:
        lines = csv.DictReader(file)
        for row in lines:
            ls.append({"Regular Prizza":row["Regular Pizza"] , "Small":row["Small"] , "Large":row["Large"]})
            #ls.append(row)
    return ls

if __name__ == "__main__":
    main()