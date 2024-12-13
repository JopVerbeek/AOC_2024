from functools import cache
import time
start_time = time.time()



with open('input.txt') as f:
    stones = list(map(int, f.read().split()))

@cache
def stone_counter(steps, stone):
    if steps == 0:
        return 1
    if stone == 0:
        return stone_counter(steps - 1, 1)
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        return stone_counter(steps - 1, int(stone[:len(stone) // 2])) + stone_counter(steps - 1, int(stone[len(stone) // 2:]))
    return stone_counter(steps - 1, stone * 2024)

stone_count = 0
for stone in stones:
    stone_count += stone_counter(75, stone)     

print(stone_count)

print("Process finished --- %s seconds ---" % (time.time() - start_time))