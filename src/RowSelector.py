from abc import ABC

from Roulette.ThrowCheckerHalf import ThrowCheckerHalf


class RowSelector(ThrowCheckerHalf, ABC):
    FIRST_HALF_THRESHOLD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    SECOND_HALF_THRESHOLD = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    def is_a(self, value: int) -> bool:
        return value in self.FIRST_HALF_THRESHOLD

    def is_first_half(self, value: int) -> bool:
        return self.is_a(value)

    def is_b(self, value: int) -> bool:
        return value in self.SECOND_HALF_THRESHOLD

    def is_second_half(self, value: int) -> bool:
        return self.is_b(value)

    def get_half_as_string(self, value: int) -> str:
        if self.is_a(value):
            return 'First half'

        if self.is_b(value):
            return 'Second half'

        return 'None'
