import os
from json import  load, dump
from typing import Dict

folder_path: str = rf"{os.getenv('APPDATA')}\TranslationGame"
statistic_file_name = "statistic.json"
statistic_file_path: str = rf"{folder_path}\statistic.json"

class Files:
    @staticmethod
    def get_statistic() -> Dict[str, int]:
        Files.path_validation(statistic_file_name)
        with open(statistic_file_path, "r") as file:
            inp = load(file)
        return inp

    @staticmethod
    def save_statistic(statistic_dict: Dict[str, int]) -> None:
        Files.path_validation(statistic_file_name)
        with open(statistic_file_path, "w") as file:
            dump(statistic_dict, file)

    @staticmethod
    def path_validation(file_name) -> None:
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        file_path = rf"{folder_path}\{file_name}"
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("{}")

def get_max_id():
    with open(statistic_file_path, "r") as file:
        data = load(file)

