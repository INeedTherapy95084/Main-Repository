def swappos(newlist, pos1, pos2):
    pos1 -= 1
    pos2 -= 1
    temp = newlist[pos1]
    newlist[pos1] = newlist[pos2]
    newlist[pos2] = temp
    return newlist

mainlist = [1, 2, 3, 4, 5]
while True:
    pos1 = input("type the position of the first index you want to change:\n")
    try:
        pos1 = int(pos1)
        if pos1 > 0:
            break
        else:
            continue
    except:
        continue
    
while True:
    pos2 = input("type the position of the second index you want to change:\n")
    try:
        pos2 = int(pos2)
        if pos2 > 0:
            break
        else:
            continue
    except:
        continue
    
print(swappos(mainlist, pos1, pos2))