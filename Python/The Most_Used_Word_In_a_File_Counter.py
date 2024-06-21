import os

os.system("cls")
file_name = input("Enter a file path: \n")

try:
    with open(file_name, encoding='utf-8') as file:
        file_content = file.readlines()
except FileNotFoundError:
    print("ERROR: File name ", file_name, " cannot be opend")
    quit()

counts = {}

for lines in file_content:
    words = lines.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

srted_Words = sorted([(v,k) for k,v in counts.items()])

os.system('cls')

print("\nThe top 10 most used words are: \n")

srted_Words.reverse()

biggestword = None
biggestcount = None

for v,k in srted_Words[:10]:
    if biggestword is None and biggestcount is None:
        biggestword = (k)
        biggestcount= (v)
    print(k, ":", v, "times")
        
print("\nThe most used word is \"", biggestword,"\" which is used" , biggestcount,  "number of times.")