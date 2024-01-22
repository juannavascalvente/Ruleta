from awscli.compat import raw_input
from colorama import Fore

from Roulette.BetController import BetController, write_throws
from Roulette.ColorThrow import ColorThrow
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
            number = int(input_data)
            if (number >= 0) and (number <= 37):
                print("You entered %d" % number)
                is_correct_number = True
            else:
                print(f'Wrong number entered {number}, MUST be between 0 and 37 (00)')
        except ValueError:
            print(f'Wrong number entered {input_data}, MUST be between 0 and 37 (00)')

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

    # def __init__(self, initial_bet: int = __INITIAL_BET,
    #              num_throws_two_options: int = __TWO_OPTIONS_LEN,
    #              num_throws_three_options: int = __THREE_OPTIONS_LEN,
    #              num_throws_to_stop_two_options: int = __TWO_OPTIONS_STOP_LEN,
    #              num_throws_to_stop_three_options: int = __THREE_OPTIONS_STOP_LEN,
    #              model: int = __MODEL_3):
    def __init__(self, data):
        self.__wallet = Wallet(self.__INITIAL_BET)
        self.__bet_controller = BetController(self.__wallet, data['BET_MODEL'])
        self.__statistics = Statistics()
        self.__f = open("log.txt", "w")
        self.__throw_generator = ThrowGenerator(data['TWO_OPTIONS_LEN'], data['THREE_OPTIONS_LEN'])
        self.__is_interactive = data['INTERACTIVE']
        self.__is_live = data['LIVE']
        self.__min_num_throws = max(data['TWO_OPTIONS_LEN'], data['THREE_OPTIONS_LEN'])
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
        self.__statistics.write(self.__f, self.__wallet)

        self.__f.close()

    def display(self):
        color_throw = ColorThrow()
        for value in self.__throw_generator.get_throws():
            if color_throw.is_red(value):
                print(Fore.RED, value)
            elif color_throw.is_black(value):
                print(Fore.BLACK, value)
            else:
                if value == ZeroType.DOUBLE_ZERO:
                    print(Fore.GREEN, "00")
                else:
                    print(Fore.GREEN, value)

    def __play(self):
        self.__throw_generator.generate()
        self.__f.write('Throws: ' + str(self.__throw_generator.get_throws()) + '\n')

        for i in range(1, self.__throw_generator.get_num_throws() + 1):

            if i < self.__min_num_throws:
                self.__f.write('Not enough data in iteration ' + str(i) + '\n')
                self.__bet_controller.add_history_not_bet()
                continue

            last_throws_for_two_options = self.__throw_generator.get_last_throws_for_two_options(i)
            last_throws_for_three_options = self.__throw_generator.get_last_throws_for_three_options(i)
            if self.__bet_controller.compute_bet(last_throws_for_two_options, last_throws_for_three_options):
                write_throws(self.__f, last_throws_for_two_options)
                current_throw = self.__throw_generator.get_throw(i - 1)

                if self.__is_interactive:
                    last_throws = self.__throw_generator.get_throws_range(i - self.__min_num_throws - 1, i - 1)
                    print('Last throws are: ' + str(last_throws))
                    self.__bet_controller.display_bets()
                    input("Press Enter to continue...")
                    ResultDisplay.display(current_throw)

                ResultDisplay.write(self.__f, current_throw)

                for bet_type in self.__bet_controller.get_bet():
                    self.__f.write('Bet amount\t->\t' + str(self.__bet_controller.get_bet_amount(bet_type)) + '\n')
                    self.__bet_controller.update_accumulated_bet(bet_type)
                    self.__f.write(
                        'Bet accumulated\t->\t' + str(self.__bet_controller.get_bet_accumulated(bet_type)) + '\n')
                    self.__f.write(
                        'Max bet accumulated\t->\t' + str(self.__bet_controller.get_max_bet_accumulated()) + '\n')
                    self.__f.write('Balance\t\t->\t' + str(self.__bet_controller.get_bet_balance()) + '\n')
                    bet_type.write(self.__f)
                    if self.__bet_controller.is_win(bet_type, current_throw):
                        if self.__is_interactive:
                            print('**********\nBet WON\n**********\n')
                        self.__f.write('Bet WON\n')
                        self.__bet_controller.update_balance_win(bet_type)
                        self.__bet_controller.reset_bet_amount(bet_type)
                    else:
                        if self.__is_interactive:
                            print('**********\nBet LOST\n**********\n')
                        self.__f.write('Bet LOST\n')
                        self.__bet_controller.update_balance_lost(bet_type)
                        if self.__bet_controller.is_max_amount_lost(bet_type):
                            self.__f.write('TOO MANY Bets LOST\n')
                            self.__bet_controller.reset_bet_amount(bet_type)
                        else:
                            self.__bet_controller.update_bet_amount(bet_type)
                    self.__f.write('New balance\t\t->\t' + str(self.__bet_controller.get_bet_balance()) + '\n')
            else:
                if self.__is_interactive:
                    last_throws = self.__throw_generator.get_throws_range(i - self.__min_num_throws - 1, i - 1)
                    print('Last 10 throws are: ' + str(last_throws))
                    self.__bet_controller.display_bets()
                    print('No bet recommendation in iteration ' + str(i) + '\n')
                    input("Press Enter to continue...")

                self.__f.write('No bet recommendation in iteration ' + str(i) + '\n')

            self.__bet_controller.reset_bet()
            self.__f.write('------------------------------------------------------------------------------------\n')
            self.__f.flush()

    def __play_live(self):
        for i in range(1, self.__throw_generator.get_num_throws() + 1):

            if i <= self.__min_num_throws:
                self.__f.write('Not enough data in iteration ' + str(i) + '\n')
                number = get_number()
                self.__throw_generator.add_throw(number)
                self.__bet_controller.add_history_not_bet()
                continue

            last_throws_for_two_options = self.__throw_generator.get_last_throws_for_two_options(i)
            last_throws_for_three_options = self.__throw_generator.get_last_throws_for_three_options(i)
            if self.__bet_controller.compute_bet(last_throws_for_two_options, last_throws_for_three_options):
                write_throws(self.__f, last_throws_for_two_options)

                last_throws = self.__throw_generator.get_throws_range(i - self.__min_num_throws - 1, i - 1)
                print('Last 10 throws are: ' + str(last_throws))
                self.__bet_controller.display_bets()

                number = get_number()
                self.__throw_generator.add_throw(number)
                current_throw = self.__throw_generator.get_throw(i - 1)
                ResultDisplay.write(self.__f, current_throw)
                ResultDisplay.display(current_throw)

                for bet_type in self.__bet_controller.get_bet():
                    self.__f.write('Bet amount\t->\t' + str(self.__bet_controller.get_bet_amount(bet_type)) + '\n')
                    self.__bet_controller.update_accumulated_bet(bet_type)
                    self.__f.write(
                        'Bet accumulated\t->\t' + str(self.__bet_controller.get_bet_accumulated(bet_type)) + '\n')
                    self.__f.write(
                        'Max bet accumulated\t->\t' + str(self.__bet_controller.get_max_bet_accumulated()) + '\n')
                    self.__f.write('Balance\t\t->\t' + str(self.__bet_controller.get_bet_balance()) + '\n')
                    bet_type.write(self.__f)
                    bet_type.display()
                    if self.__bet_controller.is_win(bet_type, current_throw):
                        if self.__is_interactive:
                            print('**********\nBet WON\n**********')
                        self.__f.write('Bet WON\n')
                        self.__bet_controller.update_balance_win(bet_type)
                        self.__bet_controller.reset_bet_amount(bet_type)
                    else:
                        if self.__is_interactive:
                            print('**********\nBet LOST\n**********')
                        self.__f.write('Bet LOST\n')
                        self.__bet_controller.update_balance_lost(bet_type)
                        if self.__bet_controller.is_max_amount_lost(bet_type):
                            self.__f.write('TOO MANY Bets LOST\n')
                            self.__bet_controller.reset_bet_amount(bet_type)
                        else:
                            self.__bet_controller.update_bet_amount(bet_type)
                    self.__f.write('New balance\t\t->\t' + str(self.__bet_controller.get_bet_balance()) + '\n')
            else:
                self.__f.write('No bet recommendation in iteration ' + str(i) + '\n')

            self.__bet_controller.reset_bet()
            self.__f.write('------------------------------------------------------------------------------------\n')
            self.__f.flush()
