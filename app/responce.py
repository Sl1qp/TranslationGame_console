from typing import List


class Response:

    @staticmethod
    def get_user_input(variants: List[int], incorrect_input_msg: str) -> int:
        while True:
            try:
                response = int(input().split()[0])
            except:
                print(incorrect_input_msg)
                continue
            if response in variants:
                return response
            print(incorrect_input_msg)