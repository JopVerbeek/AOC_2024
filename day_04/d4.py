with open('input.txt') as f:
    grid = f.read().splitlines()


# get the dimensions of the holy christmas grid
R = len(grid)
C = len(grid[0])

xmas_counter_1 = 0
xmas_counter_2 = 0
for r in range(R):
    for c in range(C):
        # part 1

        # horizontal
        if c + 3 < R and grid[r][c] == 'X' and grid[r][c + 1] == 'M' and grid[r][c + 2] == 'A' and grid[r][c + 3] == 'S':
            xmas_counter_1 += 1
        if c + 3 < R and grid[r][c] == 'S' and grid[r][c + 1] == 'A' and grid[r][c + 2]== 'M' and grid[r][c + 3] == 'X':
            xmas_counter_1 += 1
        # vertical
        if r + 3 < C and grid[r][c] == 'X' and grid[r + 1][c] == 'M' and grid[r + 2][c] == 'A' and grid[r + 3][c] == 'S':
            xmas_counter_1 += 1
        if r + 3 < C and grid[r][c] == 'S' and grid[r + 1][c] == 'A' and grid[r + 2][c] == 'M' and grid[r + 3][c] == 'X':
            xmas_counter_1 += 1
        # diagonal
        # dont go out op bounds on right
        if c + 3 < C and r + 3 < R and grid[r][c] == 'X' and grid[r + 1][c + 1] == 'M' and grid[r + 2][c + 2] == 'A' and grid[r + 3][c + 3] == 'S':
            xmas_counter_1 += 1
        if c + 3 < C and r + 3 < R and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 3][c + 3] == 'X':
            xmas_counter_1 += 1

        #  dont go out of bound on left
        if c + 3 < C and r - 3 >= 0  and grid[r][c] == 'X' and grid[r - 1][c + 1] == 'M' and grid[r - 2][c + 2] == 'A' and grid[r - 3][c + 3] == 'S':
            xmas_counter_1 += 1
        if c + 3 < C and r - 3 >= 0 and grid[r][c] == 'S' and grid[r - 1][c + 1] == 'A' and grid[r - 2][c + 2] == 'M' and grid[r - 3][c + 3] == 'X':
            xmas_counter_1 += 1

        # part 2
        # dont go out op bounds on right
        if r + 2 < R and c + 2 < C and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
            xmas_counter_2 += 1
        if r + 2 < R and c + 2 < C and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
            xmas_counter_2 += 1
        if r + 2 < R and c + 2 < C and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
            xmas_counter_2 += 1
        if r + 2 < R and c + 2 < C and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
            xmas_counter_2 += 1

print(xmas_counter_1)
print(xmas_counter_2)