def main():
    plate = input("Plates: ")
    if is_valied(plate):
        print("valied")
    else:
        print("invalied")

def is_valied(n):
    if 2 <= len(n) <= 6:
        for i in range(len(n)):
            if i<2:
                if n[i].isalpha():
                    continue
                else:
                    return False
            else:
                if n[i].isalpha():
                    continue
                elif n[i].isdigit:
                    if n[i] != "0":
                        if i == len(n)-1:
                            return True
                        else:
                            if n[i+1].isdigit:
                                continue
                            else:
                                return False
                    else:
                        return False
                else:
                    return False 
        return True
    else:
        return False

main()