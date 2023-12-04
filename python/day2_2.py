import functools


def get_input():
    with open("inputs/day2_2_2.inp") as inp:
        input = inp.read()
    return input

def merge_configs(configs):
    res = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for config in configs:
        for color, num in config.items():
            if res.get(color) < num:
                res[color] = num
    return res

def construct_config(conf):
    num, color = conf.split(" ")
    return {color: int(num)}

def check_line(line):
    _, configs = line.split(": ")

    configs = configs.split("; ")
    configs_in_dicts = []
    for config in configs:
        configs_in_dicts.append(merge_configs(map(construct_config, config.split(", "))))

    return merge_configs(configs_in_dicts)

inp = get_input()
s = 0
for line in inp.split('\n'):
    s += functools.reduce(lambda a, b: a*b, check_line(line).values(), 1)
print(s)