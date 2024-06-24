numbers: list[int | float] = []

while True:
    inp: int | str = input("Enter a number: \n")
    if inp.lower() == "done":
        break
    value: int = int(inp)
    numbers.append(value)
avg: int | float = sum(numbers) / len(numbers)
print("The avrage of the entered values is ", avg)