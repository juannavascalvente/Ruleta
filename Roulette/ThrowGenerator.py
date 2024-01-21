import os


class ThrowGenerator:

    RAND_SIZE = 4
    MAX_NUMBERS = 38
    DEFAULT_NUM_THROWS_THRESHOLD = 50

    def __init__(self, num_throws_two_options: int, num_throws_three_options):
        self.__throws = []
        self.__two_options_default_num_throws_threshold = num_throws_two_options
        self.__three_options_default_num_throws_threshold = num_throws_three_options
        self.__num_throws = self.DEFAULT_NUM_THROWS_THRESHOLD
        self.__num_last_two_options_throws = num_throws_two_options
        self.__num_last_three_options_throws = num_throws_three_options

    def set_num_throws(self, num_throws: int):
        self.__num_throws = num_throws

    def get_num_throws(self) -> int:
        # return len(self.__throws)
        return self.__num_throws

    def __generate_throw(self):
        random_data = os.urandom(self.RAND_SIZE)
        random_seed: int = int.from_bytes(random_data, byteorder="big") % self.MAX_NUMBERS
        self.__throws.append(int(random_seed))

    def get_last_throws_for_two_options(self, index: int) -> [int]:
        return self.__throws[index - self.__num_last_two_options_throws - 1:index - 1]

    def get_last_throws_for_three_options(self, index: int) -> [int]:
        return self.__throws[index - self.__num_last_three_options_throws - 1:index - 1]

    def get_throws_range(self, start: int, end: int) -> [int]:
        return self.__throws[start:end]

    def get_throw(self, index: int) -> int:
        return self.__throws[index]

    def get_throws(self) -> [int]:
        return self.__throws

    def generate(self):
        for i in range(1, self.__num_throws+1):
            self.__generate_throw()

    def set_throws(self, throws: [int]):
        self.__throws = throws

    def add_throw(self, throw: int):
        self.__throws.append(throw)
