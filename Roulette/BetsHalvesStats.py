from Roulette.LogController import LogController


class BetHalvesStats:
    def __init__(self):
        self.num_bets = 0
        self.num_first_half_bets = 0
        self.num_first_half_bets_won = 0
        self.num_second_half_bets = 0
        self.num_second_half_bets_won = 0

    def __increase_bets(self):
        self.num_bets += 1

    def __increase_first_half_bets(self):
        self.num_first_half_bets += 1

    def increase_first_half_bets_won(self):
        self.__increase_bets()
        self.__increase_first_half_bets()
        self.num_first_half_bets_won += 1

    def increase_first_half_bets_lost(self):
        self.__increase_bets()
        self.__increase_first_half_bets()

    def __increase_second_half_bets(self):
        self.num_second_half_bets += 1

    def increase_second_half_bets_won(self):
        self.__increase_bets()
        self.__increase_second_half_bets()
        self.num_second_half_bets_won += 1

    def increase_second_half_bets_lost(self):
        self.__increase_bets()
        self.__increase_second_half_bets()

    def display(self):
        LogController.display_header('HALVES STATS')
        LogController.display('Number of HALVES bets: ' + str(self.num_bets))
        if self.num_bets > 0:
            if self.num_first_half_bets > 0:
                LogController.display('Number of 1st HALF bets: ' + str(self.num_first_half_bets))
                LogController.display('Correct 1st HALF bets: %d (%0.1f perc)' % (self.num_first_half_bets_won,
                                                                                  100.0 * (float(
                                                                                      self.num_first_half_bets_won) /
                                                                                    float(self.num_first_half_bets))))
            else:
                LogController.display('No 1st HALF bets')

            if self.num_second_half_bets > 0:
                LogController.display('Number of 2nd HALF bets: ' + str(self.num_second_half_bets))
                LogController.display('Correct 2nd HALF bets: %d (%0.1f perc)' % (self.num_second_half_bets_won,
                                                                                  100.0 * (float(
                                                                                      self.num_second_half_bets_won) /
                                                                                    float(self.num_second_half_bets))))
            else:
                LogController.display('No 2nd HALF bets')
