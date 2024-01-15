from abc import ABC

from Roulette.ThrowCheckerThird import ThrowCheckerThird


class ColumnSelector(ThrowCheckerThird, ABC):
    FIRST_COLUMN = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    SECOND_COLUMN = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    THIRD_COLUMN = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    def is_first_column(self, value: int) -> bool:
        return value in self.FIRST_COLUMN

    def is_second_column(self, value: int) -> bool:
        return value in self.SECOND_COLUMN

    def is_third_column(self, value: int) -> bool:
        return value in self.THIRD_COLUMN

    def is_a(self, value: int) -> bool:
        return self.is_first_column(value)

    def is_b(self, value: int) -> bool:
        return self.is_second_column(value)

    def is_c(self, value: int) -> bool:
        return self.is_third_column(value)

    def as_string(self, value: int):
        if self.is_first_column(value):
            return 'First column'
        elif self.is_second_column(value):
            return 'Second column'
        elif self.is_third_column(value):
            return 'Third column'
        return 'NONE'
