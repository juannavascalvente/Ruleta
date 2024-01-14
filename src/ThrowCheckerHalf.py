from abc import ABC, abstractmethod


class ThrowCheckerHalf(ABC):
    __ZERO = 0
    __DOUBLE_ZERO = 37

    @abstractmethod
    def is_a(self, value: int) -> bool:
        pass

    @abstractmethod
    def is_b(self, value: int) -> bool:
        pass

    def is_zero_or_double(self, value: int) -> bool:
        return value == self.__ZERO or value == self.__DOUBLE_ZERO

    def __none_is_zero(self, values: [int]) -> bool:
        return all(not self.is_zero_or_double(value) for value in values)

    def is_all_a(self, values: [int]) -> bool:
        return self.__none_is_zero(values) and all(self.is_a(value) for value in values)

    def is_all_b(self, values: [int]) -> bool:
        return self.__none_is_zero(values) and all(self.is_b(value) for value in values)
