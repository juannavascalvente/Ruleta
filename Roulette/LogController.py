from colorama import Fore


class LogController(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def __instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls.__f = open("log.txt", "w")
        return cls._instance

    @classmethod
    def log(cls, msg: str, fore: Fore = None):
        cls.__instance().display(msg, fore)
        cls.__instance().write(msg)

    @classmethod
    def display(cls, msg: str, fore: Fore = None):
        if fore is not None:
            print(fore + msg + Fore.RESET)
        else:
            print(msg)

    @classmethod
    def write(cls, msg: str):
        cls.__instance().__f.write(msg)

    @classmethod
    def display_header(cls, msg: str):
        print('----------------------------- ' + msg + ' ----------------------------------')

    @classmethod
    def display_header_end(cls):
        print('----------------------------------------------------------------------------')

    @classmethod
    def flush(cls):
        cls.__instance().__f.flush()

    @classmethod
    def close(cls):
        cls.__instance().__f.close()
