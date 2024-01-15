class BetColorStats:

    def __init__(self):
        self.num_bets = 0
        self.num_reds_bets = 0
        self.num_reds_bets_won = 0
        self.num_blacks_bets = 0
        self.num_blacks_bets_won = 0

    def __increase_bets(self):
        self.num_bets += 1

    def __increase_red_bets(self):
        self.num_reds_bets += 1

    def increase_red_bets_won(self):
        self.__increase_bets()
        self.__increase_red_bets()
        self.num_reds_bets_won += 1

    def increase_red_bets_lost(self):
        self.__increase_bets()
        self.__increase_red_bets()

    def __increase_black_bets(self):
        self.num_blacks_bets += 1

    def increase_black_bets_won(self):
        self.__increase_bets()
        self.__increase_black_bets()
        self.num_blacks_bets_won += 1

    def increase_black_bets_lost(self):
        self.__increase_bets()
        self.__increase_black_bets()

    def display(self):
        print('--------------------------------- COLORS STATS ---------------------------------')
        print('Number of color bets: ' + str(self.num_bets))
        if self.num_bets > 0:
            if self.num_reds_bets > 0:
                print('Number of RED color bets: ' + str(self.num_reds_bets))
                print('Correct RED color bets: %d (%0.1f perc)' %
                      (self.num_reds_bets_won, 100.0*(float(self.num_reds_bets_won) / float(self.num_reds_bets))))
            else:
                print('No RED bets')

            if self.num_blacks_bets > 0:
                print('Number of BLACK color bets: ' + str(self.num_blacks_bets))
                print('Correct BLACK color bets: %d (%0.1f perc)' %
                      (self.num_blacks_bets_won, 100.0*(float(self.num_blacks_bets_won) / float(self.num_blacks_bets))))
            else:
                print('No BLACK bets')
