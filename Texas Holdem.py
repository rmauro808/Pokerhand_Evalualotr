from card import Deck
from hand_evaluator import PokerHandEvaluator

class PokerGame:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = {f"Player {i+1}": self.deck.deal(2) for i in range(num_players)}
        self.community_cards = self.deck.deal(5)

    def determine_winner(self):
        best_hand = None
        winner = None
        best_rank_value = -1  

        for player, hand in self.players.items():
            combined_hand = hand + self.community_cards
            best_five = PokerHandEvaluator.best_five_from_seven(combined_hand)
            rank, _ = PokerHandEvaluator.evaluate_hand(best_five)
            rank_value = PokerHandEvaluator.hand_ranks[rank]

            if rank_value > best_rank_value:
                best_rank_value = rank_value
                best_hand = best_five
                winner = player
            print(f"{player}'s hand: {hand}, Best Hand: {rank}")
        return winner

def main():
    game = PokerGame(num_players=2)
    print(f"Community Cards: {game.community_cards}")
    winner = game.determine_winner()
    print(f"The winner is: {winner}")

if __name__ == "__main__":
    main()
