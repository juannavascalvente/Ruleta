from Roulette import ColumnSelector


class StatisticsColumns:
    
    __BET_SEQUENCE_THRESHOLD = 5

    def __init__(self):
        self.num_columns_sequences = 0
        self.num_consecutive_first_column = 0
        self.consecutive_first_column = {}
        self.num_consecutive_second_column = 0
        self.consecutive_second_column = {}
        self.num_consecutive_third_column = 0
        self.consecutive_third_column = {}
        self.__num_first_column = 0
        self.__num_second_column = 0
        self.__num_third_column = 0
        self.num_throws = 0
        self.__num_zeros = 0
        self.__columnSelector = ColumnSelector.ColumnSelector()

        self.__num_consecutive_not_first_column = 0
        self.__consecutive_not_first_column = {}
        self.__num_consecutive_not_second_column = 0
        self.__consecutive_not_second_column = {}
        self.__num_consecutive_not_third_column = 0
        self.__consecutive_not_third_column = {}

    def update_columns_stats(self, values):
        is_first_column = False
        is_second_column = False
        is_third_column = False
        self.num_consecutive_first_column = 0
        self.num_consecutive_second_column = 0
        self.num_consecutive_third_column = 0
        self.num_columns_sequences = 0
        for value in values:
            self.num_throws += 1
            if self.__columnSelector.is_first_column(value):
                self.__num_consecutive_not_second_column += 1
                self.__num_consecutive_not_third_column += 1
                self.__num_first_column += 1
                if is_first_column:
                    self.num_consecutive_first_column += 1
                else:
                    self.num_consecutive_first_column = 1

                    self.__update_consecutive_second_column()
                    self.__update_consecutive_third_column()

                self.__update_consecutive_not_first_column()

                is_first_column = True
                is_second_column = False
                is_third_column = False
            elif self.__columnSelector.is_second_column(value):
                self.__num_consecutive_not_first_column += 1
                self.__num_consecutive_not_third_column += 1
                self.__num_second_column += 1
                if is_second_column:
                    self.num_consecutive_second_column += 1
                else:
                    self.num_consecutive_second_column = 1

                    self.__update_consecutive_first_column()
                    self.__update_consecutive_third_column()

                self.__update_consecutive_not_second_column()

                is_first_column = False
                is_second_column = True
                is_third_column = False
            elif self.__columnSelector.is_third_column(value):
                self.__num_consecutive_not_first_column += 1
                self.__num_consecutive_not_second_column += 1
                self.__num_third_column += 1
                if is_third_column:
                    self.num_consecutive_third_column += 1
                else:
                    self.num_consecutive_third_column = 1

                    self.__update_consecutive_first_column()
                    self.__update_consecutive_second_column()

                self.__update_consecutive_not_third_column()

                is_first_column = False
                is_second_column = False
                is_third_column = True
            else:
                self.__num_zeros += 1
                is_first_column = False
                is_second_column = False
                is_third_column = False

                self.__update_consecutive_second_column()
                self.__update_consecutive_second_column()
                self.__update_consecutive_third_column()

        if is_first_column:
            self.__update_consecutive_second_column()
            self.__update_consecutive_third_column()
            if self.num_columns_sequences == 0:
                self.num_columns_sequences += 1
                self.__update_consecutive_first_column()
        elif is_second_column:
            self.__update_consecutive_first_column()
            self.__update_consecutive_third_column()
            if self.num_columns_sequences == 0:
                self.num_columns_sequences += 1
                self.__update_consecutive_second_column()
        elif is_third_column:
            self.__update_consecutive_first_column()
            self.__update_consecutive_second_column()
            if self.num_columns_sequences == 0:
                self.num_columns_sequences += 1
                self.__update_consecutive_third_column()

        self.__update_consecutive_not_first_column()
        self.__update_consecutive_not_second_column()
        self.__update_consecutive_not_third_column()

    def __update_consecutive_first_column(self):
        if self.num_consecutive_first_column > 0:
            self.num_columns_sequences += 1
            if self.num_consecutive_first_column in self.consecutive_first_column:
                self.consecutive_first_column[self.num_consecutive_first_column] += 1
            else:
                self.consecutive_first_column[self.num_consecutive_first_column] = 1
            self.num_consecutive_first_column = 0

    def __update_consecutive_second_column(self):
        if self.num_consecutive_second_column > 0:
            self.num_columns_sequences += 1
            if self.num_consecutive_second_column in self.consecutive_second_column:
                self.consecutive_second_column[self.num_consecutive_second_column] += 1
            else:
                self.consecutive_second_column[self.num_consecutive_second_column] = 1
        self.num_consecutive_second_column = 0

    def __update_consecutive_third_column(self):
        if self.num_consecutive_third_column > 0:
            self.num_columns_sequences += 1
            if self.num_consecutive_third_column in self.consecutive_third_column:
                self.consecutive_third_column[self.num_consecutive_third_column] += 1
            else:
                self.consecutive_third_column[self.num_consecutive_third_column] = 1
        self.num_consecutive_third_column = 0

    def __update_consecutive_not_first_column(self):
        if self.__num_consecutive_not_first_column > 0:
            if self.__num_consecutive_not_first_column in self.__consecutive_not_first_column:
                self.__consecutive_not_first_column[self.__num_consecutive_not_first_column] += 1
            else:
                self.__consecutive_not_first_column[self.__num_consecutive_not_first_column] = 1
        self.__num_consecutive_not_first_column = 0

    def __update_consecutive_not_second_column(self):
        if self.__num_consecutive_not_second_column > 0:
            if self.__num_consecutive_not_second_column in self.__consecutive_not_second_column:
                self.__consecutive_not_second_column[self.__num_consecutive_not_second_column] += 1
            else:
                self.__consecutive_not_second_column[self.__num_consecutive_not_second_column] = 1
        self.__num_consecutive_not_second_column = 0

    def __update_consecutive_not_third_column(self):
        if self.__num_consecutive_not_third_column > 0:
            if self.__num_consecutive_not_third_column in self.__consecutive_not_third_column:
                self.__consecutive_not_third_column[self.__num_consecutive_not_third_column] += 1
            else:
                self.__consecutive_not_third_column[self.__num_consecutive_not_third_column] = 1
        self.__num_consecutive_not_third_column = 0

    def write_columns_stats(self, f):
        f.write('------------------------------ COLUMNS ------------------------------\n')
        f.write('Number of columns sequences: ' + str(self.num_columns_sequences) + '\n')
        f.write('1st Column:\n')
        i = 0
        num_six_or_higher = 0
        for item in sorted(self.consecutive_first_column):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.consecutive_first_column[item], (float(self.consecutive_first_column[item]) /
                                                           float(self.num_columns_sequences) * 100.0)) + ' %\n')
            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += self.consecutive_first_column[item]

        f.write('2nd Column:\n')
        i = 0
        for item in sorted(self.consecutive_second_column):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.consecutive_second_column[item], (float(self.consecutive_second_column[item]) /
                                                            float(self.num_columns_sequences) * 100.0)) +
                    ' %\n')
            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += self.consecutive_second_column[item]

        f.write('3rd Column:\n')
        i = 0
        for item in sorted(self.consecutive_third_column):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.consecutive_third_column[item], (float(self.consecutive_third_column[item]) /
                                                           float(self.num_columns_sequences) * 100.0)) +
                    ' %\n')
            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += self.consecutive_third_column[item]

        f.write('Not 1st Column:\n')
        i = 0
        for item in sorted(self.__consecutive_not_first_column):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.__consecutive_not_first_column[item], (float(self.__consecutive_not_first_column[item]) /
                                                                 float(self.num_columns_sequences)
                                                                 * 100.0)) + ' %\n')

        f.write('Not 2nd Column:\n')
        i = 0
        for item in sorted(self.__consecutive_not_second_column):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.__consecutive_not_second_column[item], (float(self.__consecutive_not_second_column[item]) /
                                                                  float(self.num_columns_sequences) * 100.0)) + ' %\n')

        f.write('Not 3rd Column:\n')
        i = 0
        for item in sorted(self.__consecutive_not_third_column):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.__consecutive_not_third_column[item], (float(self.__consecutive_not_third_column[item]) /
                                                                 float(self.num_columns_sequences) * 100.0)) + ' %\n')

        f.write('Num sequences higher than threshold: ' + str(num_six_or_higher) + '/' + str(self.num_columns_sequences)
                + '\n')
        f.write('Percentage sequences higher than threshold: %.1f\n' %
                (float(num_six_or_higher) / float(self.num_columns_sequences) * 100.0))
        f.write('Percentage ZERO or DOUBLE ZERO %.1f\n' % (float(self.__num_zeros) / float(self.num_throws)
                                                           * 100.0))
        f.write('Percentage 1st COLUMN %.1f\n' % (float(self.__num_first_column) / float(self.num_throws) * 100.0))
        f.write('Percentage 2nd COLUMN %.1f\n' % (float(self.__num_second_column) / float(self.num_throws) * 100.0))
        f.write('Percentage 3rd COLUMN %.1f\n' % (float(self.__num_third_column) / float(self.num_throws) * 100.0))
        assert (self.__num_first_column + self.__num_second_column + self.__num_third_column + self.__num_zeros ==
                self.num_throws)
