def get_input():
    with open("inputs/day5_1_1.inp") as f:
        return f.read()

def gen_mapping(dest, src, l):
    return src, src + l - 1, dest - src

inp = get_input()
lines = inp.split('\n')
seeds = list(map(int, lines[0].split(': ')[1].split()))
seeds = [
    (seeds[i], seeds[i] + seeds[i+1] - 1)
    for i in range(0, len(seeds), 2)
]

def apply_mapping(left, right, mapping):
    overlapped = []
    for left_mapping, right_mapping, delta in mapping:
        # Neu seed va mapping co giao nhau => tim ra vung giao nhau
        if not (right_mapping < left or left_mapping > right):
            overlapped.append((max(left_mapping, left), min(right_mapping, right), delta))

    for i, common in enumerate(overlapped):
        l, r, delta = common
        yield l + delta, r + delta

        if i < len(overlapped) - 1 and overlapped[i+1][0] > r + 1:
            yield r + 1, overlapped[i + 1][0] - 1

    if len(overlapped) == 0:
        yield left, right
        return

    if overlapped[0][0] != left:
        yield left, overlapped[0][0] - 1
    if overlapped[-1][1] != right:
        yield overlapped[-1][1] + 1, right

current_maps = []
final_maps = []
is_generating = False

for line in lines[2:]:
    if len(line) == 0:
        continue
    if line[0].isdigit():
        if not is_generating:
            is_generating = True
            current_maps.clear()
        current_maps.append(gen_mapping(*map(int, line.split())))
    else:
        if is_generating:
            is_generating = False
            current_maps.sort(key=lambda t: t[0])
            final_maps.append(current_maps[:])
final_maps.append(current_maps)

ans = float('inf')

for seed_range in seeds:
    current_ranges = [seed_range]
    new_ranges = []

    for m in final_maps:
        for left, right in current_ranges:
            for new_interval in apply_mapping(left, right, m):
                new_ranges.append(new_interval)
        print(current_ranges)
        current_ranges, new_ranges = new_ranges, []

    for left, right in current_ranges:
        ans = min(ans, left)

print(ans)