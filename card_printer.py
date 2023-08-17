class CardPrinter:
    @staticmethod
    def card(card):
        return card.__str__()


class EmojiCardPrinter(CardPrinter):
    @staticmethod
    def card(card):
        suit_symbols = {'Hearts': '♥️', 'Diamonds': '♦️', 'Clubs': '♣️', 'Spades': '♠️'}
        rank_symbols = {
            '2': '2️⃣', '3': '3️⃣', '4': '4️⃣', '5': '5️⃣',
            '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣',
            '10': '🔟', 'Jack': '🤴', 'Queen': '👸', 'King': '🤴',
            'Ace': '🅰️'
        }
        default_rank_symbols = {
            '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9',
            '10': '10', 'Jack': 'J', 'Queen': 'Q', 'King': 'K',
            'Ace': 'A'
        }
        return f"{default_rank_symbols[card.rank]}{suit_symbols[card.suit]}"
