class ZeroType:

    ZERO = 0
    DOUBLE_ZERO = 37

    @staticmethod
    def is_zero_or_double(value: int) -> bool:
        return value == ZeroType.ZERO or value == ZeroType.DOUBLE_ZERO

    @staticmethod
    def is_zero(value: int) -> bool:
        return value == ZeroType.ZERO

    @staticmethod
    def is_zero_double(value: int) -> bool:
        return value == ZeroType.DOUBLE_ZERO
