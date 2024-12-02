with open("input.txt") as f:
    lines = [list(map(int, line.split())) for line in f.read().splitlines()]


def gradual_difference(data):

    for i in range(len(data)):
        if i > 0:
            abs_diff = abs(data[i - 1] - data[i])
            if abs_diff > 3 or abs_diff < 1 or abs_diff == 0:
                return False
    return True


def inc_dec(data):
    inc_dec = []
    for i in range(len(data)):
        if i > 0:
            if data[i - 1] - data[i] < 0:
                inc_dec.append("inc")
            elif data[i - 1] - data[i] == 0:
                inc_dec.append("same")
            else:
                inc_dec.append("dec")
            if len(set(inc_dec)) > 1:
                return False
    return True


def get_tweaked(line):
    return [line[:i] + line[i + 1 :] for i in range(len(line))]


c = 0
for data in lines:
    if gradual_difference(data) and inc_dec(data):
        c += 1
    else:
        for subset in get_tweaked(data):
            if gradual_difference(subset) and inc_dec(subset):
                c += 1
                break
print(c)
