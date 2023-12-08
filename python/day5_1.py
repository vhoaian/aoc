import functools


def get_input():
    with open("inputs/day5_1_1.inp") as f:
        return f.read()

def init_seed_dict(seeds):
    return functools.reduce(lambda acc, cur: acc | {cur: (int(cur), False) }, seeds, {})

def gen_mapping(d, dest, src, l):
    keys = list(d.keys())
    to_be_reviewed = list(map(lambda x: x[0], d.values()))
    for i in range(len(to_be_reviewed)):
        if src <= to_be_reviewed[i] <= src + l:
            _d = dest - src + to_be_reviewed[i]
            if not d[keys[i]][1]:
                d[keys[i]] = _d, True

inp = get_input()
lines = inp.split('\n')
my_dict = init_seed_dict(lines[0].split(': ')[1].split())

for line in lines[2:]:
    if len(line) == 0:
        continue
    if line[0].isdigit():
        gen_mapping(my_dict, *map(int, line.split()))
        print(my_dict)
    else:
        for k in my_dict.keys():
            value, _ = my_dict[k]
            my_dict[k] = value, False

print(min(my_dict.values(), key=lambda v: v[0])[0])
