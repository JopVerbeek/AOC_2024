import re
from itertools import product

with open('input.txt') as f:
    lines = f.read().splitlines()

extracted_numbers = []
for line in lines:
    # print(line)
    # Use regular expression to find all numbers in the line
    numbers = re.findall(r'\d+', line)
    # Convert the extracted numbers from strings to integers
    numbers = [int(num) for num in numbers]
    extracted_numbers.append(numbers)


operators = ['*', '+', '|']


counter = 0
for nums in extracted_numbers:
    target = nums[0]
    num_list = nums[1:]
    

    operators_combs = list(product(operators, repeat=len(num_list)-1))
    for comb in operators_combs:
        count = num_list[0]
        for i, num in enumerate(num_list[1:]):
            if comb[i - 1] == '*':
                count *= num
            elif comb[i - 1] == '+':
                count += num
            elif comb[i - 1] == '|':
                count = int(str(count) + str(num))

        if count == target:
            counter += target
            break

print(counter)




