from Roulette.BetType import BetType

import locale


class Wallet:

    __MINIMUM_BET = 25
    __BET_FACTOR_GROWTH = 2.0

    __MAX_AMOUNT_LOST_TWO_OPTIONS_BET = 1800
    __MAX_AMOUNT_LOST_THREE_OPTIONS_BET = 1800

    def __init__(self, initial_bet: int, bet_factor_growth: float = __BET_FACTOR_GROWTH):
        self.__bet = None
        self.__initial_bet = initial_bet
        self.__bet_amount = {
            BetType.RED_BET: initial_bet,
            BetType.BLACK_BET: initial_bet,
            BetType.EVEN_BET: initial_bet,
            BetType.ODDS_BET: initial_bet,
            BetType.FIRST_HALF: initial_bet,
            BetType.SECOND_HALF: initial_bet,
            BetType.FIRST_THIRD: initial_bet,
            BetType.SECOND_THIRD: initial_bet,
            BetType.THIRD_THIRD: initial_bet,
            BetType.FIRST_COLUMN: initial_bet,
            BetType.SECOND_COLUMN: initial_bet,
            BetType.THIRD_COLUMN: initial_bet,
        }
        self.__balance = 0
        self.__bet_factor_growth = bet_factor_growth
        self.__max_bet = initial_bet
        self.__accumulated_bet = {
            BetType.RED_BET: 0.0,
            BetType.BLACK_BET: 0.0,
            BetType.EVEN_BET: 0.0,
            BetType.ODDS_BET: 0.0,
            BetType.FIRST_HALF: 0.0,
            BetType.SECOND_HALF: 0.0,
            BetType.FIRST_THIRD: 0.0,
            BetType.SECOND_THIRD: 0.0,
            BetType.THIRD_THIRD: 0.0,
            BetType.FIRST_COLUMN: 0.0,
            BetType.SECOND_COLUMN: 0.0,
            BetType.THIRD_COLUMN: 0.0,
        }
        self.__num_bet_lost = {
            BetType.RED_BET: 0,
            BetType.BLACK_BET: 0,
            BetType.EVEN_BET: 0,
            BetType.ODDS_BET: 0,
            BetType.FIRST_HALF: 0,
            BetType.SECOND_HALF: 0,
            BetType.FIRST_THIRD: 0,
            BetType.SECOND_THIRD: 0,
            BetType.THIRD_THIRD: 0,
            BetType.FIRST_COLUMN: 0,
            BetType.SECOND_COLUMN: 0,
            BetType.THIRD_COLUMN: 0,
        }
        self.__max_accumulated_bet = 0
        self.__max_balance = self.__balance
        self.__min_balance = self.__balance

    def get_bet_amount(self, bet_type: BetType) -> float:
        return self.__bet_amount[bet_type]

    def get_balance(self) -> float:
        return self.__balance

    def update_balance_win(self, bet_type: BetType):
        self.__balance -= self.get_bet_amount(bet_type)
        self.__balance += self.get_bet_amount(bet_type) * 2
        self.__max_balance = max(self.__max_balance, self.__balance)

    def update_balance_lost(self, bet_type: BetType):
        self.__balance -= self.get_bet_amount(bet_type)
        self.__min_balance = min(self.__min_balance, self.__balance)

    def init_balance(self):
        self.__balance = 0.0
        self.__reset_max_balance()
        self.__reset_min_balance()

    def update_bet_amount(self, bet_type: BetType, model: int = 1):
        if model == 1:
            self.update_bet_amount_model_1(bet_type)
        elif model == 2:
            self.update_bet_amount_model_2(bet_type)
        else:
            self.update_bet_amount_aggressive(bet_type)

    def update_bet_amount_model_1(self, bet_type: BetType):
        bets_sequence = [25, 75, 200, 400, 900, 1800]
        self.__num_bet_lost[bet_type] += 1
        self.__bet_amount[bet_type] = bets_sequence[self.__num_bet_lost[bet_type]]
        self.__max_bet = max(self.__max_bet, self.__bet_amount[bet_type])

    def update_bet_amount_model_2(self, bet_type: BetType):
        bets_sequence = [25, 50, 100, 200, 450, 900, 1800]
        self.__num_bet_lost[bet_type] += 1
        self.__bet_amount[bet_type] = bets_sequence[self.__num_bet_lost[bet_type]]
        self.__max_bet = max(self.__max_bet, self.__bet_amount[bet_type])

    def update_bet_amount_aggressive(self, bet_type: BetType):
        previous_bet = self.__bet_amount[bet_type]
        self.__bet_amount[bet_type] *= self.__bet_factor_growth
        self.__bet_amount[bet_type] += previous_bet
        self.__bet_amount[bet_type] = round(self.__bet_amount[bet_type])
        while self.__bet_amount[bet_type] % self.__MINIMUM_BET != 0:
            self.__bet_amount[bet_type] += 1.0
        if self.__is_max_amount_lost_exceeded(bet_type):
            self.set_max_bet_amount(bet_type)
        self.__max_bet = max(self.__max_bet, self.__bet_amount[bet_type])

    def __is_max_amount_lost_exceeded(self, bet_type: BetType) -> bool:
        if bet_type.is_two_options_bet():
            return self.__bet_amount[bet_type] > self.__MAX_AMOUNT_LOST_TWO_OPTIONS_BET
        return self.__bet_amount[bet_type] > self.__MAX_AMOUNT_LOST_THREE_OPTIONS_BET

    def is_max_amount_lost(self, bet_type: BetType) -> bool:
        if bet_type.is_two_options_bet():
            return self.__bet_amount[bet_type] == self.__MAX_AMOUNT_LOST_TWO_OPTIONS_BET
        return self.__bet_amount[bet_type] == self.__MAX_AMOUNT_LOST_THREE_OPTIONS_BET

    def update_accumulated_bet(self, bet_type: BetType):
        self.__accumulated_bet[bet_type] += self.__bet_amount[bet_type]
        self.__max_accumulated_bet = max(self.__max_accumulated_bet, sum(self.__accumulated_bet.values()))

    def reset_all_bet_amount(self):
        self.__bet_amount = {
            BetType.RED_BET: self.__initial_bet,
            BetType.BLACK_BET: self.__initial_bet,
            BetType.EVEN_BET: self.__initial_bet,
            BetType.ODDS_BET: self.__initial_bet,
            BetType.FIRST_HALF: self.__initial_bet,
            BetType.SECOND_HALF: self.__initial_bet,
            BetType.FIRST_THIRD: self.__initial_bet,
            BetType.SECOND_THIRD: self.__initial_bet,
            BetType.THIRD_THIRD: self.__initial_bet,
            BetType.FIRST_COLUMN: self.__initial_bet,
            BetType.SECOND_COLUMN: self.__initial_bet,
            BetType.THIRD_COLUMN: self.__initial_bet,
        }
        self.__accumulated_bet = {
            BetType.RED_BET: 0.0,
            BetType.BLACK_BET: 0.0,
            BetType.EVEN_BET: 0.0,
            BetType.ODDS_BET: 0.0,
            BetType.FIRST_HALF: 0.0,
            BetType.SECOND_HALF: 0.0,
            BetType.FIRST_THIRD: 0.0,
            BetType.SECOND_THIRD: 0.0,
            BetType.THIRD_THIRD: 0.0,
            BetType.FIRST_COLUMN: 0.0,
            BetType.SECOND_COLUMN: 0.0,
            BetType.THIRD_COLUMN: 0.0,
        }

    def reset_bet_amount(self, bet_type: BetType):
        self.__accumulated_bet[bet_type] = 0
        self.__num_bet_lost[bet_type] = 0
        self.__bet_amount[bet_type] = self.__initial_bet

    def set_max_bet_amount(self, bet_type: BetType):
        if bet_type.is_two_options_bet():
            self.__bet_amount[bet_type] = self.__MAX_AMOUNT_LOST_TWO_OPTIONS_BET
        else:
            self.__bet_amount[bet_type] = self.__MAX_AMOUNT_LOST_THREE_OPTIONS_BET

    def get_bet_accumulated(self, bet_type: BetType) -> float:
        return self.__accumulated_bet[bet_type]

    def get_max_bet_accumulated(self) -> float:
        return self.__max_accumulated_bet

    def get_max_bet(self) -> float:
        return self.__max_bet

    def get_max_balance(self) -> float:
        return self.__max_balance

    def get_min_balance(self) -> float:
        return self.__min_balance

    def __reset_max_balance(self):
        self.__max_balance = 0.0

    def __reset_min_balance(self):
        self.__min_balance = 0.0

    def display(self):
        locale.setlocale(locale.LC_ALL, 'en_EU')
        print('\n\n----------------------------- WALLET STATISTICS --------------------------')
        print('Max bet amount required:\t\t%s %s' % (f"{self.__max_bet:,.1f}", u"\N{euro sign}"))
        print('Max accumulated bet required:\t%s %s' % (f"{self.__max_accumulated_bet:,.1f}", u"\N{euro sign}"))
        print('Min balance during game:\t\t%s %s' % (f"{self.__min_balance:,.1f}", u"\N{euro sign}"))
        print('Max balance during game:\t\t%s %s' % (f"{self.__max_balance:,.1f}", u"\N{euro sign}"))
        print('Final balance after game:\t\t%s %s' % (f"{self.__balance:,.1f}", u"\N{euro sign}"))

    def write(self, f):
        locale.setlocale(locale.LC_ALL, 'en_EU')
        f.write('\n\n----------------------------- WALLET STATISTICS --------------------------\n')
        f.write('Max bet amount required:\t\t%s %s\n' % (f"{self.__max_bet:,.1f}", u"\N{euro sign}"))
        f.write('Max accumulated bet required:\t%s %s\n' % (f"{self.__max_accumulated_bet:,.1f}", u"\N{euro sign}"))
        f.write('Min balance during game:\t\t%s %s\n' % (f"{self.__min_balance:,.1f}", u"\N{euro sign}"))
        f.write('Max balance during game:\t\t%s %s\n' % (f"{self.__max_balance:,.1f}", u"\N{euro sign}"))
        f.write('Final balance after game:\t\t%s %s\n' % (f"{self.__balance:,.1f}", u"\N{euro sign}"))
