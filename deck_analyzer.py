from card import Card
from deck import Deck


class DeckAnalyzer:
    def __init__(self, deck: Deck):
        self.deck = deck

    def count_ranks(self):
        card_rank_count = {}
        for card in self.deck:
            card_rank_count[card.rank] = card_rank_count.get(card.rank, 0) + 1
        return card_rank_count

    def get_probabilities(self):
        amount_of_cards = len(self.deck)
        probs = {}
        for k, v in self.count_ranks().items():
            probs[k] = v/amount_of_cards
        return probs

    def print_probs(self):
        for k, v in self.get_probabilities().items():
            print(f"{k}-{v*100:.2f}%", end='\t')
        print()

    def get_probs_more_than(self, card: Card):
        lower_chance = .0
        upper_chance = .0
        for k, v in self.get_probabilities().items():
            if Card(rank=k, suit="") > card:
                upper_chance += v
            elif Card(rank=k, suit="") < card:
                lower_chance += v
        return lower_chance, upper_chance

    def print_probs_more_than(self, card: Card):
        low, up = self.get_probs_more_than(card)
        print(f"'<' - {low*100:.1f}%   '>' - {up*100:.1f}%")



