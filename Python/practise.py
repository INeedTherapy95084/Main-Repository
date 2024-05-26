def swaplist(newlist):
    size = len(newlist)
    
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

mainlist = [1, 2, 3]
print(mainlist)