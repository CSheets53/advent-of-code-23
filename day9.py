from scripts import read_file_strings

def part1():
    histories = read_file_strings("d9")

    def calc_next_value(seq: list):
        if all(x == 0 for x in seq): return 0

        new_seq = []
        for i in range(1, len(seq)):
            new_seq.append(seq[i] - seq[i-1])

        return seq[-1] + calc_next_value(new_seq)

    next_value_sum = 0
    for history in histories:
        hist = [int(x) for x in history.split(' ')]
        next_value_sum += calc_next_value(hist)

    return next_value_sum

def part2():
    histories = read_file_strings("d9")

    def calc_next_value(seq: list):
        if all(x == 0 for x in seq): return 0

        new_seq = []
        for i in range(1, len(seq)):
            new_seq.append(seq[i] - seq[i-1])

        return seq[0] - calc_next_value(new_seq)

    next_value_sum = 0
    for history in histories:
        hist = [int(x) for x in history.split(' ')]
        next_value_sum += calc_next_value(hist)

    return next_value_sum

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
