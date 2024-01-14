import json
import sys

from Roulette import Game


def usage():
    print('Error in input number of arguments')
    print('Usage: Ruleta num_throws')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit(-1)

    f = open(sys.argv[1])
    data = json.load(f)

    roulette = Game.Game(data)
    roulette.play()
    exit(0)
