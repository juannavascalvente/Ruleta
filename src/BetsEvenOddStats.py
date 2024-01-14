class BetEvenOddStats:
    def __init__(self):
        self.num_bets = 0
        self.num_evens_bets = 0
        self.num_evens_bets_won = 0
        self.num_odds_bets = 0
        self.num_odds_bets_won = 0

    def __increase_bets(self):
        self.num_bets += 1

    def __increase_even_bets(self):
        self.num_evens_bets += 1

    def increase_even_bets_won(self):
        self.__increase_bets()
        self.__increase_even_bets()
        self.num_evens_bets_won += 1

    def increase_even_bets_lost(self):
        self.__increase_bets()
        self.__increase_even_bets()

    def __increase_odd_bets(self):
        self.num_odds_bets += 1

    def increase_odd_bets_won(self):
        self.__increase_bets()
        self.__increase_odd_bets()
        self.num_odds_bets_won += 1

    def increase_odd_bets_lost(self):
        self.__increase_bets()
        self.__increase_odd_bets()

    def display(self):
        print('--------------------------------- EVEN/ODD STATS ---------------------------------')
        print('Number of even/odd bets: ' + str(self.num_bets))
        if self.num_bets > 0:
            if self.num_evens_bets > 0:
                print('Number of EVEN bets: ' + str(self.num_evens_bets))
                print('Correct EVEN bets: %d (%0.1f perc)' % (self.num_evens_bets_won,
                                                              100.0*(float(self.num_evens_bets_won) /
                                                                     float(self.num_evens_bets))))
            else:
                print('No EVEN bets')

            if self.num_odds_bets > 0:
                print('Number of ODD bets: ' + str(self.num_odds_bets))
                print('Correct ODD bets: %d (%0.1f perc)' % (self.num_odds_bets_won,
                                                             100.0*(float(self.num_odds_bets_won) /
                                                                    float(self.num_odds_bets))))
            else:
                print('No ODD bets')
