with open("input.txt") as f:
    inputs = [list(map(int, line.split("   "))) for line in f.read().splitlines()]

left_list, right_list = [], []
for left, right in inputs:
    left_list.append(left)
    right_list.append(right)

# q1
c1 = 0
for r, l in zip(sorted(left_list), sorted(right_list)):
    c1 += abs(r - l)
print(c1)

# q2
c2 = 0
for l in left_list:
    c2 += l * right_list.count(l)
print(c2)
