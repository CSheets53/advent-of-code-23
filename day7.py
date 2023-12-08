from collections import defaultdict
from functools import cmp_to_key
from scripts import read_file_strings

def parse_hands_bids():
    all_hands_bids = read_file_strings("d7")
    hands, bids = [], []
    for hb in all_hands_bids:
        h, b = hb.split(' ')[0], hb.split(' ')[1]
        hands.append(h)
        bids.append(int(b))

    return dict(zip(hands, bids))

HAND_TYPES = ["HIGH", "ONE", "TWO", "THREE", "FULL", "FOUR", "FIVE"]
card_map = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,#11,
    'T': 10
}

def map_hand_values(hand: str):
    new_hand = []
    for card in hand:
        new_hand.append(card_map.get(card, card))

    return new_hand

def sort_hands_in_group(h1: str, h2: str):
    if h1 == h2: return 0
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            h1_val = card_map.get(h1[i], h1[i])
            h2_val = card_map.get(h2[i], h2[i])

            if int(h1_val) > int(h2_val):
                return 1
            
            return -1
    
    return 0

def part1():
    hands_bids = parse_hands_bids()
    hand_groups = defaultdict(list)

    def get_hand_type(hand: str):
        counts = defaultdict(int)
        for card in hand:
            counts[card] += 1

        if len(counts.keys()) == 1: return HAND_TYPES[6]
        
        vals = sorted(counts.values(), reverse=True)
        if vals[0] == 4: return HAND_TYPES[5]
        if vals[0] == 3 and vals[1] == 2: return HAND_TYPES[4]
        if vals[0] == 3: return HAND_TYPES[3]
        if vals[0] == 2 and vals[1] == 2: return HAND_TYPES[2]
        if vals[0] == 2: return HAND_TYPES[1]
        
        return HAND_TYPES[0]

    # group types of hands
    for hand in hands_bids:
        hand_type = get_hand_type(hand)
        hand_groups[hand_type].append(hand)

    # rank hands in group
    total_winnings = 0
    current_rank = 1
    for group in HAND_TYPES:
        if group not in hand_groups: continue
        hands = sorted(hand_groups[group], key=cmp_to_key(sort_hands_in_group))
        
        for h in hands:
            total_winnings += hands_bids[h] * current_rank
            current_rank += 1

    return total_winnings

def part2():
    hands_bids = parse_hands_bids()
    hand_groups = defaultdict(list)

    def get_hand_type(hand: str):
        counts = defaultdict(int)

        for card in hand: counts[card] += 1

        if len(counts.keys()) == 1: return HAND_TYPES[6]
        
        j_count = 0 if 'J' not in counts else counts.pop('J')
        vals = sorted(counts.values(), reverse=True)
        
        max_val = vals[0] + j_count
        if max_val == 5: return HAND_TYPES[6] # five of a kind
        if max_val == 4: return HAND_TYPES[5] # four of a kind
        if max_val == 3 and vals[1] == 2: return HAND_TYPES[4] # full house
        if max_val == 3: return HAND_TYPES[3] # three of a kind
        if max_val == 2 and vals[1] == 2: return HAND_TYPES[2] # two pair
        if max_val == 2 or j_count == 2: return HAND_TYPES[1]
        
        return HAND_TYPES[0]

    # group types of hands
    for hand in hands_bids:
        hand_type = get_hand_type(hand)
        hand_groups[hand_type].append(hand)

    # rank hands in group
    total_winnings = 0
    current_rank = 1
    for group in HAND_TYPES:
        if group not in hand_groups: continue
        hands = sorted(hand_groups[group], key=cmp_to_key(sort_hands_in_group))
        
        for h in hands:
            total_winnings += hands_bids[h] * current_rank
            current_rank += 1

    return total_winnings

#print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
