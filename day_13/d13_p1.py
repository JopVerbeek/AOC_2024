import re

with open('input.txt') as f:
    machines = f.read().split('\n\n')

PRESSES = 100
total_costs = 0
for machine in machines:
    ba, bb, prize_loc = [list(map(int,(re.findall(r'\d+', line)))) for line in machine.splitlines()]
    ba_x, ba_y = ba
    bb_x, bb_y = bb
    p_x, p_y = prize_loc
    
    min_costs = 1_000_000
    
    for i in range(PRESSES + 1):
        for j in range(PRESSES + 1):
            if ba_x * i + bb_x * j == p_x and ba_y * i + bb_y * j == p_y:
                cost = i * 3 + j
                if cost < min_costs:
                    min_costs = cost

    total_costs += 0 if min_costs == 1_000_000 else min_costs

print(total_costs)



