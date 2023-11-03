dict1 = {}

while True:
    try:
        item = input().title().strip().upper()
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1
    except EOFError:
        sdict = dict(sorted(list(dict1.items())))
        for i in sdict:
            print(i,sdict[i])
        break
    except KeyError:
        pass