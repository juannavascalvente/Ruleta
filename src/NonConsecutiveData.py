class NonConsecutiveData:
    def __init__(self, option: str):
        self.__num_consecutive = 0
        self.__sequences = {}
        self.__num_sequences = 0
        self.__current_sequence = []
        self.__option = option

    def reset(self):
        self.__num_consecutive = 0
        self.__num_sequences = 0
        self.__sequences = {}
        self.__current_sequence = []

    def add(self, value: int):
        self.__num_consecutive += 1
        self.__current_sequence.append(value)

    def save(self):
        if self.__num_consecutive == 0:
            return

        if self.__num_consecutive in self.__sequences:
            self.__sequences[self.__num_consecutive].append(self.__current_sequence)
        else:
            self.__sequences[self.__num_consecutive] = [self.__current_sequence]
        self.__current_sequence = []
        self.__num_consecutive = 0
        self.__num_sequences += 1

    def get_current_sequence(self) -> [int]:
        return self.__current_sequence

    def getOption(self) -> str:
        return self.__option

    def getSequences(self):
        return sorted(self.__sequences)

    def getNumSequences(self) -> int:
        return self.__num_sequences

    def getNumSequencesHigherThan(self, value: int) -> int:
        num_sequences = 0
        for index in self.__sequences:
            if index >= value:
                num_sequences += len(self.__sequences[index])
        return num_sequences

    def isEmpty(self) -> bool:
        return self.getNumSequences() == 0

    def getSequencesAt(self, index: int) -> []:
        if index not in self.__sequences:
            return []
        return self.__sequences[index]
