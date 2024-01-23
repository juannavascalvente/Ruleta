from abc import ABC

from Roulette.ThrowCheckerThird import ThrowCheckerThird


class ThirdSelector(ThrowCheckerThird, ABC):

    FIRST_THIRD_THRESHOLD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    SECOND_THIRD_THRESHOLD = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    THIRD_THIRD_THRESHOLD = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    def is_a(self, value: int) -> bool:
        return self.is_first_third(value)

    def is_b(self, value: int) -> bool:
        return self.is_second_third(value)

    def is_c(self, value: int) -> bool:
        return self.is_third_third(value)

    def is_first_third(self, value: int) -> bool:
        return value in self.FIRST_THIRD_THRESHOLD

    def is_second_third(self, value: int) -> bool:
        return value in self.SECOND_THIRD_THRESHOLD

    def is_third_third(self, value: int) -> bool:
        return value in self.THIRD_THIRD_THRESHOLD

    def is_first_or_second_third(self, value: int) -> bool:
        return value in self.FIRST_THIRD_THRESHOLD or value in self.SECOND_THIRD_THRESHOLD

    def is_second_or_third_third(self, value: int) -> bool:
        return value in self.SECOND_THIRD_THRESHOLD or value in self.THIRD_THIRD_THRESHOLD

    def is_first_or_third_third(self, value: int) -> bool:
        return value in self.FIRST_THIRD_THRESHOLD or value in self.THIRD_THIRD_THRESHOLD

    def get_third_as_string(self, value: int) -> str:
        if self.is_first_third(value):
            return 'First third'

        if self.is_second_third(value):
            return 'Second third'

        if self.is_third_third(value):
            return 'Third third'

        return 'None'
