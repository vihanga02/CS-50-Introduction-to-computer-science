def main():
    dt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer(dt)

def answer(n):
    match n:
        case "42" | "forty-two" | "forty two" :
            return print("yes")
        case _:
           return print("no")
        
main()   