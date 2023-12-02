from scripts import read_file_strings

def part1():
    record = read_file_strings("d2")
    NUM_RED = 12
    NUM_GREEN = 13
    NUM_BLUE = 14

    sum_ids = 0
    for game in record:
        game_info, cube_info = game.split(": ")[0], game.split(": ")[1]
        cube_sets = cube_info.split("; ")

        invalid_game = False
        for cube_set in cube_sets:
            number_colors = cube_set.split(", ")

            # check each individual number of cubes
            for num_color in number_colors:
                num, color = int(num_color.split(' ')[0]), num_color.split(' ')[1]
                color = color.strip('\n')

                if color == "red":
                    if num > NUM_RED:
                        invalid_game = True
                        break

                elif color == "green":
                    if num > NUM_GREEN:
                        invalid_game = True
                        break

                elif color == "blue":
                    if num > NUM_BLUE:
                        invalid_game = True
                        break

            if invalid_game: break

        if not invalid_game:
            # grab game id
            id = int(game_info.split(' ')[1])
            #print(f"invalid: game {id}")
            sum_ids += id

    return sum_ids

def part2():
    record = read_file_strings("d2")

    power_sum = 0
    for game in record:
        cube_info = game.split(": ")[1]
        cube_sets = cube_info.split("; ")

        num_red, num_green, num_blue = 0, 0, 0
        for cube_set in cube_sets:
            number_colors = cube_set.split(", ")

            # check each individual number of cubes
            for num_color in number_colors:
                num, color = int(num_color.split(' ')[0]), num_color.split(' ')[1]
                color = color.strip('\n')

                if color == "red": num_red = max(num_red, num)
                elif color == "green": num_green = max(num_green, num)
                elif color == "blue": num_blue = max(num_blue, num)

        set_power = num_red * num_green * num_blue
        power_sum += set_power

    return power_sum

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
