with open('input.txt') as f:
    G = f.read().splitlines()

R = len(G)
C = len(G[0])

antennas = {}

for r in range(R):
    for c in range(C):
        if G[r][c] != '.':
            if G[r][c] not in antennas:
                antennas[G[r][c]] = []
            antennas[G[r][c]].append((r, c))

print(antennas)

antinodes = set()

for array in antennas.values():
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                r1, c1 = array[i]
                r2, c2 = array[j]
                #  PART 2
                change_r = r1 - r2
                change_c = c1 - c2
                r = r1
                c = c1

                # antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                # antinodes.add((2 * r2 - r1 , 2 * c2 - c1))
                while 0 <= r < R and 0 <= c < C:
                    antinodes.add((r, c))
                    r += change_r
                    c += change_c

antinodes_in_bounds = [1 for r, c in antinodes if 0 <= r < R and 0 <= c < C]
print(len(antinodes_in_bounds))
            






















