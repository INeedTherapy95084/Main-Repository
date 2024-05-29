def reverse_string(string):
    s = string.split()[::-1]
    l = []
    
    for i in s:
        l.append(i)
        
    return l

string = input("Type a sentance:\n")

print(" ".join(reverse_string(string)))