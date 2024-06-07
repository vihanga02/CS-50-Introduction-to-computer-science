ad = 50
print("Amount Due:50")
while ad > 0:
    ic = int(input("Insert Coin:"))
        
    if ic == 5:
        ad = ad - ic
        if ad > 0:
            print("Amount Due:"+str(ad))
        else:
            co = 0 - ad
            print("Change Owend:"+str(co))
            break
        
    elif ic == 10:
        ad = ad - ic
        if ad > 0:
            print("Amount Due:"+str(ad))
        else:
            co = 0 - ad
            print("Change Owend:"+str(co))
            break
    elif ic == 25:
        ad = ad - ic
        if ad > 0:
            print("Amount Due:"+str(ad))
        else:
            co = 0 - ad
            print("Change Owend:"+str(co))
            break
    else:
        print("Enter a valied coin!")
        break
