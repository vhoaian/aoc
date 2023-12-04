def get_input():
    with open("inputs/day4_2_2.inp") as inp:
        input = inp.read()
    return input

def count_numbers(my_nums, winning_nums):
    return sum(map(lambda n: 1 if n in winning_nums else 0, my_nums))

def find_count_of_a_line(line):
    _, line = line.split(": ")
    winning_numbers, my_numbers = line.split(" | ")
    winning_numbers = list(map(int, winning_numbers.split()))
    my_numbers = list(map(int, my_numbers.split()))
    count = count_numbers(my_numbers, winning_numbers)

    return count

def do_it(line_num, counts, winning_numbers):
    count = winning_numbers[line_num]
    counts[line_num] += 1
    current_count = counts[line_num]
    for next_line_num in range(line_num + 1, line_num + count + 1):
        if next_line_num > len(counts) - 1:
            break
        counts[next_line_num] += 1*current_count

inp = get_input()
s = 0
lines = inp.split('\n');
counts = [0]*(len(lines) + 1)
winning_numbers = [0]
for line in lines:
    winning_numbers.append(find_count_of_a_line(line))

for i in range(1, len(lines) + 1):
    do_it(i, counts, winning_numbers)

print(sum(counts))