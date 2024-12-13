import re

# cant brute for like in part 1 so we will have to solve equations of both lines
# take into account that we need ints
with open('input.txt') as f:
    machines = f.read().split('\n\n')

cost = 0
for machine in machines:
    ba, bb, prize_loc = [list(map(int,(re.findall(r'\d+', line)))) for line in machine.splitlines()]
    ba_x, ba_y = ba
    bb_x, bb_y = bb
    p_x, p_y = prize_loc
    p_x, p_y = p_x + 10_000_000_000_000, p_y + 10_000_000_000_000

    a = (p_x * bb_y - p_y * bb_x) / (ba_x * bb_y - ba_y * bb_x)
    b = (p_x - ba_x * a) / bb_x

    if a % 1 == 0 and b % 1 == 0: # check if both b and a are ints
        cost += a * 3 + b

print(int(cost))