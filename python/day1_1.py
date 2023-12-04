def get_input():
    with open("inputs/day1_1_2.inp") as inp:
        input = inp.read()
    return input

def identify_number(line):
    num_chrs = []
    for i in range(len(line)):
        if line[i].isdigit():
            num_chrs.append(line[i])
            break;
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            num_chrs.append(line[i])
            break;
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

