import sys

def main():
    if is_valied_comand_line_argument(sys.argv):
        line = get_lines(sys.argv[1])
        print(count_lines(line))

def is_valied_comand_line_argument(argv):
    if len(argv) != 2:
        sys.exit("you must enter file name at the command line argument")
    else:
        arg = argv[1]
        if arg.startswith('.py',len(arg)-3,len(arg)):
            return True
        else:
            sys.exit("You must enter a python file name as a argument")

def get_lines(code):
    try:
        ls = []
        with open(code) as file:
            for line in file:
                ls.append(line)
    except FileNotFoundError:
        sys.exit("file not found")

    return ls

def count_lines(ls):
    count = 0
    for line in ls:
        if line.startswith('#') == False:
            if len(line) > 1:
                count += 1
    return count

if __name__ == "__main__":
    main()