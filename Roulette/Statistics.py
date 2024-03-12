from Roulette import BetType, StatisticsDataThird, StatisticsDataHalf
from Roulette import ColorThrow
from Roulette import ColumnSelector
from Roulette import EvenOddThrow
from Roulette import LogController
from Roulette import RowSelector
from Roulette import StatsUtil
from Roulette import ThirdSelector
from Roulette import Wallet

from Roulette import BetsColorStats
from Roulette import BetsEvenOddStats
from Roulette import BetsHalvesStats


class Statistics:
    TWO_OPTIONS_THRESHOLD = 5
    ZERO_VALUE = 0
    DOUBLE_ZERO_VALUE = 37
    BET_SEQUENCE_THRESHOLD = TWO_OPTIONS_THRESHOLD

    def __init__(self):
        self.throws = []
        self.num_throws = 0

        self.__stats_color = StatisticsDataHalf.StatisticsDataHalf('RED', 'BLACK', ColorThrow.ColorThrow())
        self.__stats_even_odd = StatisticsDataHalf.StatisticsDataHalf('EVEN', 'ODD', EvenOddThrow.EvenOddThrow())
        self.__stats_halves = StatisticsDataHalf.StatisticsDataHalf('1st HALF', '2nd HALF', RowSelector.RowSelector())
        self.__stats_columns = StatisticsDataThird.StatisticsDataThird('1st column', '2nd column', '3rd column',
                                                                       ColumnSelector.ColumnSelector())
        self.__stats_thirds = StatisticsDataThird.StatisticsDataThird('1st third', '2nd third', '3rd third',
                                                                      ThirdSelector.ThirdSelector())

        self.bets_history = [[BetType.BetType]]
        self.bets_per_iteration = {}
        self.bets_color_stats = BetsColorStats.BetColorStats()
        self.bets_even_odd_stats = BetsEvenOddStats.BetEvenOddStats()
        self.bets_halves_stats = BetsHalvesStats.BetHalvesStats()

        self.__color_throw = ColorThrow.ColorThrow()
        self.__even_odd_throw = EvenOddThrow
        self.__row_selector = RowSelector.RowSelector()
        self.__columnSelector = ColumnSelector.ColumnSelector()

    def update(self, throws: [int], bets_history: []):
        self.throws = throws
        self.bets_history = bets_history
        self.num_throws = len(self.throws)

        self.__stats_color.update_stats(throws)
        self.__stats_even_odd.update_stats(throws)
        self.__stats_halves.update_stats(throws)
        self.__stats_thirds.update_stats(throws)
        self.__stats_columns.update_stats(throws)

        self.__compute_forecast_stats()

    def display(self, wallet: Wallet):
        self.__display_bets_forecast()
        wallet.log()

    def write(self, wallet: Wallet):
        self.__stats_even_odd.write_stats()
        self.__stats_color.write_stats()
        self.__stats_halves.write_stats()
        self.__stats_columns.write_stats()
        self.__stats_thirds.write_stats()
        self.__write_bets_per_throw()
        wallet.log()

    def __write_bets_per_throw(self):
        LogController.LogController.display_header('BETS STATISTICS')
        LogController.LogController.write('Number of throws ->\t\t\t\t\t' + str(self.num_throws) + '\n')
        total_bets = 0
        for item in sorted(self.bets_per_iteration):
            LogController.LogController.write('Number of bets in iteration ' + str(item) + ' ->\t' +
                                              str(self.bets_per_iteration[item]) + '\n')
            total_bets += self.bets_per_iteration[item]
        LogController.LogController.write('Number of bets ->\t\t\t\t\t' + str(total_bets) + '\n')
        LogController.LogController.write('Percentage of bets in game ->\t\t%0.1f\n' %
                                          StatsUtil.StatsUtil.percentage(total_bets, self.num_throws))

    def __compute_forecast_stats(self):
        for (throw, bets_in_throw) in zip(self.throws, self.bets_history):
            num_bets = 0
            for bet in bets_in_throw:
                if BetType.BetTypeChecker.is_no_bet(bet):
                    continue

                num_bets += 1
                if BetType.BetTypeChecker.is_color_bet(bet):
                    self.__compute_color_stats(bet, throw)
                elif BetType.BetTypeChecker.is_even_odd_bet(bet):
                    self.__compute_even_odd_stats(bet, throw)
                elif BetType.BetTypeChecker.is_halves_bet(bet):
                    self.__compute_halves_stats(bet, throw)

            if num_bets > 0:
                if num_bets in self.bets_per_iteration:
                    self.bets_per_iteration[num_bets] += 1
                else:
                    self.bets_per_iteration[num_bets] = 1

    def __compute_color_stats(self, bet: BetType.BetType, throw: int):
        if BetType.BetTypeChecker.is_red_bet(bet):
            if self.__color_throw.is_a(throw):
                self.bets_color_stats.increase_red_bets_won()
            else:
                self.bets_color_stats.increase_red_bets_lost()
        elif BetType.BetTypeChecker.is_black_bet(bet):
            if self.__color_throw.is_b(throw):
                self.bets_color_stats.increase_black_bets_won()
            else:
                self.bets_color_stats.increase_black_bets_lost()

    def __compute_even_odd_stats(self, bet: BetType.BetType, throw: int):
        if BetType.BetTypeChecker.is_even_bet(bet):
            if self.__even_odd_throw.is_even(throw):
                self.bets_even_odd_stats.increase_even_bets_won()
            else:
                self.bets_even_odd_stats.increase_even_bets_lost()
        elif BetType.BetTypeChecker.is_odd_bet(bet):
            if self.__even_odd_throw.is_odd(throw):
                self.bets_even_odd_stats.increase_odd_bets_won()
            else:
                self.bets_even_odd_stats.increase_odd_bets_lost()

    def __compute_halves_stats(self, bet: BetType.BetType, throw: int):
        if BetType.BetTypeChecker.is_first_half_bet(bet):
            if self.__row_selector.is_a(throw):
                self.bets_halves_stats.increase_first_half_bets_won()
            else:
                self.bets_halves_stats.increase_first_half_bets_lost()
        elif BetType.BetTypeChecker.is_second_half_bet(bet):
            if self.__row_selector.is_b(throw):
                self.bets_halves_stats.increase_second_half_bets_won()
            else:
                self.bets_halves_stats.increase_second_half_bets_lost()

    def __display_bets_forecast(self):
        self.bets_color_stats.display()
        self.bets_even_odd_stats.display()
        self.bets_halves_stats.display()
