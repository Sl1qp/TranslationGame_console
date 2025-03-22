from random import randint
from responce import Response
from translation_service import TranslationService
from file_worker import Files


class Game:
    def __init__(self):
        self.__word_base: TranslationService = TranslationService()
        self.language: str = "English"
        self.level: str = "C1"

        self.player_name: str = "Player"
        self.max_player_score: int = 0

        self.statistic = Files.get_statistic()

    def start(self):
        self.input_player_data()
        current_score = self.__start_game()
        print(f"Current score = {current_score} !\nMax score = {self.max_player_score}")
        #print(f"Name: {self.player_name}\nScore: {self.max_player_score}")

        self.statistic[self.player_name] = self.max_player_score
        Files.save_statistic(self.statistic)

    def __start_game(self) -> int:
        current_score = 0
        question_count = randint(5, 15)

        for _ in range(question_count):
            question = self.__word_base.get_question(self.language, self.level)
            question_word = question["question_word"]
            other_words = question["other_word"]

            print(f"Переведите слово: {question_word[1]}")
            print('\n'.join(f"{i+1}) {other_words[i]}" for i in range(0,4)))
            player_answer_code = Response.get_user_input([i for i in range(1, 5)], "Incorrect input!")

            # print(f"--> player_name = {self.player_name}")
            # print(f"--> max_player_score = {self.max_player_score}")
            # print(f"--> current_score = {current_score}")
            # print(f"--> question_word = {question["question_word"]}")
            # print(f"--> other_words = {question["other_word"]}")
            # print(f"--> player_answer_code = {player_answer_code}")
            # print(f"--> other_words[player_answer_code - 1] = {other_words[player_answer_code - 1]}")
            # print(f"--> question_word[0] = {question_word[0]}")

            if other_words[player_answer_code - 1] == question_word[0]:
                current_score += 1
            if player_answer_code == -1:
                break

        if self.max_player_score < current_score:
            self.max_player_score = current_score

        return current_score

    def input_player_data(self):
        while True:
            try:
                print("Enter your name: ")
                entered_name = input()
                if len(entered_name) >= 20 or entered_name == "":
                    raise Exception()
                self.player_name = entered_name
                self.max_player_score = self.statistic.get(self.player_name, 0)
                break
            except:
                print("Invalid input")

