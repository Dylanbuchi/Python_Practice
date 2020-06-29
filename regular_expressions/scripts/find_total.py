import re

numbers = list()
total = 0

with open("regular_expressions/scripts/sum.txt") as file:
    for line in file:
        numbers += re.findall(r"([0-9]+)", line.strip())


for i in numbers:
    total += int(i)
print(total)
