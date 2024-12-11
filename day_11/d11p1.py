with open('input.txt') as f:
    stones = list(map(int, f.read().split()))

for i in range(25):
    blink_stones = []
    for stone in stones:
        if stone == 0:
            blink_stones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            stone = str(stone)
            blink_stones.append(int(stone[:len(stone) // 2]))
            blink_stones.append(int(stone[len(stone) // 2:]))            
        else:
            blink_stones.append(stone * 2024)
    stones = blink_stones
    
print(len(stones))
