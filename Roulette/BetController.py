from Roulette import BetType, ColorThrow, ColumnSelector, EvenOddThrow, RowSelector, ThirdSelector, Wallet, ZeroType


def write_throws(f, throws: [int]):
    f.write('Bet computed based on throws -> ' + str(throws) + '\n')


class BetController:

    def __init__(self, wallet: Wallet.Wallet, model: int):
        self.__last_throws_two_options = []
        self.__last_throws_three_options = []
        self.__next_bets = []
        self.__bets = []
        self.__wallet = wallet
        self.__color_throw = ColorThrow.ColorThrow()
        self.__rows_selector = RowSelector.RowSelector()
        self.__column_selector = ColumnSelector.ColumnSelector()
        self.__third_selector = ThirdSelector.ThirdSelector()
        self.__even_odd_throw = EvenOddThrow
        self.__model = model

    def init_balance(self):
        self.__wallet.init_balance()

    def add_history_not_bet(self):
        self.__bets.append([BetType.BetType.NO_BET])

    def display_bets(self):
        print('----------------------------- RECOMMENDED BETS ----------------------------------')
        for bet in self.get_bet():
            bet.display()
            print('---------------------------------------------------------------------------------')

    def compute_bet(self, throws_two_options: [int], throws_three_options: [int]) -> bool:
        self.__last_throws_two_options = throws_two_options
        self.__last_throws_three_options = throws_three_options

        if self.__is_bet_on_even():
            self.__next_bets.append(BetType.BetType.EVEN_BET)
        if self.__is_bet_on_odds():
            self.__next_bets.append(BetType.BetType.ODDS_BET)
        if self.__is_bet_on_red():
            self.__next_bets.append(BetType.BetType.RED_BET)
        if self.__is_bet_on_black():
            self.__next_bets.append(BetType.BetType.BLACK_BET)
        if self.__is_bet_on_first_half():
            self.__next_bets.append(BetType.BetType.FIRST_HALF)
        if self.__is_bet_on_second_half():
            self.__next_bets.append(BetType.BetType.SECOND_HALF)
        if self.__is_bet_on_first_third():
            self.__next_bets.append(BetType.BetType.FIRST_THIRD)
        if self.__is_bet_on_second_third():
            self.__next_bets.append(BetType.BetType.SECOND_THIRD)
        if self.__is_bet_on_third_third():
            self.__next_bets.append(BetType.BetType.THIRD_THIRD)
        if self.__is_bet_on_first_column():
            self.__next_bets.append(BetType.BetType.FIRST_COLUMN)
        if self.__is_bet_on_second_column():
            self.__next_bets.append(BetType.BetType.SECOND_COLUMN)
        if self.__is_bet_on_third_column():
            self.__next_bets.append(BetType.BetType.THIRD_COLUMN)

        if len(self.__next_bets) == 0:
            self.__bets.append([BetType.BetType.NO_BET])
        else:
            self.__bets.append(self.__next_bets)

        return len(self.__next_bets) > 0

    def get_bets_history(self) -> [[BetType.BetType]]:
        return self.__bets

    def get_bet(self) -> [BetType]:
        return self.__next_bets

    def reset_bet(self):
        self.__next_bets = []

    def update_bet_amount(self, bet_type: BetType) -> float:
        return self.__wallet.update_bet_amount(bet_type, self.__model)

    def is_max_amount_lost(self, bet_type: BetType) -> bool:
        return self.__wallet.is_max_amount_lost(bet_type)

    def reset_all_bet_amount(self):
        self.__wallet.reset_all_bet_amount()

    def reset_bet_amount(self, bet_type: BetType):
        self.__wallet.reset_bet_amount(bet_type)

    def set_max_bet_amount(self, bet_type: BetType):
        self.__wallet.set_max_bet_amount(bet_type)

    def get_bet_amount(self, bet_type: BetType) -> float:
        return self.__wallet.get_bet_amount(bet_type)

    def get_bet_accumulated(self, bet_type: BetType) -> float:
        return self.__wallet.get_bet_accumulated(bet_type)

    def get_max_bet_accumulated(self) -> float:
        return self.__wallet.get_max_bet_accumulated()

    def update_balance_win(self, bet_type: BetType):
        self.__wallet.update_balance_win(bet_type)

    def update_balance_lost(self, bet_type: BetType):
        self.__wallet.update_balance_lost(bet_type)

    def get_bet_balance(self) -> float:
        return self.__wallet.get_balance()

    def __is_bet_zero_or_double(self) -> bool:
        return any((value == 0 or value == 37) for value in self.__last_throws_two_options)

    def __is_bet_on_even(self) -> bool:
        return all(value % 2 == 0 or ZeroType.ZeroType.is_zero_or_double(value)
                   for value in self.__last_throws_two_options)

    def __is_bet_on_odds(self) -> bool:
        return all(value % 2 != 0 or ZeroType.ZeroType.is_zero_or_double(value)
                   for value in self.__last_throws_two_options)

    def __is_bet_on_red(self) -> bool:
        return all(self.__color_throw.is_black(value) or ZeroType.ZeroType.is_zero_or_double(value)
                   for value in self.__last_throws_two_options)

    def __is_bet_on_black(self) -> bool:
        return all(self.__color_throw.is_red(value) or ZeroType.ZeroType.is_zero_or_double(value)
                   for value in self.__last_throws_two_options)

    def __is_bet_on_first_half(self) -> bool:
        return all(self.__rows_selector.is_second_half(value) or ZeroType.ZeroType.is_zero_or_double(value)
                   for value in self.__last_throws_two_options)

    def __is_bet_on_second_half(self) -> bool:
        return all(self.__rows_selector.is_first_half(value) or ZeroType.ZeroType.is_zero_or_double(value)
                   for value in self.__last_throws_two_options)

    def __is_bet_on_first_third(self) -> bool:
        return all(self.__third_selector.is_second_third(value) or ZeroType.ZeroType.is_zero_or_double(value)
                   or self.__third_selector.is_third_third(value) for value in self.__last_throws_three_options)

    def __is_bet_on_second_third(self) -> bool:
        return all(self.__third_selector.is_first_third(value) or ZeroType.ZeroType.is_zero_or_double(value)
                   or self.__third_selector.is_third_third(value) for value in self.__last_throws_three_options)

    def __is_bet_on_third_third(self) -> bool:
        return all(self.__third_selector.is_first_third(value) or ZeroType.ZeroType.is_zero_or_double(value) or
                   self.__third_selector.is_second_third(value) for value in self.__last_throws_three_options)

    def __is_bet_on_first_column(self) -> bool:
        return all(self.__column_selector.is_second_column(value) or self.__column_selector.is_third_column(value) or
                   ZeroType.ZeroType.is_zero_or_double(value) for value in self.__last_throws_three_options)

    def __is_bet_on_second_column(self) -> bool:
        return all(self.__column_selector.is_first_column(value) or self.__column_selector.is_third_column(value) or
                   ZeroType.ZeroType.is_zero_or_double(value) for value in self.__last_throws_three_options)

    def __is_bet_on_third_column(self) -> bool:
        return all(self.__column_selector.is_first_column(value) or self.__column_selector.is_second_column(value) or
                   ZeroType.ZeroType.is_zero_or_double(value) for value in self.__last_throws_three_options)

    def display(self):
        print(self.__wallet)

    def update_accumulated_bet(self, bet_type: BetType.BetType):
        self.__wallet.update_accumulated_bet(bet_type)

    def is_win(self, bet_type: BetType.BetType, value: int) -> bool:
        if ZeroType.ZeroType.is_zero_or_double(value):
            return False

        if bet_type == BetType.BetType.ODDS_BET:
            return self.__even_odd_throw.is_odd(value)
        elif bet_type == BetType.BetType.EVEN_BET:
            return self.__even_odd_throw.is_even(value)
        elif bet_type == BetType.BetType.RED_BET:
            return self.__color_throw.is_red(value)
        elif bet_type == BetType.BetType.BLACK_BET:
            return self.__color_throw.is_black(value)
        elif bet_type == BetType.BetType.FIRST_HALF:
            return self.__rows_selector.is_first_half(value)
        elif bet_type == BetType.BetType.SECOND_HALF:
            return self.__rows_selector.is_second_half(value)
        elif bet_type == BetType.BetType.FIRST_THIRD:
            return self.__third_selector.is_first_third(value)
        elif bet_type == BetType.BetType.SECOND_THIRD:
            return self.__third_selector.is_second_third(value)
        elif bet_type == BetType.BetType.THIRD_THIRD:
            return self.__third_selector.is_third_third(value)
        elif bet_type == BetType.BetType.FIRST_COLUMN:
            return self.__column_selector.is_first_column(value)
        elif bet_type == BetType.BetType.SECOND_COLUMN:
            return self.__column_selector.is_second_column(value)
        elif bet_type == BetType.BetType.THIRD_COLUMN:
            return self.__column_selector.is_third_column(value)
