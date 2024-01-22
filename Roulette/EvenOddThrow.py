from abc import ABC

from Roulette.ThrowCheckerHalf import ThrowCheckerHalf
from Roulette.ZeroType import ZeroType


def is_even(value: int) -> bool:
    return value % 2 == 0


def is_odd(value: int) -> bool:
    return value % 2 == 1


class EvenOddThrow(ThrowCheckerHalf, ABC):

    def is_a(self, value: int) -> bool:
        return is_even(value)

    def is_b(self, value: int) -> bool:
        return is_odd(value)

    @staticmethod
    def as_string(value: int) -> str:
        if ZeroType.is_zero_or_double(value):
            return "ZERO"
        elif is_odd(value):
            return "ODD"
        return "EVEN"
