def construct_using_inp(input):
    symbols = []
    lines = input.split()
    height = len(lines)
    width = len(lines[0])
    symbols.append(['.']*(width+2))
    for line in input.split():
        symbols.append(['.'] + list(line) + ['.'])
    symbols.append(['.']*(width+2))
    return symbols, width, height

def print_matrix(matrix):
    for i in matrix:
        print("".join(i))

def get_input():
    with open("inputs/day3_1_2.inp") as inp:
        input = inp.read()
    return input

def is_valid_number(matrix, x_fr, x_to, line_num):
    for line in matrix[line_num-1:line_num+2]:
        for c in line[x_fr-1:x_to+2]:
            if c != '.' and not c.isdigit():
                return True
    return False

def find_right_boundary(matrix, line_num, idx):
    if not matrix[line_num][idx].isdigit():
        return -1
    while matrix[line_num][idx].isdigit():
        idx+=1
    return idx-1

matrix, width, height = construct_using_inp(get_input())
# print_matrix(matrix)

sum = 0
i = 1
while i < height + 1:
    j=1
    while j < width + 1:
        found_idx = find_right_boundary(matrix, i, j)
        if found_idx > 0:
            num = "".join(matrix[i][j:found_idx+1])
            if is_valid_number(matrix, j, found_idx, i):
                sum += int(num)
            j = found_idx

        j+=1
    i+=1
print(sum)

