from dataclasses import dataclass

@dataclass
class APITranslate:
    url: str = "https://translate.api.cloud.yandex.net/translate/v2/translate"

    api_key: str = "AQVNzCb-3m6D2qsiE4LZP1UvuEb9HXixNTLwqJjo"
    folder_id: str = "b1gcnpve17udmimik6km"

@dataclass
class Color:
    white: (int, int, int) = (255, 255, 255)
    black: (int, int, int) = (0, 0, 0)
    gray: (int, int, int) = (128, 128, 128)

    purple: (int, int, int) = (235, 171, 204)
    light_purple: (int, int, int) = (235, 129, 184)


@dataclass
class GameState:
    """
    Содержит стандартные значения настроек игры
    """
    language_list = ["English", "Deutsch", "French"]
    language_difficulty_list = ["A1", "A2", "B1", "B2", "C1", "C2"]


@dataclass
class UserState:
    """
    Содержит стандартные значения данных о пользователе
    """
    score = {'A1': 0, 'A2': 0, 'B1': 0, 'B2': 0, 'C1': 0, 'C2': 0}
    id: int = -1
    name: str = ""
