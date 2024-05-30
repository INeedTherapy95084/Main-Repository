def swappos(newlist, pos1, pos2):
    pos1 -= 1
    pos2 -= 1
    temp = newlist[pos1]
    newlist[pos1] = newlist[pos2]
    newlist[pos2] = temp
    return newlist

mainlist = [1, 2, 3, 4, 5]
while True:
    try:
        pos1 = int(input("type the position of the first index you want to change:\n"))
        if pos1 > 0:
            break
        else:
            continue
    except:
        continue
    
while True:
    try:
        pos2 = int(input("type the position of the second index you want to change:\n"))
        if pos2 > 0:
            break
        else:
            continue
    except:
        continue
    
print(swappos(mainlist, pos1, pos2))