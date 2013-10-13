import time
from collections import defaultdict
import re

# started, but not yet finished
start_time = time.time()


def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)


class Hand:
    """
    Calculate the value of a hand in poker
    """

    def card_number(self, card):
        return {
            "T": "10",
            "J": "11",
            "Q": "12",
            "K": "13",
            "A": "14"
        }.get(card[0], card[0])

    def __init__(self, hand):
        self.nums, self.colors = set(), set()
        self.pairs = defaultdict(int)

        for card in hand:
            num = self.card_number(card)
            self.nums.add(int(num))
            self.colors.add(card[1])
            self.hand = hand
            self.pairs[card[0]] += 1

    def __str__(self):
        return """
        Hand: %r
        Numbers: %r
        Colors: %r
        Pairs: %r
        """ % (self.hand, self.nums, self.colors, self.pairs)

    def consecutive_nums(self):
        if len(self.nums) != 5:
            return False
        nums = sorted(list(self.nums))
        for i in range(4):
            if nums[i+1] - nums[i] != 1:
                return False
        return True

    def check_cards(self):
        """
        Check for the combination that can be made with the current hands
        """
        # royal flush
        if len(self.colors) == 1 and sorted(list(self.nums)) == range(10, 15):
            return 9, ()

        # straight flush
        if len(self.colors) == 1 and self.consecutive_nums():
            return 8, ()

        # four of a kind
        found_2, found_3 = [], []
        for pair in self.pairs:
            if self.pairs[pair] == 4:
                return 7, ()
            if self.pairs[pair] == 3:
                found_3.append(pair)
            if self.pairs[pair] == 2:
                found_2.append(pair)
        if len(found_3) and len(found_2):
            return 6, (found_2, found_3)

        if len(self.colors) == 1:
            return 5, sorted(list(self.nums))

        if self.consecutive_nums():
            return 4, sorted(list(self.nums))

        if found_3:
            return 3, found_3

        if len(found_2) == 2:
            return 2, found_2

        if found_2:
            return 1, found_2

        return 0, self.nums

    def beats(self, hand2):
        """
        Compare 2 hands to see who would win
        """
        h1 = self.check_cards()
        h2 = hand2.check_cards()
        if h1 != h2:
            # we have a clear winner
            return h1 > h2



allHands = {
    9: Hand(['TC', 'KC', 'QC', 'JC', 'AC']),
    8: Hand(['TC', 'KC', 'QC', 'JC', '9C']),
    7: Hand(['TD', 'TS', 'TC', 'TH', 'AC']),
    6: Hand(['2H', '2D', '4C', '4D', '4S']),
    5: Hand(['3D', '6D', '7D', 'TD', 'QD']),
    4: Hand(['4D', '5s', '6c', '7D', '8D']),
    3: Hand(['2D', '9C', 'AS', 'AH', 'AC']),
    2: Hand(['2C', 'TS', '8S', '8D', 'TD']),
    1: Hand(['5H', '5C', '6S', '7S', 'KD']),
    0: Hand(['2C', '5C', '7D', '8S', 'QH'])
}

for key in allHands:
    print key
    assert allHands[key].check_cards()[0] == key

# hands = [i.split(' ') for i in open('54.txt').read().split("\n")]
# print hands[0]
# print hands[1]

# h = Hand(hands[1][0:5])
# print h

# check_hand(hands[0][0:5], hands[0][5:10])
# check_hand(hands[1][0:5], hands[1][5:10])

print time.time() - start_time, "seconds"
