from abc import ABC

from Roulette.ThrowCheckerHalf import ThrowCheckerHalf


class ColorThrow(ThrowCheckerHalf, ABC):

    RED_VALUES = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    BLACK_VALUES = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    def is_a(self, value: int) -> bool:
        return value in self.RED_VALUES

    def is_red(self, value: int) -> bool:
        return self.is_a(value)

    def is_b(self, value: int) -> bool:
        return value in self.BLACK_VALUES

    def is_black(self, value: int) -> bool:
        return self.is_b(value)

    def as_string(self, value: int) -> str:
        if value in self.RED_VALUES:
            return 'RED'

        if value in self.BLACK_VALUES:
            return 'BLACK'

        return 'GREEN'
