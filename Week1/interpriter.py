def main():
    ex = input("expression: ")
    answer(ex)

def answer(n):
    x, y, z = n.split(" ")

    if y == "+": 
        return print(float(x)+float(z))
    elif y == "-":
        return print(float(x)-float(z))
    elif y == "/":
        return print(float(x)/float(z))
    elif y == "*":
        return print(float(x)*float(z))

main()