import re
from math import prod

with open("input.txt") as f:
    lines = f.read().splitlines()


# part1
c = 0
for line in lines:
    for mult in re.findall(r"mul\(\d+,\d+\)", line):
        c += prod(list(map(int, re.findall(r"\d+", mult))))
print(c)

# part2
c2 = 0
state = True
for line in lines:
    for op in re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line):
        if op == "do()":
            state = True
        elif op == "don't()":
            state = False
        elif state:
            c2 += prod(list(map(int, re.findall(r"\d+", op))))
print(c2)
