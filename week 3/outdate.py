months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date:").strip()
        if date[0].isdigit():
            x,y,z = date.split("/")
            if 1<=len(x)<=2 and 1<=len(y)<=2 and len(z)==4 and 0<int(y)<=12:
                if int(y) == 1 or int(y)==3 or int(y)==5 or int(y)==7 or int(y)==8 or int(y)==10 or int(y)==12:
                    if 0<int(x)<= 31:
                        print(f"{z}-{y}-{x}")
                        break
                    else:
                        pass
                elif int(y) == 4 or int(y)==6 or int(y)==9 or int(y)==11:
                    if 0<int(x) <= 30:
                        print(f"{z}-{y}-{x}")
                        break
                    else:
                        pass
                elif y == 2:
                    if int(z)%4 == 0:
                        if 0<int(x)<=29:
                            print(f"{z}-{y}-{x}")
                            break
                        else:
                            pass
                    else:
                        if 0<int(x)<=28:
                            print(f"{z}-{y}-{x}")
                            break
                        else:
                            pass
        elif date[0].isalpha():
            x,y = date.split(",")
            x1,x2 = x.split(" ")
            y = y.strip()
            x1 = x1.title()
            if x1 in months:
                if 0<len(x2)<=2 and len(y)==4:
                    if int(months.index(x1))==0 or int(months.index(x1))==2 or int(months.index(x1))==4 or int(months.index(x1))==6 or int(months.index(x1))==7 or int(months.index(x1))==9 or int(months.index(x1))==11:
                        if 0<int(x2) <= 31:
                            print(f"{y}-{months.index(x1)+1}-{x2}")
                            break
                        else:
                            pass
                    elif int(months.index(x1))==3 or int(months.index(x1))==5 or int(months.index(x1))==8 or int(months.index(x1))==10:
                        if 0<int(x2) <= 30:
                            print(f"{y}-{months.index(x1)+1}-{x2}")
                            break
                        else:
                            pass
                    elif int(months.index('x1')) == 1:
                        if int(z)%4 == 0:
                            if 0<int(x2)<=29:
                                print(f"{y}-{months.index(x1)+1}-{x2}")
                                break
                            else:
                                pass
                        else:
                            if 0<int(x2)<=28:
                                print(f"{y}-{months.index(x1)+1}-{x2}")
                                break
                            else:
                                pass
    except ValueError:
        pass