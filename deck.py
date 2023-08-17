import random
from collections import UserList

from card import Card
from card_printer import CardPrinter


class Deck(UserList):
    def __init__(self, cards: list[Card] = None, card_printer=CardPrinter):
        super().__init__(cards)
        self.card_printer = card_printer

    @property
    def cards(self) -> list[Card]:
        return self.data

    @cards.setter
    def cards(self, value):
        self.data = value

    def shuffle(self):
        random.shuffle(self.cards)

    def is_empty(self):
        return len(self.cards) == 0

    def get_card(self):
        if self.cards:
            return self.cards.pop()
        return None

    def print_deck(self):
        for card in self.cards:
            self.card_printer.print_card(card)


class DeckBuilder:
    @staticmethod
    def build_standard_deck(deck: Deck):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        cards = [Card(suit, rank) for suit in suits for rank in ranks]
        deck.cards = cards

    @staticmethod
    def build_reverse_standard_deck(deck: Deck):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        cards = [Card(suit, rank) for rank in ranks for suit in suits]
        deck.cards = cards
