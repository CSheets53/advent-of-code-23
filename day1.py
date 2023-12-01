from scripts import read_file_strings

#part 1
def part1():
    calibration_doc = read_file_strings("d1")
    val_sum = 0

    for line in calibration_doc:
        l, r = 0, len(line) - 1

        # get first and last digits
        while not line[l].isdigit():
            l += 1

        while not line[r].isdigit():
            r -= 1

        value = int(f"{line[l]}{line[r]}")
        val_sum += value

    return val_sum

def part2():
    calibration_doc = read_file_strings("d1")

    # this feels unintuitive but oh well
    digit_words = {
        "one": '1', 
        "two": '2', 
        "three": '3', 
        "four": '4', 
        "five": '5', 
        "six": '6', 
        "seven": '7',
        "eight": '8', 
        "nine": '9'
    }

    def parse_first_digit():
        # idea: increase length of start string until it matches a digit word
        # start early so that we can check for a word before moving to accept digit
        r = 1
        while r <= len(line):
            if line[r-1].isdigit(): return line[r-1]

            slice = line[:r]

            for word in digit_words.keys():
                if word in slice:
                    return digit_words[word]
                
            r += 1

        # no digit found
        return ''
    
    def parse_last_digit():
        # idea: increase length of start string until it matches a digit word
        l = len(line) - 1
        while l >= 0:
            if line[l].isdigit(): return line[l]

            slice = line[l:]

            for word in digit_words.keys():
                if word in slice:
                    return digit_words[word]
                
            l -= 1

        # no digit found
        return ''

    val_sum = 0

    for line in calibration_doc:
        if not line: continue
        first_digit = parse_first_digit()
        last_digit = parse_last_digit()

        value = 0 if not first_digit or not last_digit else int(f"{first_digit}{last_digit}")
        val_sum += value
        print(value)

    return val_sum

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
