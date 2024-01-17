from Roulette import ThrowCheckerHalf, NonConsecutiveData


class StatisticsDataHalf:
    __BET_SEQUENCE_THRESHOLD = 5

    def __init__(self, optionA: str, optionB: str, throw_checker: ThrowCheckerHalf):
        self.__optionA = optionA
        self.__optionB = optionB
        self.__num_throws = 0

        self.__num_As = 0
        self.__num_Bs = 0
        self.__num_green = 0

        self.__throw_checker = throw_checker

        self.__consecutive_A = NonConsecutiveData.NonConsecutiveData(optionA)
        self.__consecutive_B = NonConsecutiveData.NonConsecutiveData(optionB)
        self.__consecutive_non_A = NonConsecutiveData.NonConsecutiveData('Non ' + optionA)
        self.__consecutive_non_B = NonConsecutiveData.NonConsecutiveData('Non ' + optionB)

    def __get_a_as_string(self) -> str:
        return self.__optionA

    def __get_b_as_string(self) -> str:
        return self.__optionB

    def __get_report_header(self) -> str:
        return '------------------------------ ' + self.__get_a_as_string() + '/' + self.__get_b_as_string() + \
            ' ------------------------------\n'

    def write_stats(self, f):
        f.write(self.__get_report_header())
        num_a_sequences_without_zeros = self.__consecutive_A.getNumSequences()
        num_b_sequences_without_zeros = self.__consecutive_B.getNumSequences()
        num_sequences_without_zeros = num_a_sequences_without_zeros + num_b_sequences_without_zeros
        f.write('Number of sequences (without zeros): ' + str(num_sequences_without_zeros) + '\n')

        num_a_sequences_with_zeros = self.__consecutive_non_A.getNumSequences()
        num_b_sequences_with_zeros = self.__consecutive_non_B.getNumSequences()
        num_sequences_with_zeros = num_a_sequences_with_zeros + num_b_sequences_with_zeros
        f.write('Number of sequences (with zeros): ' + str(num_sequences_with_zeros) + '\n')

        self.__write_option(f, self.__consecutive_A)

        self.__write_option(f, self.__consecutive_non_A)

        self.__write_option(f, self.__consecutive_B)

        self.__write_option(f, self.__consecutive_non_B)

        # num_six_or_higher = self.__consecutive_A.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
        #                     self.__consecutive_B.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
        #                     self.__consecutive_non_A.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
        #                     self.__consecutive_non_B.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD)
        # f.write('Num sequences higher than threshold: ' + str(num_six_or_higher) + '/' +
        #         str(num_sequences_without_zeros) + '\n')
        # if num_sequences_without_zeros == 0:
        #     f.write('Percentage sequences higher than threshold: 0 %\n')
        # else:
        #     f.write('Percentage sequences higher than threshold: %.1f\n' %
        #             (float(num_six_or_higher) / float(num_sequences_without_zeros) * 100.0))
        f.write('Percentage ZERO or DOUBLE ZERO %.1f\n' % (float(self.__num_green) / float(self.__num_throws)
                                                           * 100.0))
        f.write('Percentage ' + self.__get_a_as_string() + ' %.1f\n' % (float(self.__num_As) / float(self.__num_throws)
                                                                        * 100.0))
        f.write('Percentage ' + self.__get_b_as_string() + ' %.1f\n' % (float(self.__num_Bs) / float(self.__num_throws)
                                                                        * 100.0))
        assert (self.__num_As + self.__num_Bs + self.__num_green == self.__num_throws)

    def update_stats(self, values: [int]):
        self.__consecutive_A.reset()
        self.__consecutive_B.reset()
        self.__consecutive_non_A.reset()
        self.__consecutive_non_B.reset()

        for value in values:
            if self.__num_throws == 0:
                if self.__throw_checker.is_zero_or_double(value):
                    self.__num_green += 1
                    self.__consecutive_non_A.add(value)
                    self.__consecutive_non_B.add(value)
                elif self.__throw_checker.is_a(value):
                    self.__num_As += 1
                    self.__consecutive_A.add(value)
                    self.__consecutive_non_B.add(value)
                elif self.__throw_checker.is_b(value):
                    self.__num_Bs += 1
                    self.__consecutive_B.add(value)
                    self.__consecutive_non_A.add(value)

                self.__num_throws += 1
                continue

            self.__num_throws += 1
            if self.__throw_checker.is_zero_or_double(value):

                self.__num_green += 1
                self.__consecutive_A.save()
                self.__consecutive_non_B.add(value)
                self.__consecutive_B.save()
                self.__consecutive_non_A.add(value)

            elif self.__throw_checker.is_b(value):
                self.__num_Bs += 1

                self.__consecutive_A.save()
                self.__consecutive_non_B.save()

                self.__consecutive_B.add(value)
                self.__consecutive_non_A.add(value)

            else:
                self.__num_As += 1

                self.__consecutive_A.add(value)
                self.__consecutive_non_B.add(value)

                self.__consecutive_B.save()
                self.__consecutive_non_A.save()

        self.__consecutive_A.save()
        self.__consecutive_B.save()
        self.__consecutive_non_A.save()
        self.__consecutive_non_B.save()

    def __write_option(self, f, data: NonConsecutiveData):
        f.write(data.getOption() + ':\n')
        if data.isEmpty():
            f.write('\tNONE\n')
            return
        i = 0
        sequences = data.getSequences()
        for index in sequences:
            current_sequences = data.getSequencesAt(index)
            f.write('\t' + str(index) + ' ->\t %d' % len(current_sequences) + '\n')
            if index > 4:
                f.write('\t' + str(index) + ' ->\t' + str(current_sequences) + '\n')
