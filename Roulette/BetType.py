from enum import Enum
from Roulette.LogController import LogController
from colorama import Fore


class BetType(Enum):
    NO_BET = 0
    ODDS_BET = 2
    EVEN_BET = 3
    RED_BET = 4
    BLACK_BET = 5
    FIRST_HALF = 6
    SECOND_HALF = 7
    FIRST_THIRD = 8
    SECOND_THIRD = 9
    THIRD_THIRD = 10
    FIRST_COLUMN = 11
    SECOND_COLUMN = 12
    THIRD_COLUMN = 13

    def __get_message(self) -> str:
        return 'Bet: ' + self.__as_string()

    def display(self, amount: str):
        LogController.display(self.__get_message() + ' -> ' + amount + ' €')

    def display_result(self, is_win: bool):
        if is_win:
            LogController.display(self.__get_message() + ' -> WON', Fore.GREEN)
        else:
            LogController.display(self.__get_message() + ' -> LOST', Fore.RED)

    def write(self):
        LogController.write(self.__get_message() + '\n')

    def __as_string(self):
        if self == self.ODDS_BET:
            return 'ODDS'
        elif self == self.EVEN_BET:
            return 'EVENS'
        elif self == self.RED_BET:
            return 'RED'
        elif self == self.BLACK_BET:
            return 'BLACK'
        elif self == self.FIRST_HALF:
            return 'FIRST HALF'
        elif self == self.SECOND_HALF:
            return 'SECOND HALF'
        elif self == self.FIRST_COLUMN:
            return 'FIRST COLUMN'
        elif self == self.SECOND_COLUMN:
            return 'SECOND COLUMN'
        elif self == self.THIRD_COLUMN:
            return 'THIRD COLUMN'
        elif self == self.FIRST_THIRD:
            return 'FIRST THIRD'
        elif self == self.SECOND_THIRD:
            return 'SECOND THIRD'
        elif self == self.THIRD_THIRD:
            return 'THIRD THIRD'
        else:
            return 'UNKNOWN'

    def is_two_options_bet(self) -> bool:
        return self.value in range(self.ODDS_BET.value, self.FIRST_THIRD.value + 1)

    def is_three_options_bet(self) -> bool:
        return self.value in range(self.FIRST_THIRD.value, self.THIRD_COLUMN.value + 1)


class BetTypeChecker:

    @staticmethod
    def is_no_bet(bet: BetType) -> bool:
        return bet == BetType.NO_BET

    @staticmethod
    def is_red_bet(bet: BetType) -> bool:
        return bet == BetType.RED_BET

    @staticmethod
    def is_black_bet(bet: BetType) -> bool:
        return bet == BetType.BLACK_BET

    @staticmethod
    def is_color_bet(bet: BetType) -> bool:
        return BetTypeChecker.is_red_bet(bet) or BetTypeChecker.is_black_bet(bet)

    @staticmethod
    def is_odd_bet(bet: BetType) -> bool:
        return bet == BetType.ODDS_BET

    @staticmethod
    def is_even_bet(bet: BetType) -> bool:
        return bet == BetType.EVEN_BET

    @staticmethod
    def is_even_odd_bet(bet: BetType) -> bool:
        return BetTypeChecker.is_even_bet(bet) or BetTypeChecker.is_odd_bet(bet)

    @staticmethod
    def is_first_half_bet(bet: BetType) -> bool:
        return bet == BetType.FIRST_HALF

    @staticmethod
    def is_second_half_bet(bet: BetType) -> bool:
        return bet == BetType.SECOND_HALF

    @staticmethod
    def is_halves_bet(bet: BetType) -> bool:
        return BetTypeChecker.is_first_half_bet(bet) or BetTypeChecker.is_second_half_bet(bet)

    @staticmethod
    def is_first_third_bet(bet: BetType) -> bool:
        return bet == BetType.FIRST_THIRD

    @staticmethod
    def is_second_third_bet(bet: BetType) -> bool:
        return bet == BetType.SECOND_THIRD

    @staticmethod
    def is_third_third_bet(bet: BetType) -> bool:
        return bet == BetType.THIRD_THIRD

    @staticmethod
    def is_thirds_bet(bet: BetType) -> bool:
        return BetTypeChecker.is_first_third_bet(bet) or BetTypeChecker.is_second_third_bet(bet) or \
            BetTypeChecker.is_third_third_bet(bet)

    @staticmethod
    def is_first_column_bet(bet: BetType) -> bool:
        return bet == BetType.FIRST_COLUMN

    @staticmethod
    def is_second_column_bet(bet: BetType) -> bool:
        return bet == BetType.SECOND_COLUMN

    @staticmethod
    def is_third_column_bet(bet: BetType) -> bool:
        return bet == BetType.THIRD_COLUMN

    @staticmethod
    def is_columns_bet(bet: BetType) -> bool:
        return BetTypeChecker.is_first_column_bet(bet) or BetTypeChecker.is_second_column_bet(bet) or \
            BetTypeChecker.is_third_column_bet(bet)
