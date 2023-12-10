from math import lcm
from scripts import read_file_strings

def part1():
    network = read_file_strings("d8")
    rl_instructions = network[0]
    node_map = {}

    for mapping in network[2:]:
        key, tup = mapping.split(" = ")[0], mapping.split(" = ")[1]
        tup = (tup[1:4], tup[6:9])
        node_map[key] = tup

    i = 0
    num_steps = 0
    next_element = "AAA"
    while True:
        if i >= len(rl_instructions): i = 0

        if next_element == "ZZZ": return num_steps

        if rl_instructions[i] == 'R':
            next_element = node_map[next_element][1]
        else:
            next_element = node_map[next_element][0]

        i += 1
        num_steps += 1

def part2():
    network = read_file_strings("d8")
    rl_instructions = network[0]
    node_map = {}

    for mapping in network[2:]:
        key, tup = mapping.split(" = ")[0], mapping.split(" = ")[1]
        tup = (tup[1:4], tup[6:9])
        node_map[key] = tup

    start_elements = []
    for n in node_map:
        if n[-1] == 'A': start_elements.append(n)

    # find length of paths
    all_step_counts = []
    for elem in start_elements:
        i = 0
        num_steps = 0
        next_element = elem
        while True:
            if i >= len(rl_instructions): i = 0

            if next_element[-1] == 'Z': break

            if rl_instructions[i] == 'R':
                next_element = node_map[next_element][1]
            else:
                next_element = node_map[next_element][0]

            i += 1
            num_steps += 1

        all_step_counts.append(num_steps)

    return lcm(*all_step_counts)

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
