# start is an @ in the data and boxes are denoted as an O and the wall is #

with open('input.txt') as f:
    G, moves = f.read().split('\n\n')
    G, moves = [list(line) for line in G.splitlines()], moves.replace('\n', '')


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
    cr = r
    cc = c
    tb_moved = []
    move = True
    while True:
        cr += dr
        cc += dc
        if G[cr][cc] == '#':
            move = False
            break            
        if G[cr][cc] == 'O':
            tb_moved.append((cr, cc))
        if G[cr][cc] == '.':
            break
    if move:
        G[r][c] = '.'
        G[r + dr][c + dc] = '@'
        for box in tb_moved:
            br, bc = box
            G[br + dr][bc + dc] = 'O'
        r, c = r + dr, c + dc

gps_sum = 0


for rr in range(R):
    for cc in range(C):
        if G[rr][cc] == 'O':
            gps_sum += rr * 100 + cc

print(gps_sum)