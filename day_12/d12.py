from collections import deque

with open('input.txt') as f:
    G = f.read().splitlines()


# function for calculating the perimiter of an area
def calc_perimeter(points):
    perim_counter = 0
    perimeter_dict = {}
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r, c in points:
        perim_counter += 4
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if (rr, cc) in points:
                perim_counter -= 1
            else:
                if (dr, dc) not in perimeter_dict:
                    perimeter_dict[(dr, dc)] = set()
                perimeter_dict[(dr, dc)].add((r, c))


    
    # calculate the number of sides in the polygon
    # check for every up and down left right how far you can expand
    # add expanded coors to the seen 
    side_counter = 0
    for dir, perim_coor in perimeter_dict.items():
        seen_sides = set()
        for (pr, pc) in perim_coor:
            if (pr, pc) not in seen_sides:
                side_counter += 1
                Q = deque([(pr, pc)])
                while Q:
                    rr, cc = Q.popleft()
                    if (rr, cc) in seen_sides:
                        continue
                    seen_sides.add((rr, cc))
                    for dr, dc in dirs:
                        r_r, c_c = rr + dr, cc + dc
                        if (r_r, c_c) in perim_coor:
                            Q.append((r_r, c_c))

    return perim_counter , side_counter

# code for finding the area's
R = len(G)
C = len(G[0])

area_perimeters = []
areas = []
seen = set()
for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        area = {(r, c)}
        Q = deque([(r, c)])
        # get the directions for certain coordinates

        while Q:
            rr, cc = Q.popleft()
            for i, (r_r, c_c) in enumerate([(rr + 1, cc), (rr - 1, cc), (rr, cc + 1), (rr, cc - 1)]):
                if r_r < 0 or r_r >= R or c_c < 0 or c_c >= C:
                    continue
                if (r_r, c_c) in area:
                    continue
                if G[r][c] != G[r_r][c_c]:
                    continue
                Q.append((r_r, c_c))
                area.add((r_r, c_c))

        seen |= area
        areas.append(area)

p1 = 0
p2 = 0
for plot in areas:
    perim_size, side_size = calc_perimeter(plot)
    p1 += len(plot) * perim_size
    p2 += len(plot) * side_size


print(p1, p2)