def removechars(str, remove):
    print(str.translate({ord(i): None for i in remove}))

str = input("Type a word or sentance:\n")
remove = input("Type the word or the letters you want to remove:\n")

removechars(str, remove)