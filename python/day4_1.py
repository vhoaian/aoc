def get_input():
    with open("inputs/day4_1_2.inp") as inp:
        input = inp.read()
    return input

def count_numbers(my_nums, winning_nums):
    return sum(map(lambda n: 1 if n in winning_nums else 0, my_nums))

def check_line(line):
    _, line = line.split(": ")
    winning_numbers, my_numbers = line.split(" | ")
    winning_numbers = list(map(int, winning_numbers.split()))
    my_numbers = list(map(int, my_numbers.split()))
    count = count_numbers(my_numbers, winning_numbers)
    return 0 if count == 0 else 2 ** (count - 1)

inp = get_input()
s = 0
for line in inp.split('\n'):
    s+=check_line(line)
print(s)