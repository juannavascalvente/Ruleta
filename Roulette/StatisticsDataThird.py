from Roulette import NonConsecutiveData, ThrowCheckerThird
from Roulette import LogController


class StatisticsDataThird:
    __BET_SEQUENCE_THRESHOLD = 7

    def __init__(self, optionA: str, optionB: str, optionC: str, throw_checker: ThrowCheckerThird):
        self.__optionA = optionA
        self.__optionB = optionB
        self.__optionC = optionC
        self.__num_throws = 0

        self.__num_As = 0
        self.__num_Bs = 0
        self.__num_Cs = 0
        self.__num_green = 0

        self.__throw_checker = throw_checker

        self.__consecutive_A = NonConsecutiveData.NonConsecutiveData(optionA)
        self.__consecutive_B = NonConsecutiveData.NonConsecutiveData(optionB)
        self.__consecutive_C = NonConsecutiveData.NonConsecutiveData(optionC)

        self.__consecutive_non_A = NonConsecutiveData.NonConsecutiveData('Non ' + optionA)
        self.__consecutive_non_B = NonConsecutiveData.NonConsecutiveData('Non ' + optionB)
        self.__consecutive_non_C = NonConsecutiveData.NonConsecutiveData('Non ' + optionC)

        self.__consecutive_non_AB = NonConsecutiveData.NonConsecutiveData('Non ' + optionA + ' nor ' + optionB)
        self.__consecutive_non_BC = NonConsecutiveData.NonConsecutiveData('Non ' + optionB + ' nor ' + optionC)
        self.__consecutive_non_AC = NonConsecutiveData.NonConsecutiveData('Non ' + optionA + ' nor ' + optionC)

    def __get_a_as_string(self) -> str:
        return self.__optionA

    def __get_b_as_string(self) -> str:
        return self.__optionB

    def __get_c_as_string(self) -> str:
        return self.__optionC

    def __get_report_header(self) -> str:
        return '------------------------------ ' + self.__get_a_as_string() + '/' + self.__get_b_as_string() + '/' + \
            self.__get_c_as_string() + ' ------------------------------\n'

    def write_stats(self):
        LogController.LogController.write(self.__get_report_header())
        num_a_sequences_without_zeros = self.__consecutive_A.getNumSequences()
        num_b_sequences_without_zeros = self.__consecutive_B.getNumSequences()
        num_c_sequences_without_zeros = self.__consecutive_C.getNumSequences()
        num_sequences_without_zeros = (num_a_sequences_without_zeros + num_b_sequences_without_zeros +
                                       num_c_sequences_without_zeros)
        LogController.LogController.write('Number of sequences (without zeros): ' + str(num_sequences_without_zeros) +
                                          '\n')

        self.__write_option(self.__consecutive_A)

        self.__write_option(self.__consecutive_non_A)

        self.__write_option(self.__consecutive_B)

        self.__write_option(self.__consecutive_non_B)

        self.__write_option(self.__consecutive_C)

        self.__write_option(self.__consecutive_non_C)

        self.__write_non_two_options(self.__consecutive_non_AB)
        self.__write_non_two_options(self.__consecutive_non_BC)
        self.__write_non_two_options(self.__consecutive_non_AC)

        num_six_or_higher = self.__consecutive_A.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_B.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_C.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_non_A.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_non_B.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_non_C.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_non_AB.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_non_BC.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD) + \
                            self.__consecutive_non_AC.getNumSequencesHigherThan(self.__BET_SEQUENCE_THRESHOLD)

        # f.write('Num sequences higher than threshold: ' + str(num_six_or_higher) + '/' +
        #         str(num_sequences_without_zeros) + '\n')
        # if num_sequences_without_zeros == 0:
        #     f.write('Percentage sequences higher than threshold: 0 %\n')
        # else:
        #     f.write('Percentage sequences higher than threshold: %.1f\n' %
        #             (float(num_six_or_higher) / float(num_sequences_without_zeros) * 100.0))
        LogController.LogController.write('Percentage ZERO or DOUBLE ZERO %.1f\n' % (float(self.__num_green) / float(self.__num_throws)
                                                           * 100.0))
        LogController.LogController.write('Percentage ' + self.__get_a_as_string() + ' %.1f\n' % (float(self.__num_As) / float(self.__num_throws)
                                                                        * 100.0))
        LogController.LogController.write('Percentage ' + self.__get_b_as_string() + ' %.1f\n' % (float(self.__num_Bs) / float(self.__num_throws)
                                                                        * 100.0))
        LogController.LogController.write('Percentage ' + self.__get_c_as_string() + ' %.1f\n' % (float(self.__num_Cs) / float(self.__num_throws)
                                                                        * 100.0))
        assert (self.__num_As + self.__num_Bs + self.__num_Cs + self.__num_green == self.__num_throws)

    def __write_option(self, data: NonConsecutiveData):
        LogController.LogController.write(data.getOption() + ':\n')
        if data.isEmpty():
            LogController.LogController.write('\tNONE\n')
            return
        i = 0
        sequences = data.getSequences()
        for index in sequences:
            current_sequences = data.getSequencesAt(index)
            LogController.LogController.write('\t' + str(index) + ' ->\t %d' % len(current_sequences) + '\n')
            if index > 4:
                LogController.LogController.write('\t' + str(index) + ' ->\t' + str(current_sequences) + '\n')

    def update_stats(self, values: [int]):

        self.__consecutive_A.reset()
        self.__consecutive_B.reset()
        self.__consecutive_C.reset()
        self.__consecutive_non_A.reset()
        self.__consecutive_non_B.reset()
        self.__consecutive_non_C.reset()
        self.__consecutive_non_AB.reset()
        self.__consecutive_non_BC.reset()
        self.__consecutive_non_AC.reset()

        for value in values:
            if self.__num_throws == 0:

                if self.__throw_checker.is_zero_or_double(value):
                    self.__num_green += 1
                    self.__consecutive_non_A.add(value)
                    self.__consecutive_non_B.add(value)
                    self.__consecutive_non_C.add(value)
                    self.__consecutive_non_AB.add(value)
                    self.__consecutive_non_BC.add(value)
                    self.__consecutive_non_AC.add(value)
                elif self.__throw_checker.is_a(value):
                    self.__num_As += 1
                    self.__consecutive_A.add(value)
                    self.__consecutive_non_B.add(value)
                    self.__consecutive_non_C.add(value)
                    self.__consecutive_non_BC.add(value)
                elif self.__throw_checker.is_b(value):
                    self.__num_Bs += 1
                    self.__consecutive_B.add(value)
                    self.__consecutive_non_A.add(value)
                    self.__consecutive_non_C.add(value)
                    self.__consecutive_non_AC.add(value)
                else:
                    self.__num_Cs += 1
                    self.__consecutive_C.add(value)
                    self.__consecutive_non_A.add(value)
                    self.__consecutive_non_B.add(value)
                    self.__consecutive_non_AB.add(value)

                self.__num_throws += 1
                continue

            self.__num_throws += 1
            if self.__throw_checker.is_zero_or_double(value):

                self.__num_green += 1

                self.__consecutive_A.save()
                self.__consecutive_B.save()
                self.__consecutive_C.save()

                self.__consecutive_non_A.add(value)
                self.__consecutive_non_B.add(value)
                self.__consecutive_non_C.add(value)

                self.__consecutive_non_AB.add(value)
                self.__consecutive_non_AC.add(value)
                self.__consecutive_non_BC.add(value)

            elif self.__throw_checker.is_a(value):
                self.__num_As += 1

                self.__consecutive_B.save()
                self.__consecutive_C.save()
                self.__consecutive_non_A.save()
                self.__consecutive_non_AB.save()
                self.__consecutive_non_AC.save()

                self.__consecutive_A.add(value)
                self.__consecutive_non_B.add(value)
                self.__consecutive_non_C.add(value)
                self.__consecutive_non_BC.add(value)

            elif self.__throw_checker.is_b(value):
                self.__num_Bs += 1

                self.__consecutive_A.save()
                self.__consecutive_C.save()
                self.__consecutive_non_B.save()
                self.__consecutive_non_AB.save()
                self.__consecutive_non_BC.save()

                self.__consecutive_B.add(value)
                self.__consecutive_non_A.add(value)
                self.__consecutive_non_C.add(value)
                self.__consecutive_non_AC.add(value)

            elif self.__throw_checker.is_c(value):
                self.__num_Cs += 1

                self.__consecutive_A.save()
                self.__consecutive_B.save()
                self.__consecutive_non_C.save()
                self.__consecutive_non_AC.save()
                self.__consecutive_non_BC.save()

                self.__consecutive_C.add(value)
                self.__consecutive_non_A.add(value)
                self.__consecutive_non_B.add(value)
                self.__consecutive_non_AB.add(value)

        self.__consecutive_A.save()
        self.__consecutive_B.save()
        self.__consecutive_C.save()
        self.__consecutive_non_A.save()
        self.__consecutive_non_B.save()
        self.__consecutive_non_C.save()
        self.__consecutive_non_AB.save()
        self.__consecutive_non_BC.save()
        self.__consecutive_non_AC.save()

        self.__check_sequences(values)

    def __write_single_option(self, option: str, data: {}, sequences_data, num_sequences_without_zeros: int,
                              num_six_or_higher: int):
        LogController.LogController.write(option + ':\n')
        if len(data) == 0:
            LogController.LogController.write('\tNONE\n')
            return
        i = 0
        for item in sorted(data):
            i += 1
            LogController.LogController.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (data[item], (float(data[item]) / float(num_sequences_without_zeros) * 100.0)) + ' %\n')
            if item > 4:
                LogController.LogController.write('\t' + str(item) + ' ->\t' + str(sequences_data) + '\n')

            if item > self.__BET_SEQUENCE_THRESHOLD:
                num_six_or_higher += data[item]

    def __write_non_single_option(self, option: str, data: {}, sequences_data, num_sequences_without_zeros: int):
        LogController.LogController.write('NON ' + option + ':\n')
        if len(data) == 0:
            LogController.LogController.write('\tNONE\n')
            return
        i = 0
        for item in sorted(data):
            i += 1
            LogController.LogController.write('\t' + str(item) + ' ->\t %d (%.1f)' %
                    (data[item], (float(data[item]) / float(num_sequences_without_zeros) * 100.0)) + ' %\n')
            if item > 4:
                LogController.LogController.write('\t' + str(item) + ' ->\t' + str(sequences_data[item]) + '\n')

    def __write_non_two_options(self, data: NonConsecutiveData.NonConsecutiveData):
        LogController.LogController.write(data.getOption() + ':\n')
        if data.isEmpty():
            LogController.LogController.write('\tNONE\n')
            return
        sequences = data.getSequences()
        for index in sequences:
            current_sequences = data.getSequencesAt(index)
            LogController.LogController.write('\t' + str(index) + ' ->\t %d' % len(current_sequences) + '\n')
            if index > 4:
                LogController.LogController.write('\t' + str(index) + ' ->\t' + str(current_sequences) + '\n')

    def __check_sequences(self, values: [int]):
        assert (self.__check_sequence(values, self.__consecutive_non_A))
        assert (self.__check_sequence(values, self.__consecutive_non_B))
        assert (self.__check_sequence(values, self.__consecutive_non_C))
        assert (self.__check_sequence(values, self.__consecutive_non_AB))
        assert (self.__check_sequence(values, self.__consecutive_non_AC))
        assert (self.__check_sequence(values, self.__consecutive_non_BC))

    def __check_sequence(self, values: [int], data: NonConsecutiveData.NonConsecutiveData) -> bool:
        for index in data.getSequences():
            sequences = data.getSequencesAt(index)
            for sequence in sequences:
                if not all(elem in values for elem in sequence):
                    return False
        return True
