import sys
sys.setrecursionlimit(15000)

with open('input.txt') as f:
    files = f.read().replace('\n', '')

disk = []
counter = 0
count = 0

for i, num in enumerate(files, start=1):
    counter += 1
    if i%2 != 0:
        disk.extend([count] * int(num))
    else:
        disk.extend([-1] * int(num))
    if  counter == 2:
        count += 1
        counter = 0


for i in [i for i, char in enumerate(disk) if char == -1]:
    while disk[-1] == -1:
        disk.pop()
    if i >= len(disk):
        break
    disk[i] = disk.pop()

print(sum(i * num for i, num in enumerate(disk)))


