import numpy as np

from OtrioArtist import *
from Player import *

class Game:
    def __init__(self):
        '''
        A game has 4 players - it tracks the pieces each player has placed
        and rotates between the players.
        '''
        self.player = [Player(RED), Player(BLU), Player(YLW), Player(GRN)]

    def rotate_player(self):
        '''
        Rotate from active player to next player in order
        :return:
        '''
        return False



if __name__ == '__main__':
    g = Game()


