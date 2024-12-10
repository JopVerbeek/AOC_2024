with open('input.txt') as f:
    data = [int(num) for num in f.read().replace('\n', '')]

files = {}
empty_space = []

file_id = 0
position = 0
for i, char in enumerate(data):
    if i % 2 == 0:
        files[file_id] = (position, char)
        file_id += 1
    else:
        if char != 0:
            empty_space.append((position, char))
    position += char

while file_id > 0:
    file_id -= 1
    pos, size = files[file_id]
    for i, (start, length) in enumerate(empty_space):
        if start >= pos:
            break
        if size <= length:
            files[file_id] = (start, size)
            if size == length:
                empty_space.pop(i)
            else:
                empty_space[i] = (start + size, length - size)
            break

checksum = 0
for id, (pos, size) in files.items():
    for i in range(pos, pos + size):
        checksum += id * i

print(checksum)