from scripts import read_file_strings

def part1():
    schematic = read_file_strings("d3")
    schematic = [[char for char in line if char != '\n'] for line in schematic]
    NUM_ROWS = len(schematic)
    NUM_COLS = len(schematic[0])

    fetched_num_coords = set()

    def is_symbol(char: str):
        return not char.isdigit() and char != '.'
    
    def get_digit(row: int, col: int):
        if (row, col) in fetched_num_coords: return 0

        digit = schematic[row][col]
        fetched_num_coords.add((row, col))

        # move left
        current_col = col - 1
        while current_col >= 0 and schematic[row][current_col].isdigit():
            digit = schematic[row][current_col] + digit
            fetched_num_coords.add((row, current_col))
            current_col -= 1

        # move right
        current_col = col + 1
        while current_col < NUM_ROWS and schematic[row][current_col].isdigit():
            digit += schematic[row][current_col]
            fetched_num_coords.add((row, current_col))
            current_col += 1

        return int(digit)
    
    part_num_sum = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if is_symbol(schematic[i][j]):
                # can we check above
                if i - 1 >= 0:
                    # top left
                    if j - 1 >= 0 and schematic[i - 1][j - 1].isdigit():
                        part_num_sum += get_digit(i - 1, j - 1)

                    # top
                    top_had_num = False
                    if schematic[i - 1][j].isdigit():
                        part_num_sum += get_digit(i - 1, j)

                    # top right
                    if j + 1 < NUM_COLS and schematic[i - 1][j + 1].isdigit() and not top_had_num:
                        part_num_sum += get_digit(i - 1, j + 1)

                # left
                if j - 1 >= 0 and schematic[i][j - 1].isdigit():
                    part_num_sum += get_digit(i, j - 1)

                # right
                if j + 1 >= 0 and schematic[i][j + 1].isdigit():
                    part_num_sum += get_digit(i, j + 1)

                # can we check below
                if i + 1 < len(schematic):
                    # bottom left
                    if j - 1 >= 0 and schematic[i + 1][j - 1].isdigit():
                        part_num_sum += get_digit(i + 1, j - 1)

                    # bottom
                    if schematic[i + 1][j].isdigit():
                        part_num_sum += get_digit(i + 1, j)

                    # bottom right
                    if j + 1 < NUM_COLS and schematic[i + 1][j + 1].isdigit():
                        part_num_sum += get_digit(i + 1, j + 1)

    return part_num_sum

def part2():
    schematic = read_file_strings("d3")
    schematic = [[char for char in line if char != '\n'] for line in schematic]
    NUM_ROWS = len(schematic)
    NUM_COLS = len(schematic[0])

    fetched_num_coords = set()
    
    def get_digit(row: int, col: int):
        if (row, col) in fetched_num_coords: return 0

        digit = schematic[row][col]
        fetched_num_coords.add((row, col))

        # move left
        current_col = col - 1
        while current_col >= 0 and schematic[row][current_col].isdigit():
            digit = schematic[row][current_col] + digit
            fetched_num_coords.add((row, current_col))
            current_col -= 1

        # move right
        current_col = col + 1
        while current_col < NUM_ROWS and schematic[row][current_col].isdigit():
            digit += schematic[row][current_col]
            fetched_num_coords.add((row, current_col))
            current_col += 1

        return int(digit)
    
    gear_ratio_sum = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if schematic[i][j] == '*':
                adjacent_part_nums = []

                # can we check above
                if i - 1 >= 0:
                    # top left
                    if j - 1 >= 0 and schematic[i - 1][j - 1].isdigit():
                        digit = get_digit(i - 1, j - 1)
                        if digit > 0: adjacent_part_nums.append(digit)

                    # top
                    top_had_num = False
                    if schematic[i - 1][j].isdigit():
                        digit = get_digit(i - 1, j)
                        if digit > 0: adjacent_part_nums.append(digit)

                    # top right
                    if j + 1 < NUM_COLS and schematic[i - 1][j + 1].isdigit() and not top_had_num:
                        digit = get_digit(i - 1, j + 1)
                        if digit > 0: adjacent_part_nums.append(digit)

                # left
                if j - 1 >= 0 and schematic[i][j - 1].isdigit():
                    digit = get_digit(i, j - 1)
                    if digit > 0: adjacent_part_nums.append(digit)

                # right
                if j + 1 >= 0 and schematic[i][j + 1].isdigit():
                    digit = get_digit(i, j + 1)
                    if digit > 0: adjacent_part_nums.append(digit)

                # can we check below
                if i + 1 < len(schematic):
                    # bottom left
                    if j - 1 >= 0 and schematic[i + 1][j - 1].isdigit():
                        digit = get_digit(i + 1, j - 1)
                        if digit > 0: adjacent_part_nums.append(digit)

                    # bottom
                    if schematic[i + 1][j].isdigit():
                        digit = get_digit(i + 1, j)
                        if digit > 0: adjacent_part_nums.append(digit)

                    # bottom right
                    if j + 1 < NUM_COLS and schematic[i + 1][j + 1].isdigit():
                        digit = get_digit(i + 1, j + 1)
                        if digit > 0: adjacent_part_nums.append(digit)

                if len(adjacent_part_nums) == 2:
                    gear_ratio_sum += adjacent_part_nums[0] * adjacent_part_nums[1]

    return gear_ratio_sum

# print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
