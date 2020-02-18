from itertools import combinations, permutations
import time
import pandas as pd

### Generate all poker cards
all_suits = ['club','diamond','heart','spade']
all_ranks = [str(i) for i in range(2,11)] + ['J','Q','K','A']
pokers = [i+'-'+j for i in all_suits for j in all_ranks]

### Question 1
### Generate all poker hands
tStart = time.time()
hands = list(combinations(pokers, 5))

num_of_hands = {
    'straight_flush': 0,
    'four_of_a_kind': 0,
    'full_house': 0,
    'flush': 0,
    'straight': 0,
    'three_of_a_kind': 0,
    'two_pairs': 0,
    'one_pair': 0,
    'high_card': 0
}

def type_of_hand(r,s):
    r_unique = set(r)
    if len(r_unique) != 5: ### any rank appears more than once
        r_count = []
        for i in r_unique:
            r_count.append(r.count(i))

        if 4 in r_count:
            return('four_of_a_kind')
        elif 3 in r_count and 2 in r_count:
            return('full_house')
        elif 3 in r_count and 2 not in r_count:
            return('three_of_a_kind')
        elif 2 in r_count and len(r_count) == 3:
            return('two_pairs')
        elif 2 in r_count and len(r_count) == 4:
            return('one_pair')
    else:
        #### These hands are considered as straight
        straight_hands = [{'A','2','3','4','5'}]
        for i in range(len(all_ranks)-4):
            straight_hands.append(set(all_ranks[i:i+5]))
        if r_unique in straight_hands and len(set(s)) == 1:
            return('straight_flush')
        elif r_unique in straight_hands:
            return('straight')
        elif len(set(s)) == 1:
            return('flush')
        else:
            return('high_card')

### Counting each type of poker hands
for hand in hands:
    ranks = []
    suits = []
    for card in hand:
        s, r = card.split('-')
        suits.append(s)
        ranks.append(r)
    num_of_hands[type_of_hand(ranks,suits)] += 1

print(pd.DataFrame(num_of_hands.items(), columns=['Poker Hand','Number of hands']))
print("There are", len(hands), "distinct hands in total.")

tEnd = time.time()
print("The program costs", (tEnd-tStart), "sec")
