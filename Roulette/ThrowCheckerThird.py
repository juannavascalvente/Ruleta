from abc import ABC, abstractmethod


class ThrowCheckerThird(ABC):
    __ZERO = 0
    __DOUBLE_ZERO = 37

    @abstractmethod
    def is_a(self, value: int) -> bool:
        pass

    @abstractmethod
    def is_b(self, value: int) -> bool:
        pass

    @abstractmethod
    def is_c(self, value: int) -> bool:
        pass

    def is_zero_or_double(self, value: int) -> bool:
        return value == self.__ZERO or value == self.__DOUBLE_ZERO

    def all_a(self, values: [int]) -> bool:
        return all(self.is_a(value) for value in values)

    def all_b(self, values: [int]) -> bool:
        return all(self.is_b(value) for value in values)

    def all_c(self, values: [int]) -> bool:
        return all(self.is_c(value) for value in values)
