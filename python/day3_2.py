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
    with open("inputs/day3_2_2.inp") as inp:
        input = inp.read()
    return input

def valid_gear(matrix, x, y):
    first_hint = -1,-1
    second_hint = -1,-1
    if matrix[y][x] != '*':
        return first_hint, second_hint
    line_i = y-1
    while line_i < y+2:
        line = matrix[line_i]
        c_i = x-1
        while c_i < x+2:
            c = line[c_i]
            if c.isdigit():
                if first_hint[0] == -1:
                    first_hint = c_i, line_i
                    c_i += 1
                    while line[c_i].isdigit():
                        c_i += 1
                elif second_hint[0] == -1:
                    second_hint = c_i, line_i
                    c_i += 1
                    while line[c_i].isdigit():
                        c_i += 1
                else:
                    print(first_hint, second_hint)
                    raise Exception("What is going on here!!!!!!")
            c_i += 1
        line_i += 1
    # if only one num was found, reset the first
    if second_hint[0] == -1:
        first_hint = -1, -1
    return first_hint, second_hint

def find_number_from_hint(matrix, x_hint, y_hint):
    if not matrix[y_hint][x_hint].isdigit():
        raise Exception("Hey it is not a valid hint? Joking me!!!")
    left_bound = right_bound = x_hint
    while matrix[y_hint][left_bound].isdigit():
        left_bound -= 1
    left_bound += 1
    while matrix[y_hint][right_bound].isdigit():
        right_bound += 1
    right_bound -= 1
    return int("".join(matrix[y_hint][left_bound:right_bound+1]))

matrix, width, height = construct_using_inp(get_input())
# print_matrix(matrix)

sum = 0
i = 1
while i < height + 1:
    j=1
    while j < width + 1:
        first_hint, second_hint = valid_gear(matrix, j, i)
        if first_hint[0] > 0 and second_hint[0] > 0:
            first_num = find_number_from_hint(matrix, first_hint[0], first_hint[1])
            second_num = find_number_from_hint(matrix, second_hint[0], second_hint[1])
            sum += first_num * second_num
        j+=1
    i+=1
print(sum)

