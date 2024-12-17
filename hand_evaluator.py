from collections import Counter
from itertools import combinations
from card import Card 

class PokerHandEvaluator:
    hand_ranks = {
        "Royal Flush": 10,
        "Straight Flush": 9,
        "Four of a Kind": 8,
        "Full House": 7,
        "Flush": 6,
        "Straight": 5,
        "Three of a Kind": 4,
        "Two Pair": 3,
        "One Pair": 2,
        "High Card": 1,
    }

    @staticmethod
    def evaluate_hand(cards):
        suits = [card.suit for card in cards]
        values = [Card.values.index(card.value) for card in cards]
        value_counts = Counter(values)
        most_common = value_counts.most_common()

        # Check for Flush
        flush_suit = None
        for suit in Card.suits:
            if suits.count(suit) >= 5:
                flush_suit = suit
                break
        flush_cards = [card for card in cards if card.suit == flush_suit] if flush_suit else []

        # Check for Straight
        unique_values = sorted(set(values))
        straight_high = None
        for i in range(len(unique_values) - 4):
            if unique_values[i:i + 5] == list(range(unique_values[i], unique_values[i] + 5)):
                straight_high = unique_values[i + 4]
                break

        # Royal Flush
        if flush_suit and straight_high and straight_high == Card.values.index("A"):
            if all(card.suit == flush_suit for card in flush_cards):
                return "Royal Flush", sorted(values, reverse=True)[:5]

        # Straight Flush
        if flush_suit and straight_high:
            if all(card.suit == flush_suit for card in flush_cards):
                return "Straight Flush", sorted(values, reverse=True)[:5]

        # Four of a Kind
        if most_common[0][1] == 4:
            quad_value = most_common[0][0]
            kicker = max(value for value in values if value != quad_value)
            return "Four of a Kind", [quad_value] * 4 + [kicker]

        # Full House
        if most_common[0][1] == 3 and len(most_common) > 1 and most_common[1][1] >= 2:
            triple_value = most_common[0][0]
            pair_value = most_common[1][0]
            return "Full House", [triple_value] * 3 + [pair_value] * 2

        # Flush
        if flush_suit:
            flush_values = sorted([Card.values.index(card.value) for card in flush_cards], reverse=True)
            return "Flush", flush_values[:5]

        # Straight
        if straight_high:
            return "Straight", list(range(straight_high - 4, straight_high + 1))[::-1]

        # Three of a Kind
        if most_common[0][1] == 3:
            triple_value = most_common[0][0]
            kickers = sorted([value for value in values if value != triple_value], reverse=True)[:2]
            return "Three of a Kind", [triple_value] * 3 + kickers

        # Two Pair
        if len(most_common) > 1 and most_common[0][1] == 2 and most_common[1][1] == 2:
            pair1 = most_common[0][0]
            pair2 = most_common[1][0]
            kicker = max(value for value in values if value != pair1 and value != pair2)
            return "Two Pair", [pair1] * 2 + [pair2] * 2 + [kicker]

        # One Pair
        if most_common[0][1] == 2:
            pair_value = most_common[0][0]
            kickers = sorted([value for value in values if value != pair_value], reverse=True)[:3]
            return "One Pair", [pair_value] * 2 + kickers

        # High Card
        sorted_values = sorted(values, reverse=True)
        return "High Card", sorted_values[:5]

    @staticmethod
    def best_five_from_seven(seven_cards):
        best_rank = None
        best_hand = None

        for combo in combinations(seven_cards, 5):
            rank, tie_breaker = PokerHandEvaluator.evaluate_hand(combo)

            if best_rank is None or PokerHandEvaluator.hand_ranks[rank] > PokerHandEvaluator.hand_ranks[best_rank]:
                best_rank = rank
                best_hand = combo

        return best_hand
