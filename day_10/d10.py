from collections import deque

with open('input.txt') as f:
    G = [[int(num) for num in line] for line in f.read().splitlines()]

R = len(G)
C = len(G[0])

trailheads = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            trailheads.append((r, c))

def get_trails(grid, r, c):
    # implement simple bfs for finding the paths
    D = deque([(r, c)])
    seen = {(r, c)}
    counter = 0
    while len(D) > 0:
        rr, cc = D.popleft()
        for r_r, c_c in [(rr-1, cc), (rr+1, cc), (rr, cc-1), (rr, cc + 1)]:     
            if r_r < 0 or r_r >= R or c_c < 0 or c_c >= C:
                continue
            if grid[r_r][c_c] != grid[rr][cc] + 1:
                continue
            #  uncomment line 28, 29 to get the answer to part 1
            # if (r_r, c_c) in seen:
            #     continue
            seen.add((r_r, c_c))

            if grid[r_r][c_c] == 9:
                counter += 1

            D.append((r_r, c_c))

    return counter

total = 0
for r, c in trailheads:
    total += get_trails(G, r, c)

print(total)

    