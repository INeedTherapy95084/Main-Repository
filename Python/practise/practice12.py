dct = {"yash": 20, "tahsin": 27, "junaid": 30, "razzo": 29}

dctKeys = list(dct.keys())
dctKeys.sort()
dctValues = list(dct.values())
dctValues.sort()

sorted_dict = {}

count = 0

for i in dctKeys:
    while True:
        sorted_dict[i] = dctValues[count]
        count += 1
        break

print(sorted_dict)
