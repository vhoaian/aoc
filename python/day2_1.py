def get_input():
    with open("inputs/day2_1_2.inp") as inp:
        input = inp.read()
    return input

CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_a_config(conf):
    num, color = conf.split()
    num = int(num)
    if num > CONSTRAINTS.get(color):
        return False
    return True

def check_line(line):
    game, configs = line.split(": ")
    _, game = game.split(" ")
    game = int(game)

    configs = configs.split("; ")
    for config in configs:
        if all(map(check_a_config, config.split(", "))) == False:
            return 0
    return game

inp = get_input()
s = 0
for line in inp.split('\n'):
    s+=check_line(line)
print(s)