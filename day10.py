from scripts import read_file_strings

pipe_map = read_file_strings("d10")
NUM_ROWS = len(pipe_map)
NUM_COLS = len(pipe_map[0])

def part1():
    # find S
    s_loc = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if pipe_map[i][j] == 'S': 
                s_loc = (i, j)
                break

        if s_loc: break

    # start navigating loop
    """Notes:
    - can only care about the four cardinal directions
    - pipes can only work if on correct side
    """
    left_pipes = {'L', 'F', '-'}
    right_pipes = {'J', '7', '-'}

    # move from start
    y, x = s_loc
    if y + 1 < NUM_ROWS and pipe_map[y + 1][x] == '|':
        y += 1
    elif y - 1 > 0 and pipe_map[y - 1][x] == '|':
        y -= 1
    elif x + 1 < NUM_COLS and pipe_map[y][x + 1] in right_pipes:
        x += 1
    elif x - 1 > 0 and pipe_map[y][x - 1] in left_pipes:
        x -= 1
    else:
        print("Something went wrong starting from 'S'")
        return -1
    
    last_x, last_y = s_loc[1], s_loc[0]
    visited = set([(last_y, last_x)])
    distance_traveled = 1
    #print(f"{s_loc=}")
    # now not in start, we need movement to be specific to pipe type
    while x != s_loc[1] or y != s_loc[0]:
        #print(f"{x=}, {last_x=} <==> {y=}, {last_y=}")
        visited.add((y, x))
        current_x, current_y = x, y
        pipe = pipe_map[y][x]
        if pipe == '|':
            if last_y == y - 1: # coming from up
                y += 1
            else:
                y -= 1
        elif pipe == '-':
            if last_x == x - 1: # coming from left
                x += 1
            else:
                x -= 1
        elif pipe == 'L':
            if last_x == x + 1: # coming from right, go up
                y -= 1
            else:
                x += 1
        elif pipe == 'J':
            if last_x == x - 1: # coming from left, go up
                y -= 1
            else:
                x -= 1
        elif pipe == '7':
            if last_x == x - 1: # coming from left, go down
                y += 1
            else:
                x -= 1
        elif pipe == 'F':
            if last_x == x + 1: # coming from right, go down
                y += 1
            else:
                x += 1
        else:
            print("UH OH, something broke")
            break

        distance_traveled += 1
        last_x, last_y = current_x, current_y

    return distance_traveled // 2, visited

def part2(visited: set) -> int:
    num_enclosed = 0
    
    for row in range(NUM_ROWS):
        # assisted from https://github.com/OskarSigvardsson/adventofcode/blob/master/2023/day10/day10.py
        for col in range(NUM_COLS):
            if (row, col) in visited: continue
            
            # cast rays diagonally downwards, to see how far to exit
            ray_num = 0
            x, y = col, row
            while x < NUM_COLS and y < NUM_ROWS:
                pipe = pipe_map[y][x]
                if (y, x) in visited and pipe != 'L' and pipe != '7':
                    ray_num += 1
                
                x += 1
                y += 1
            
            if ray_num % 2: num_enclosed += 1

    return num_enclosed

p1_dist, visited = part1()
# print(f"Part 1: {p1_dist}")
print(f"Part 2: {part2(visited)}")
