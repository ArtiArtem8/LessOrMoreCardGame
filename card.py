class Card:
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank
        return False

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.ranks.index(self.rank) < self.ranks.index(other.rank)
        raise TypeError("Can't compare Card with non-Card type")

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


if __name__ == "__main__":
    card1 = Card("Hearts", "2")
    card2 = Card("Spades", "10")
    card3 = Card("Diamonds", "Ace")

    print(f"{card1 == card2 = } ")  # False
    print(f"{card1 != card2 = } ")  # True
    print(f"{card1 < card2 = } ")  # True
    print(f"{card1 <= card2 = } ")  # True
    print(f"{card1 > card2 = } ")  # False
    print(f"{card1 >= card2 = } ")  # False
    print(f"{card1 == card3 = } ")  # False
    print(f"{card1 != card3 = } ")  # True
    print(f"{card1 < card3 = } ")  # True
    print(f"{card1 <= card3 = } ")  # True
    print(f"{card1 > card3 = } ")  # False
    print(f"{card1 >= card3 = } ")  # False
