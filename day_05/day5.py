from functools import cmp_to_key


with open('input.txt') as f:
    ordering_rules, updates = f.read().split('\n\n')
    updates_ = [list(map(int, line.split(','))) for line in updates.splitlines()]
    
    # rework part 2
    rules_2 = [tuple(map(int, line.split("|"))) for line in ordering_rules.split("\n")]
    updates_2 = [list(map(int, line.split(","))) for line in updates.split("\n")]

    
dict_rules = {}
for rule in ordering_rules.split('\n'):
    dom, sub  = rule.split('|')
    dom, sub = int(dom), int(sub)
    if dom not in dict_rules:
        dict_rules[dom] = [sub]
    else:
        dict_rules[dom].append(sub)

c1 = 0
bad_index = []
for idx, update in enumerate([list(map(int, line.split(','))) for line in updates.splitlines()]):
    is_good = True
    for i, num in enumerate(update):
        if num not in dict_rules and i != len(update) - 1:
            is_good = False
            break
        elif num not in dict_rules and i == len(update) - 1:
            break
        to_check = update[i+1:]
        next_pages = dict_rules[num]
        for check in to_check:
            if check not in next_pages:
                is_good = False
                break
        if not is_good:
            break
    if is_good:
        c1 += update[len(update) // 2]
    else:
        bad_index.append(idx)

print(c1)

# brute force not possible lmao



# part 2
# c2 = 0
# print(bad_index)
# for i in bad_index:
#     for comb in list(permutations(updates_[i]))[1:]:
#         is_good = True
#         for i, num in enumerate(comb):
#             if num not in dict_rules and i != len(comb) - 1:
#                 is_good = False
#                 break
#             elif num not in dict_rules and i == len(comb) - 1:
#                 break
#             to_check = comb[i+1:]
#             next_pages = dict_rules[num]
#             for check in to_check:
#                 if check not in next_pages:
#                     is_good = False
#                     break
#             if not is_good:
#                 break
#         if is_good:
#             c2 += comb[len(comb) // 2]
#             break
# print(c2)

# here we go again

#  kan ook ook al wegfilter door part 1 te sorten maar ik was te lui
c2 = 0
print(rules_2)
key = cmp_to_key(lambda a, b: -1 if (a, b) in rules_2 else 1)
for i in bad_index:
    update = updates_2[i]
    print(sorted(update, key = key), update)    
    update.sort(key = key)
    c2 += update[len(update) // 2]

print(c2)