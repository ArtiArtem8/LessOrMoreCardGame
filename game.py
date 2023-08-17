import json
import time

from card import Card
from card_printer import EmojiCardPrinter
from deck import DeckBuilder, Deck
from deck_analyzer import DeckAnalyzer
from translation import Translation

translation = Translation('en')
T = translation.T


def compare(x, y):
    return (x > y) - (x < y)


def ask(question, valid_answers):
    while True:
        user_input = input(f"{question} ({', '.join(valid_answers)}): ").strip().lower()
        if user_input in valid_answers:
            return user_input
        else:
            print(T("invalid_input"))


class Game:
    def __init__(self):
        # deck and card
        self.card_printer = EmojiCardPrinter()
        self.deck = Deck()
        self.card_above: Card | None = None

        DeckBuilder.build_standard_deck(self.deck)

        # cheats
        self.analyze = DeckAnalyzer(self.deck)

        # configs
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.score = 0
        self.timer = 0
        self.cheats = 0
        self.scores = []
        self.load_scores()

        self.is_running = False

    def run(self):
        global translation, T
        langs = ['en', 'ru']
        self.is_running = True
        print(T("menu"))
        while self.is_running:
            answer = ask(T("menu_options"), ('1', '2', '3', '4', '5'))
            if answer == '1':
                self.round_loop()
            elif answer == '2':
                self.print_leader_table()
            elif answer == '3':
                self.cheats = not self.cheats
                print(f'{self.cheats=}')
            elif answer == '4':
                translation = Translation(langs[(langs.index(translation.current_lang) + 1) % len(langs)])
                T = translation.T
                print(T("menu"))
            elif answer == '5':
                self.is_running = False

    def round_loop(self):
        start_time = time.time()
        self.score = 0
        DeckBuilder.build_standard_deck(self.deck)
        self.deck.shuffle()
        self.card_above = self.deck.get_card()
        self.print_card_above()
        while not self.deck.is_empty():
            if self.cheats:
                self.analyze.print_probs_more_than(self.card_above)
            answer = self.make_a_choice()
            self.pop_and_check(answer)
            self.print_card_above()
            if self.deck.is_empty():
                print(T('card_are_over_game'))
                end_time = time.time()
                self.timer = end_time - start_time
                print(T('your_score_is') % self.calculate_score())

                self.save_score()
                break

    def make_a_choice(self) -> int:
        print(T("ask_what_is_next"), '">", "<"')  # What will your next card be, over or under?
        answer = self.get_choice()
        return answer

    @staticmethod
    def get_choice() -> int:
        valid_answers = {'<': -1, '>': 1}
        valid_answers.update(translation.translations['valid_answers'])

        while (ans := input().lower().strip()) not in valid_answers:
            print(T('invalid_answer'))
        return valid_answers[ans]

    def pop_and_check(self, answer: int):
        card = self.deck.get_card()
        if compare(card, self.card_above) == answer:
            self.score += 1
            print(T("right_choice"))
        else:
            print(T("wrong_choice"))
        self.card_above = card

    def print_card_above(self):
        print(T('the_card_above_is'), self.card_printer.card(self.card_above))

    def save_score(self):
        print(T("ask_a_name"))
        while len(name := input()) < 3:
            print(T('minimum_name_length'))
        score_data = {
            "name": name,
            "score": self.calculate_score(),
            "time": self.timer,
            "cheats": self.cheats,
            "true_score": self.score
        }
        self.scores.append(score_data)
        self._update_score_file()

    def calculate_score(self):
        return (self.score * 100) - int(self.timer**1.6)

    def _update_score_file(self):
        with open('scores.json', 'w') as file:
            json.dump(self.scores, file)

    def load_scores(self):
        try:
            with open("scores.json", "r") as file:
                self.scores = json.load(file)
        except FileNotFoundError:
            print(T("no_scores_found"))

    def print_leader_table(self):
        self.load_scores()
        top_scores = sorted(self.scores, key=lambda x: x['score'], reverse=True)
        print(T("top_leaders"))
        print('+==================+')
        for i in range(5):
            print(f"{i + 1}. ", end='')
            if i < len(top_scores):
                print(f"{top_scores[i]['name']}\t- {top_scores[i]['score']}", end='')
            print()
        print('+==================+')
