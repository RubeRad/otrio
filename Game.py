import numpy as np

from OtrioArtist import *
from Player import *

class Game:
    def __init__(self):
        self.player = [Player(RED), Player(BLU), Player(YLW), Player(GRN)]

    def rotate_player(self):
        return False



if __name__ == '__main__':
    g = Game()


