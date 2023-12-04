def get_input():
    with open("inputs/day1_2_2.inp") as inp:
        input = inp.read()
    return input

OTHER_NUMS = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]
NUMS = list(map(lambda t: t[0], OTHER_NUMS))
def to_num(num_str):
    idx = NUMS.index(num_str)
    return OTHER_NUMS[idx][1] if idx >= 0 else None

def find_the_first_in_str(line):
    first_found = map(lambda num: (line.find(num), num), NUMS)
    first_found = filter(lambda t: t[0] >= 0, first_found)
    first_found = list(first_found)
    if len(first_found) == 0:
        return len(line),""
    first_found = min(first_found, key=lambda t: t[0])

    return first_found[0], str(to_num(first_found[1]))

def find_the_last_in_str(line):
    last_found = map(lambda num: (line.rfind(num), num), NUMS)
    last_found = filter(lambda t: t[0] >= 0, last_found)
    last_found = map(lambda t: (t[0], t[1], t[0] + len(t[1])), last_found)
    last_found = list(last_found)
    if len(last_found) == 0:
        return -1,""
    last_found = max(last_found, key=lambda t: t[2])

    return last_found[0], str(to_num(last_found[1]))

def identify_number(line):
    num_chrs = []
    first_in_num_idx = -1
    last_in_num_idx = -1

    for i in range(len(line)):
        if line[i].isdigit():
            num_chrs.append(line[i])
            first_in_num_idx = i
            break
    first_in_str_idx, this_str = find_the_first_in_str(line)
    if first_in_num_idx == -1 or first_in_num_idx > first_in_str_idx:
        if first_in_num_idx != -1:
            num_chrs.pop()
        num_chrs.append(this_str)

    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            num_chrs.append(line[i])
            last_in_num_idx = i
            break
    last_in_str_idx, this_str = find_the_last_in_str(line)
    if last_in_num_idx == -1 or last_in_num_idx < last_in_str_idx:
        if last_in_num_idx != -1:
            num_chrs.pop()
        num_chrs.append(this_str)

    if len(num_chrs) != 2:
        raise Exception("What is going on here???")
    return int("".join(num_chrs))

def construct_using_input(input):
    nums = []
    for line in input.split('\n'):
        num = identify_number(line)
        nums.append(num)
    return nums

print(sum(construct_using_input(get_input())))


