from scripts import read_file_strings

def parse_cards():
    cards = read_file_strings("d4")

    parsed_cards = []
    for card in cards:
        # parse numbers out
        card_all_nums = card.split(": ")[1]
        split_nums = card_all_nums.split(" | ")
        winning_nums, personal_nums = split_nums[0], split_nums[1]

        winning_nums = winning_nums.split(' ')
        winning_nums = [int(x) for x in winning_nums if x.isdigit()]

        personal_nums = personal_nums.split(' ')
        personal_nums = [int(x) for x in personal_nums if x.isdigit()]

        # create set of winning nums
        winning_nums = set(winning_nums)

        parsed_cards.append((winning_nums, personal_nums))

    return parsed_cards

def part1():
    cards = parse_cards()

    total_points = 0
    for winning_nums, personal_nums in cards:
        points = 0
        for n in personal_nums:
            if n in winning_nums:
                # either set points or double them
                points = 1 if points == 0 else points * 2

        total_points += points

    return total_points

def part2():
    cards = parse_cards()

    # card #: # copies
    card_copies = {}
    for i in range(len(cards)):
        card_copies[i] = 1

    for i in range(len(cards)):
        winning_nums, personal_nums = cards[i]

        next_card = i + 1
        for n in personal_nums:
            if n in winning_nums:
                card_copies[next_card] += card_copies[i]
                next_card += 1

    return sum(card_copies.values())


#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
