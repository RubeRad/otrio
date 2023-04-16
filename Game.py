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
        self.player = [Player(REDl, RED),
                       Player(BLUl, BLU),
                       Player(YLWl, YLW),
                       Player(GRNl, GRN)]

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

        for i in self.legal_moves(player):
            self.player[player].place(index=i)
            if self.player[player].has_a_win():
                indices.append(i)
            self.player[player].remove(index=i)

        return indices



if __name__ == '__main__':
    g = Game()
    board = OtrioArtist()
    #board.im_save('move.png')

    '''
    g.player[0].place(SMA, 0)
    g.player[0].place(MED, 4)
    test1 = g.winning_next_moves(0)
    g.player[0].place(BIG, 2)
    test2 = g.winning_next_moves(0)
    '''





    for move in range(27): # 27 spots, max 27 moves
        # maybe we never even need to rotate?
        p = move % 4

        # win if you can
        wins = g.winning_next_moves(p)
        if wins: # empty list evaluates as False
            g.player[p].place(index=wins[0])
            highlight = g.player[p].all_wins()
            g.player[p].draw(board)
            for trip in highlight:
                for index in trip:
                    which, where = g.player[p].convert_to_wh(index)
                    board.draw_piece(which,g.player[p].bright,where)
            print('Player {} wins!'.format(p))
            break # game over!

        # block if you must
        blocks = g.winning_next_moves( (p+1)%4 )
        legal = g.legal_moves(p)
        if blocks and blocks[0] in legal:
            g.player[p].place(index=blocks[0])
        else: # otherwise random
            if legal:
                spot = np.random.choice(legal)
                g.player[p].place(index=spot)

        # wherever they played, draw the updated board
        g.player[p].draw(board)
        #board.im_save('move.png')

    board.im_save('win.png')

