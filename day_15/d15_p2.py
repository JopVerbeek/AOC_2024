from copy import deepcopy

with open('input.txt') as f:
    G, moves = f.read().split('\n\n')
    G, moves = [list(line) for line in G.splitlines()], moves.replace('\n', '')


def expand_grid(grid):
    new_grid = []
    for line in grid:
        new_line = []
        for item in line:
            if item == '@':
                new_line.extend(['@', '.'])
            elif item == 'O':
                new_line.extend(['[', ']'])
            else:
                new_line.extend([item, item])
        new_grid.append(new_line)
    return new_grid


G = expand_grid(G)
for line in G:
    print(''.join(line))
R = len(G)
C = len(G[0])

# find start pos robot
start_pos = None
for r in range(R):
    for c in range(C):
        if G[r][c] == '@':
            start_pos = (r, c)
            break

r, c = start_pos
for move in moves:
    dr = -1 if move == '^' else 1 if move == 'v' else 0
    dc = 1 if move == '>' else -1 if move == '<' else 0
    tb_moved = [(r, c)]
    move = True
    for cr, cc in tb_moved:
        nr = cr + dr
        nc = cc + dc
        if (nr, nc) in tb_moved: continue
        char = G[nr][nc]
        if char == '#':
            move = False
            break
        if char == '[':
            tb_moved.append((nr, nc))
            tb_moved.append((nr, nc + 1))
        if char == ']':
            tb_moved.append((nr, nc))
            tb_moved.append((nr, nc - 1))
    if move:
        GC = [list(row) for row in G]
        G[r][c] = '.'
        G[r + dr][c + dc] = '@'
        for box in tb_moved[1:]:
            br, bc = box
            G[br][bc] = '.'
        for box in tb_moved[1:]:
            br, bc = box
            G[br + dr][bc + dc] = GC[br][bc]
        r, c = r + dr, c + dc

gps_sum = 0
for rr in range(R):
    for cc in range(C):
        if G[rr][cc] == '[':
            gps_sum += rr * 100 + cc

print(gps_sum)