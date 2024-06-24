import os

os.system("cls")
file_name: str = input("Enter a file path: \n")

try:
    with open(file_name, encoding='utf-8') as file:
        file_content: list[str] = file.readlines()
except FileNotFoundError:
    print("ERROR: File name ", file_name, " cannot be opend")
    quit()

counts: dict = {}

for lines in file_content:
    words: list[str] = lines.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

sorted_Words: list[tuple[None, None]] = sorted([(v,k) for k,v in counts.items()])

os.system('cls')

print("\nThe top 10 most used words are: \n")

sorted_Words.reverse()

for v,k in sorted_Words[:10]:
    if biggestword is None and biggestcount is None:
        biggestword: None = (k)
        biggestcount: None = (v)
    print(k, ":", v, "times")
        
print("\nThe most used word is \"", biggestword,"\" which is used" , biggestcount,  "number of times.")