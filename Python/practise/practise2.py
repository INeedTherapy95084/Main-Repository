def swappos(newlist, pos1, pos2):
    pos1 -= 1
    pos2 -= 1
    temp = newlist[pos1]
    newlist[pos1] = newlist[pos2]
    newlist[pos2] = temp
    return newlist

mainlist = [1, 2, 3, 4, 5]
pos1 = int(input("type the position of the first index you want to change:\n"))
pos2 = int(input("type the position of the second index you want to change:\n"))
print(swappos(mainlist, pos1, pos2))