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
        # ...
        return False

    def open_spots(self):
        '''
        Ask each player where all their pieces are and return a list
        of all open piece positions
        :return: list of 0-27 indices with no pieces
        '''
        indices = []
        b_array = np.array(self.player[0].flags) | \
                  np.array(self.player[1].flags) | \
                  np.array(self.player[2].flags) | \
                  np.array(self.player[3].flags)

        for i in range(len(b_array)):
            if b_array[i] == False:
                indices.append(i)

        return indices

    def legal_moves(self, player):
        '''
        For the specified player index, start with self.open_spots(),
        and narrow down based on what pieces the player has left
        :param player:
        :return: list of 0-27 indices that player can legally play
        '''
        indices = []
        s_p, m_p, b_p = self.player[player].remaining_pieces()

        for i in self.open_spots():
            if i < 9 and s_p > 0:
                indices.append(i)
            elif i < 18 and m_p > 0:
                indices.append(i)
            elif b_p > 0:
                indices.append(i)

        return indices

    def winning_next_moves(self, player):
        '''
        For the specified player index, start from self.legal_moves(), and check
        if any of them would result in a win if played. Can be used for finding a
        winning move for the current player, or finding spots that need to be
        blocked for subsequent players
        :param player:
        :return: list of 0-27 indices that would give player a win
        '''
        indices = []
        #indices = self.legal_moves(player)
        # ...
        return indices



if __name__ == '__main__':
    g = Game()
    board = OtrioArtist()

    '''
    for p in g.player:
        p.place(index=random.randint(0,26))
        open_spots = g.open_spots()
    '''


    for move in range(27): # 27 spots, max 27 moves
        # maybe we never even need to rotate?
        p = move % 4

        # win if you can
        wins = g.winning_next_moves(p)
        if wins: # empty list evaluates as False
            g.player[p].place(index=wins[0])
            print('Player {} wins!'.format(p))
            break # game over!

        # block if you must
        blocks = g.winning_next_moves( (p+1)%4 )
        if blocks:
            g.player[p].place(index=blocks[0])

        # otherwise random
        spots = g.legal_moves(p)
        spot = np.random.choice(spots)
        g.player[p].place(index=spot)

        # wherever they played, draw the updated board
        g.player[p].draw(board)


        # this part should be able to go away
        done = False
        for i, playa in enumerate(g.player):
            if playa.has_a_win():
                done = True
                print('Player {} wins!'.format(i))
                print(playa.all_wins())
        if done:
            break

    board.im_save('gs2_test.png')

