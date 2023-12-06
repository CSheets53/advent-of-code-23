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
    # shoutout to Dazbo's guide helping me try to understand this: https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb
    seeds, maps, map_names = parse_maps()
    ranges_to_map = []
    for i in range(0, len(seeds), 2):
        ranges_to_map.append((seeds[i], seeds[i] + seeds[i+1]))

    for name in map_names:
        new_ranges = []

        for line in maps[name]:
            dest, map_start, size = line[0], line[1], line[2]
            map_end = map_start + size

            unused_ranges = []
            while ranges_to_map:
                src_start, src_end = ranges_to_map.pop()

                # split the source range into its overlap and non-overlapped segments
                left_no_overlap = (src_start, min(src_end, map_start))
                mid_overlapped = (max(src_start, map_start), min(src_end, map_end))
                right_no_overlap = (max(src_start, map_end), src_end)

                if left_no_overlap[1] > left_no_overlap[0]:
                    # we started before the map started
                    unused_ranges.append(left_no_overlap)
                if mid_overlapped[1] > mid_overlapped[0]:
                    # there is some overlap
                    offset = dest - map_start
                    new_ranges.append((mid_overlapped[0] + offset, mid_overlapped[1] + offset))
                if right_no_overlap[1] > right_no_overlap[0]:
                    # we ended after the map ended
                    unused_ranges.append(right_no_overlap)

            ranges_to_map = unused_ranges

        # pass on any unmapped ranges as 1:1
        ranges_to_map += new_ranges

    return min(start for start, _ in ranges_to_map)

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
