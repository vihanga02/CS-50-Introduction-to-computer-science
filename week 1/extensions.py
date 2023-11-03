def main():
    file = input("File name: ")
    ex(file)

def ex(n):
    nn = n.split('.')
    if nn[-1] == "gif":
        return print("image/gif")
    elif nn[-1] == "jpg" or nn[-1] == "jpeg":
        return print("image/jpeg")
    elif nn[-1] == "png":
        return print("image/png")
    elif nn[-1] == "pdf":
        return print("application/pdf")
    elif nn[-1] == "txt":
        return print("text/plain")
    elif nn[-1] == "zip":
        return print("application/zip")
    else:
        return print("wrong extention")

main()