from collections import defaultdict
from scripts import read_file_strings

def parse_maps():
    almanac = read_file_strings("d5")
    seeds = [int(x) for x in almanac[0].split(": ")[1].split(' ')]
    map_names = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

    maps = defaultdict(list)
    current_line_ix = 3
    name_ix = 0
    current_name = map_names[name_ix]
    while current_line_ix < len(almanac):
        current_line = almanac[current_line_ix]
        if len(current_line) <= 1:
            current_line_ix += 1
            name_ix += 1
            current_name = map_names[name_ix]
        else:
            maps[current_name].append([int(x) for x in current_line.split(' ')])
        
        current_line_ix += 1

    return (seeds, maps, map_names)

def part1():
    seeds, maps, map_names = parse_maps()
    source_nums = seeds.copy()

    for name in map_names:
        for i in range(len(source_nums)):
            source = source_nums[i]

            for line in maps[name]:
                if source >= line[1] and source < line[1] + line[2]:
                    diff = source - line[1]
                    source_nums[i] = line[0] + diff
                    break

    return min(source_nums)

def part2():
    # todo some other time
    pass

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
