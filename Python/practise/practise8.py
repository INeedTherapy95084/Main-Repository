def print_even_words(str):
    stentence = str.split()
    result = []
    
    for i in stentence:
        length = len(i)
        if length % 2 == 0:
            result.append(i)
        else:
            continue
        
    print(*result)

str = input("Type a word or sentence:\n")

print_even_words(str)