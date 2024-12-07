with open('input.txt') as f:
    G = f.read().splitlines()

    # dimensions of the grid
R = len(G)
C = len(G[0])

start_r, start_c = None, None
start_coor = None
for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            start_r, start_c = r, c 

ans_1 = 0
ans_2 = 0


# loop through the grid and if an item has already been seen you know that you have cycled through
for i_r in range(R):
    for i_c in range(C):
        dir = 0  
        r, c = start_r, start_c  
        seen = set()
        seen_rc = set()
        # trace the path until the person goes out of bounds
        while True:
            if (r, c, dir) in seen:
                ans_2 += 1
                break
            seen.add((r, c, dir))
            seen_rc.add((r, c))
            dir_r, dir_c = [(-1, 0), (0, 1), (1, 0), (0, -1)][dir]
            rr, cc = r + dir_r, c + dir_c
            if not (0 <= rr < R and 0 <= cc < C):
                if G[i_r][i_c] == '#':
                    ans_1 = len(seen_rc)                
                break
            if G[rr][cc] == '#' or i_r == rr and i_c == cc:
                dir = (dir+1) % 4
            else:
                r, c = rr, cc

print(ans_1)  
print(ans_2)
