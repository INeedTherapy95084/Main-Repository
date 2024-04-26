numbers = []

while True:
    inp = input("Enter a number: \n")
    if inp.lower() == "done":
        break
    value = int(inp)
    numbers.append(value)
avg = sum(numbers) / len(numbers)
print("The avrage of the entered values is ", avg)