from Roulette import RowSelector


class StatisticsThirds:
    
    __BET_SEQUENCE_THRESHOLD = 5

    def __init__(self):
        self.num_thirds_sequences = 0
        self.num_consecutive_first_third = 0
        self.consecutive_first_third = {}
        self.num_consecutive_second_third = 0
        self.consecutive_second_third = {}
        self.num_consecutive_third_third = 0
        self.consecutive_third_third = {}
        self.__num_first_third = 0
        self.__num_second_third = 0
        self.__num_third_third = 0
        self.num_throws = 0
        self.__num_zeros = 0
        self.__thirdSelector = RowSelector.RowSelector()

        self.__num_consecutive_not_first_third = 0
        self.__consecutive_not_first_third = {}
        self.__num_consecutive_not_second_third = 0
        self.__consecutive_not_second_third = {}
        self.__num_consecutive_not_third_third = 0
        self.__consecutive_not_third_third = {}

    def update_thirds_stats(self, values):
        is_first_third = False
        is_second_third = False
        is_third_third = False
        self.num_consecutive_first_third = 0
        self.num_consecutive_second_third = 0
        self.num_consecutive_third_third = 0
        self.num_thirds_sequences = 0
        for value in values:
            self.num_throws += 1
            if self.__thirdSelector.is_first_third(value):
                self.__num_consecutive_not_second_third += 1
                self.__num_consecutive_not_third_third += 1
                self.__num_first_third += 1
                if is_first_third:
                    self.num_consecutive_first_third += 1
                else:
                    self.num_consecutive_first_third = 1

                    if self.num_consecutive_second_third > 0:
                        self.num_thirds_sequences += 1
                        if self.num_consecutive_second_third in self.consecutive_second_third:
                            self.consecutive_second_third[self.num_consecutive_second_third] += 1
                        else:
                            self.consecutive_second_third[self.num_consecutive_second_third] = 1
                    if self.num_consecutive_third_third > 0:
                        self.num_thirds_sequences += 1
                        if self.num_consecutive_third_third in self.consecutive_third_third:
                            self.consecutive_third_third[self.num_consecutive_third_third] += 1
                        else:
                            self.consecutive_third_third[self.num_consecutive_third_third] = 1

                if self.__num_consecutive_not_first_third > 0:
                    if self.__num_consecutive_not_first_third in self.__consecutive_not_first_third:
                        self.__consecutive_not_first_third[self.__num_consecutive_not_first_third] += 1
                    else:
                        self.__consecutive_not_first_third[self.__num_consecutive_not_first_third] = 1
                self.__num_consecutive_not_first_third = 0

                self.num_consecutive_second_third = 0
                self.num_consecutive_third_third = 0
                is_first_third = True
                is_second_third = False
                is_third_third = False
            elif self.__thirdSelector.is_second_third(value):
                self.__num_consecutive_not_first_third += 1
                self.__num_consecutive_not_third_third += 1
                self.__num_second_third += 1
                if is_second_third:
                    self.num_consecutive_second_third += 1
                else:
                    self.num_consecutive_second_third = 1

                    if self.num_consecutive_first_third > 0:
                        self.num_thirds_sequences += 1
                        if self.num_consecutive_first_third in self.consecutive_first_third:
                            self.consecutive_first_third[self.num_consecutive_first_third] += 1
                        else:
                            self.consecutive_first_third[self.num_consecutive_first_third] = 1
                    if self.num_consecutive_third_third > 0:
                        self.num_thirds_sequences += 1
                        if self.num_consecutive_third_third in self.consecutive_third_third:
                            self.consecutive_third_third[self.num_consecutive_third_third] += 1
                        else:
                            self.consecutive_third_third[self.num_consecutive_third_third] = 1

                if self.__num_consecutive_not_second_third > 0:
                    if self.__num_consecutive_not_second_third in self.__consecutive_not_second_third:
                        self.__consecutive_not_second_third[self.__num_consecutive_not_second_third] += 1
                    else:
                        self.__consecutive_not_second_third[self.__num_consecutive_not_second_third] = 1
                self.__num_consecutive_not_second_third = 0

                self.num_consecutive_first_third = 0
                self.num_consecutive_third_third = 0
                is_first_third = False
                is_second_third = True
                is_third_third = False
            elif self.__thirdSelector.is_third_third(value):
                self.__num_consecutive_not_first_third += 1
                self.__num_consecutive_not_second_third += 1
                self.__num_third_third += 1
                if is_third_third:
                    self.num_consecutive_third_third += 1
                else:
                    self.num_consecutive_third_third = 1

                    if self.num_consecutive_first_third > 0:
                        self.num_thirds_sequences += 1
                        if self.num_consecutive_first_third in self.consecutive_first_third:
                            self.consecutive_first_third[self.num_consecutive_first_third] += 1
                        else:
                            self.consecutive_first_third[self.num_consecutive_first_third] = 1
                    if self.num_consecutive_second_third > 0:
                        self.num_thirds_sequences += 1
                        if self.num_consecutive_second_third in self.consecutive_second_third:
                            self.consecutive_second_third[self.num_consecutive_second_third] += 1
                        else:
                            self.consecutive_second_third[self.num_consecutive_second_third] = 1

                if self.__num_consecutive_not_third_third > 0:
                    if self.__num_consecutive_not_third_third in self.__consecutive_not_third_third:
                        self.__consecutive_not_third_third[self.__num_consecutive_not_third_third] += 1
                    else:
                        self.__consecutive_not_third_third[self.__num_consecutive_not_third_third] = 1
                self.__num_consecutive_not_third_third = 0

                self.num_consecutive_first_third = 0
                self.num_consecutive_second_third = 0
                is_first_third = False
                is_second_third = False
                is_third_third = True
            else:
                self.__num_zeros += 1
                is_first_third = False
                is_second_third = False
                is_third_third = False
                self.num_thirds_sequences += 1

                if self.num_consecutive_first_third > 0:
                    self.num_thirds_sequences += 1
                    if self.num_consecutive_first_third in self.consecutive_first_third:
                        self.consecutive_first_third[self.num_consecutive_first_third] += 1
                    else:
                        self.consecutive_first_third[self.num_consecutive_first_third] = 1
                self.num_consecutive_first_third = 0

                if self.num_consecutive_second_third > 0:
                    self.num_thirds_sequences += 1
                    if self.num_consecutive_second_third in self.consecutive_second_third:
                        self.consecutive_second_third[self.num_consecutive_second_third] += 1
                    else:
                        self.consecutive_second_third[self.num_consecutive_second_third] = 1
                self.num_consecutive_second_third = 0

                if self.num_consecutive_third_third > 0:
                    self.num_thirds_sequences += 1
                    if self.num_consecutive_third_third in self.consecutive_third_third:
                        self.consecutive_third_third[self.num_consecutive_third_third] += 1
                    else:
                        self.consecutive_third_third[self.num_consecutive_third_third] = 1
                self.num_consecutive_third_third = 0

        self.num_thirds_sequences += 1

        if is_first_third:
            if self.num_consecutive_first_third > 0:
                self.num_thirds_sequences += 1
                if self.num_consecutive_first_third in self.consecutive_first_third:
                    self.consecutive_first_third[self.num_consecutive_first_third] += 1
                else:
                    self.consecutive_first_third[self.num_consecutive_first_third] = 1
            if self.num_consecutive_third_third > 0:
                self.num_thirds_sequences += 1
                if self.num_consecutive_third_third in self.consecutive_third_third:
                    self.consecutive_third_third[self.num_consecutive_third_third] += 1
                else:
                    self.consecutive_third_third[self.num_consecutive_third_third] = 1

        if is_second_third:
            if self.num_consecutive_first_third > 0:
                self.num_thirds_sequences += 1
                if self.num_consecutive_first_third in self.consecutive_first_third:
                    self.consecutive_first_third[self.num_consecutive_first_third] += 1
                else:
                    self.consecutive_first_third[self.num_consecutive_first_third] = 1
            if self.num_consecutive_third_third > 0:
                self.num_thirds_sequences += 1
                if self.num_consecutive_third_third in self.consecutive_third_third:
                    self.consecutive_third_third[self.num_consecutive_third_third] += 1
                else:
                    self.consecutive_third_third[self.num_consecutive_third_third] = 1

        if is_third_third:
            if self.num_consecutive_first_third > 0:
                self.num_thirds_sequences += 1
                if self.num_consecutive_first_third in self.consecutive_first_third:
                    self.consecutive_first_third[self.num_consecutive_first_third] += 1
                else:
                    self.consecutive_first_third[self.num_consecutive_first_third] = 1
            if self.num_consecutive_second_third > 0:
                self.num_thirds_sequences += 1
                if self.num_consecutive_second_third in self.consecutive_second_third:
                    self.consecutive_second_third[self.num_consecutive_second_third] += 1
                else:
                    self.consecutive_second_third[self.num_consecutive_second_third] = 1

        if self.__num_consecutive_not_first_third > 0:
            if self.__num_consecutive_not_first_third in self.__consecutive_not_first_third:
                self.__consecutive_not_first_third[self.__num_consecutive_not_first_third] += 1
            else:
                self.__consecutive_not_first_third[self.__num_consecutive_not_first_third] = 1

        if self.__num_consecutive_not_second_third > 0:
            if self.__num_consecutive_not_second_third in self.__consecutive_not_second_third:
                self.__consecutive_not_second_third[self.__num_consecutive_not_second_third] += 1
            else:
                self.__consecutive_not_second_third[self.__num_consecutive_not_second_third] = 1

        if self.__num_consecutive_not_third_third > 0:
            if self.__num_consecutive_not_third_third in self.__consecutive_not_third_third:
                self.__consecutive_not_third_third[self.__num_consecutive_not_third_third] += 1
            else:
                self.__consecutive_not_third_third[self.__num_consecutive_not_third_third] = 1

    def write_thirds_stats(self, f):
        f.write('------------------------------ THIRDS ------------------------------\n')
        f.write('Number of thirds sequences: ' + str(self.num_thirds_sequences) + '\n')
        f.write('1st Third:\n')
        i = 0
        num_six_or_higher = 0
        for item in sorted(self.consecutive_first_third):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.consecutive_first_third[item], (float(self.consecutive_first_third[item]) /
                                                          float(self.__num_first_third) * 100.0)) + ' %\n')
            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += self.consecutive_first_third[item]

        f.write('2nd Third:\n')
        i = 0
        for item in sorted(self.consecutive_second_third):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.consecutive_second_third[item], (float(self.consecutive_second_third[item]) /
                                                           float(self.__num_second_third) * 100.0)) +
                    ' %\n')
            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += self.consecutive_second_third[item]

        f.write('3rd Third:\n')
        i = 0
        for item in sorted(self.consecutive_third_third):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.consecutive_third_third[item], (float(self.consecutive_third_third[item]) /
                                                          float(self.__num_third_third) * 100.0)) +
                    ' %\n')
            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += self.consecutive_third_third[item]

        f.write('Not 1st Third:\n')
        i = 0
        for item in sorted(self.__consecutive_not_first_third):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.__consecutive_not_first_third[item], (float(self.__consecutive_not_first_third[item]) /
                                                                float(self.num_thirds_sequences) * 100.0)) + ' %\n')

        f.write('Not 2nd Third:\n')
        i = 0
        for item in sorted(self.__consecutive_not_second_third):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.__consecutive_not_second_third[item], (float(self.__consecutive_not_second_third[item]) /
                                                                 float(self.num_thirds_sequences) * 100.0)) + ' %\n')

        f.write('Not 3rd Third:\n')
        i = 0
        for item in sorted(self.__consecutive_not_third_third):
            i += 1
            f.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (self.__consecutive_not_third_third[item], (float(self.__consecutive_not_third_third[item]) /
                                                                float(self.num_thirds_sequences) * 100.0)) + ' %\n')

        f.write('Num sequences higher than threshold: ' + str(num_six_or_higher) + '/' + str(self.num_thirds_sequences)
                + '\n')
        f.write('Percentage sequences higher than threshold: %.1f\n' %
                (float(num_six_or_higher) / float(self.num_thirds_sequences) * 100.0))
        f.write('Percentage ZERO or DOUBLE ZERO %.1f\n' % (float(self.__num_zeros) / float(self.num_throws)
                                                           * 100.0))
        f.write('Percentage 1st THIRD %.1f\n' % (float(self.__num_first_third) / float(self.num_throws) * 100.0))
        f.write('Percentage 2nd THIRD %.1f\n' % (float(self.__num_second_third) / float(self.num_throws) * 100.0))
        f.write('Percentage 3rd THIRD %.1f\n' % (float(self.__num_third_third) / float(self.num_throws) * 100.0))
        assert (self.__num_first_third + self.__num_second_third + self.__num_third_third + self.__num_zeros ==
                self.num_throws)
