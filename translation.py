class Translation:
    translation_en = {
        "ask_what_is_next": "What will your next card be, over or under?",
        "invalid_answer": """Wrong answer, try ">" or "<"!""",
        "valid_answers": {'under': -1, 'less': -1, 'above': 1, 'more': 1},
        "the_card_above_is": "You got a card -",
        "right_choice": "Congrats, you guessed it!",
        "wrong_choice": "You didn't guess it!",
        "card_are_over_game": "The deck is out of cards!",
        "your_score_is": "Your final score is %s points!",
        "ask_a_name": "Please, enter your name.",
        "minimum_name_length": "The minimum name length is 3 characters!",
        "no_scores_found": "Can't find scores data file.",
        "top_leaders": "Leaderboard",
        "menu": """1. Start the game
2. Show leaderboard
3. Cheats
4. Change language
5. Exit""",
        "menu_options": "Enter the item you want.",
        "invalid_input": "Invalid input. Please choose from the provided options.",

    }
    translation_ru = {
        "ask_what_is_next": "Какой будет твоя следующая карта, больше или меньше?",
        "invalid_answer": """Неправильный вариант ответа, попробуйте ">" или "<"!""",
        "valid_answers": {'меньше': -1, 'больше': 1},
        "the_card_above_is": "Вы получили карту -",
        "right_choice": "Поздравляю, вы угадали!",
        "wrong_choice": "Вы не угадали это!",
        "card_are_over_game": "В колоде кончились карты!",
        "your_score_is": "Ваш итоговый счёт - %s очков.",
        "ask_a_name": "Введите ваше имя",
        "minimum_name_length": "Минимальная длина имени составляет 3 символа!",
        "top_leaders": "Таблица лидеров",
        "menu": """1. Начать играть
2. Показать таблицу лидеров
3. Читы
4. Сменить язык
5. Выход""",
        "menu_options": "Введите нужный вам пункт.",
        "invalid_input": "Неверный Ввод. Пожалуйста, выберите один из предложенных вариантов.",
    }

    def __init__(self, lang='en'):
        self.current_lang = lang
        self.translations = {}
        if attr := getattr(self, f'translation_{lang}'):
            self.translations = attr
        else:
            self.translations = self.translation_en
            self.current_lang = 'en'

    def T(self, msg: str):
        if msg in self.translations:
            return self.translations[msg]
        elif msg not in self.translations and msg in self.translation_en:
            return self.translation_en[msg]
        else:
            raise KeyError(f"Can't find translation for this message - {msg}")
