import numpy as np
import random

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
    board = OtrioArtist()

    for i in range(26):
        g.player[i%4].place(index=random.randint(0,26))
        g.player[i%4].draw(board)

    for i in range(4):
        if g.player[i].has_a_win():
            print('Player {} wins!'.format(i))
            print(g.player[i].all_wins())

    board.im_save('gs2_test.png')


