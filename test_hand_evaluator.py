import unittest
from hand_evaluator import PokerHandEvaluator
from card import Card

class TestHandEvaluator(unittest.TestCase):
    
    #Test one pair
    def test_one_pair(self):
        cards = [
            Card("Diamonds", "A"),
            Card("Hearts", "A"),
            Card("Clubs", "3"),
            Card("Spades", "4"),
            Card("Diamonds", "10")

        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("One Pair", [12, 12, 8, 2, 1])  
        self.assertEqual(result, expected)
        
    #Test two pairs
    def test_two_pairs(self):
        cards = [
            Card("Diamonds", "A"),
            Card("Hearts", "A"),
            Card("Clubs", "3"),
            Card("Spades", "3"),
            Card("Diamonds", "10")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Two Pair", [12, 12, 1, 1, 8])
        self.assertEqual(result, expected)
        
    #Testing three of a kind
    def test_three_pair(self):
        cards = [
            Card("Diamonds", "A"),
            Card("Hearts", "A"),
            Card("Clubs", "A"),
            Card("Spades", "4"),
            Card("Diamonds", "10")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Three of a Kind", [12, 12, 12, 8, 2])
        self.assertEqual(result, expected)

    #Testing four of a kind
    def test_four_pair_four(self):
        cards = [
            Card("Diamonds", "A"),
            Card("Hearts", "A"),
            Card("Clubs", "A"),
            Card("Spades", "A"),
            Card("Diamonds", "10")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Four of a Kind", [12, 12, 12, 12, 8])
        self.assertEqual(result, expected)

    #Testing full house (3 of a kind, one pair)
    def test_full_house(self):
        cards = [
            Card("Diamonds", "A"),
            Card("Hearts", "A"),
            Card("Clubs", "A"),
            Card("Spades", "4"),
            Card("Diamonds", "4")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Full House", [12, 12, 12, 2, 2])
        self.assertEqual(result, expected)

    #Testing Flush(5 cards same suit)
    def test_flush(self):
        cards = [
            Card("Diamonds", "A"),
            Card("Diamonds", "6"),
            Card("Diamonds", "Q"),
            Card("Diamonds", "4"),
            Card("Diamonds", "10")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Flush", [12, 10, 8, 4, 2])
        self.assertEqual(result, expected)

    #Testing straight
    def test_straight(self):
        cards = [
            Card("Diamonds", "5"),
            Card("Hearts", "6"),
            Card("Clubs", "7"),
            Card("Spades", "4"),
            Card("Diamonds", "8")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Straight", [6, 5, 4, 3, 2])
        self.assertEqual(result, expected)

    #Testing straight flush
    def test_straight_flush(self):
        cards = [
            Card("Spades", "J"),
            Card("Spades", "10"),
            Card("Spades", "9"),
            Card("Spades", "8"),
            Card("Spades", "7")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Straight Flush", [9, 8, 7, 6, 5])
        self.assertEqual(result, expected)

    #Testing royal flush
    def test_royal_flush(self):
        cards = [
            Card("Spades", "A"),
            Card("Spades", "K"),
            Card("Spades", "Q"),
            Card("Spades", "J"),
            Card("Spades", "10")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("Royal Flush", [12, 11, 10, 9, 8])
        self.assertEqual(result, expected)

    #Testing high card
    def test_high_card(self):
        cards = [
            Card("Spades", "2"),
            Card("Clubs", "7"),
            Card("Spades", "4"),
            Card("Hearts", "Q"),
            Card("Diamonds", "10")
        ]
        result = PokerHandEvaluator.evaluate_hand(cards)
        expected = ("High Card", [10, 8, 5, 2, 0])
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
