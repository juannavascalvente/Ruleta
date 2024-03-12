from awscli.compat import raw_input

from Roulette.BetController import BetController, write_throws
from Roulette.ColorThrow import ColorThrow
from Roulette.LogController import LogController
from Roulette.ResultDisplay import ResultDisplay
from Roulette.Statistics import Statistics
from Roulette.ThrowGenerator import ThrowGenerator
from Roulette.Wallet import Wallet
from Roulette.ZeroType import ZeroType


def get_number() -> int:
    is_correct_number = False
    number = -1
    while not is_correct_number:
        input_data = ""
        try:
            input_data = raw_input("Enter result from Roulette!\n")
            if len(input_data) > 2:
                LogController.display(f'Wrong number entered \'{number}\', MUST be 00 or between 0 and 36')
            else:
                if input_data == "00":
                    number = 37
                    LogController.display("You entered 00")
                else:
                    number = int(input_data)
                    LogController.display("You entered %d" % number)
                if (number >= 0) and (number <= 37):
                    is_correct_number = True
                else:
                    LogController.display(f'Wrong number entered \'{number}\', MUST be 00 or between 0 and 36')
        except ValueError:
            LogController.display(f'Wrong number entered \'{input_data}\', MUST be 00 or between 0 and 36')

    return number


class Game:
    __INITIAL_BET = 25
    __TWO_OPTIONS_LEN = 5
    __THREE_OPTIONS_LEN = 5
    __TWO_OPTIONS_STOP_LEN = 11
    __THREE_OPTIONS_STOP_LEN = 8

    __MODEL_1 = 1
    __MODEL_2 = 2
    __MODEL_3 = 3

    __MAX_NUM_THROWS = 1000000

    def __init__(self, data):
        self.__wallet = Wallet(self.__INITIAL_BET)
        self.__bet_controller = BetController(self.__wallet, data['BET_MODEL'])
        self.__statistics = Statistics()
        self.__throw_generator = ThrowGenerator(data['TWO_OPTIONS_LEN'], data['THREE_OPTIONS_LEN'],
                                                data['COMBINED_OPTIONS_LEN'])
        self.__is_interactive = data['INTERACTIVE']
        self.__is_live = data['LIVE']
        self.__min_num_throws = max(data['TWO_OPTIONS_LEN'], data['THREE_OPTIONS_LEN'], data['COMBINED_OPTIONS_LEN'])
        if self.__is_live:
            self.__num_throws = self.__MAX_NUM_THROWS
        else:
            self.__num_throws = data['NUM_THROWS']

    def play(self):
        self.__bet_controller.reset_all_bet_amount()
        self.__bet_controller.init_balance()

        self.__throw_generator.set_num_throws(self.__num_throws)
        if self.__is_live:
            self.__play_live()
        else:
            self.__play()

        self.__statistics.update(self.__throw_generator.get_throws(), self.__bet_controller.get_bets_history())
        self.__statistics.display(self.__wallet)
        self.__statistics.write(self.__wallet)

        LogController.close()

    def display(self):
        color_throw = ColorThrow()
        for value in self.__throw_generator.get_throws():
            if color_throw.is_red(value):
                LogController.display(value)
            elif color_throw.is_black(value):
                LogController.display(value)
            else:
                if value == ZeroType.DOUBLE_ZERO:
                    LogController.display("00")
                else:
                    LogController.display(value)

    def __play(self):
        self.__throw_generator.generate()
        LogController.write('Throws: ' + str(self.__throw_generator.get_throws()) + '\n')

        for i in range(1, self.__throw_generator.get_num_throws() + 1):

            if i < self.__min_num_throws:
                LogController.log('Not enough data in iteration ' + str(i) + '\n')
                self.__bet_controller.add_history_not_bet()
                continue

            two_options_throws = self.__throw_generator.get_last_throws_for_two_options(i)
            three_options_throws = self.__throw_generator.get_last_throws_for_three_options(i)
            combined_throws = self.__throw_generator.get_last_throws_for_combined_options(i)
            if self.__bet_controller.compute_bet(two_options_throws, three_options_throws, combined_throws):
                write_throws(two_options_throws)
                current_throw = self.__throw_generator.get_throw(i - 1)

                if self.__is_interactive:
                    last_throws = self.__throw_generator.get_throws_range(i - self.__min_num_throws - 1, i - 1)
                    LogController.display('Last throws are: ' + str(last_throws))
                    self.__bet_controller.display_bets()
                    input("Press Enter to continue...")

                ResultDisplay.log(current_throw)

                for bet_type in self.__bet_controller.get_bet():
                    self.__bet_controller.process(bet_type, current_throw)
            else:
                if self.__is_interactive:
                    last_throws = self.__throw_generator.get_throws_range(i - self.__min_num_throws - 1, i - 1)
                    LogController.display('Last 10 throws are: ' + str(last_throws))
                    self.__bet_controller.display_bets()
                    LogController.display('No bet recommendation in iteration ' + str(i) + '\n')
                    input("Press Enter to continue...")

                LogController.write('No bet recommendation in iteration ' + str(i) + '\n')

            self.__bet_controller.reset_bet()
            LogController.display_header_end()
            LogController.flush()

    def __play_live(self):
        for i in range(1, self.__throw_generator.get_num_throws() + 1):

            if i <= self.__min_num_throws:

                LogController.log('Not enough data in iteration ' + str(i) + '\n')
                number = get_number()
                self.__throw_generator.add_throw(number)
                self.__bet_controller.add_history_not_bet()
                continue

            two_options_throws = self.__throw_generator.get_last_throws_for_two_options(i)
            three_options_throws = self.__throw_generator.get_last_throws_for_three_options(i)
            combined_throws = self.__throw_generator.get_last_throws_for_combined_options(i)
            if self.__bet_controller.compute_bet(two_options_throws, three_options_throws, combined_throws):
                write_throws(three_options_throws)

                last_throws = self.__throw_generator.get_throws_range(i - self.__min_num_throws - 1, i - 1)
                LogController.display('Last throws are: ' + str(last_throws))
                self.__bet_controller.display_bets()

                number = get_number()
                self.__throw_generator.add_throw(number)
                current_throw = self.__throw_generator.get_throw(i - 1)
                ResultDisplay.log(current_throw)

                for bet_type in self.__bet_controller.get_bet():
                    self.__bet_controller.process(bet_type, current_throw)
            else:
                LogController.display('No bet recommendation in iteration ' + str(i) + '\n')
                number = get_number()
                self.__throw_generator.add_throw(number)

            self.__bet_controller.reset_bet()
            self.__bet_controller.display()
            LogController.display_header_end()
            LogController.flush()
