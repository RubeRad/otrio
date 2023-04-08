import numpy as np

from OtrioArtist import * # colors, pieces, artist class

# A Player has 27 places he can put pieces, 9 SMA, 9 MED and 9 BIG
# and the player will hold a list of 27 flags for which of those have pieces.
# There are 49 unique winning configurations (per player, total 196).
# This function will generate and return the whole list so they can
# generate them once, at construction, and hold the list for convenient
# looping through to check for winning moves

def all_winning_triples():
    win_trip = []

    #3-Ring wins (e.g. SMB at position (0,0,0))
    for i in range(9):
        snum = i
        mnum = i + 9
        bnum = i + 18
        win_trip.append((snum, mnum, bnum))

    #Same-Size wins (e.g. MMM at (0,1,2))
    
    return win_trip

    #return [ (0,1,2),      # SMA top row
             #(4, 9+4, 18+4), # SMA,MED,BIG all in the center
             #(8,12,18) ]   # SMA LR, MED ctr, BIG UL



class Player:
    def __init__(self, c):
        '''
        A Player knows what color his pieces are, and
        holds an array of 27 flags for whether pieces are placed
        :param c: What color is this player's pieces?
        '''
        self.color = c                         # what color am I
        self.flags = [False]*27                # No pieces played to start
        self.wintrips = all_winning_triples()  # know where the wins are

    def place(self, which, where):
        '''
        Set the appropriate flag to indicate a played piece
        :param which: SMA, MED, or BIG
        :param where: Position index 0-8
        :return: None
        '''
        pass

    def draw(self, board):
        '''
        Draw all this players active pieces onto an OtrioArtist
        :param board: an OtrioArtist (may have other Player's pieces already drawn)
        :return: None
        '''
        pass

    def has_pieces(self, indices):
        '''
        Go through a list of indices (probably one of the winning 3-tuples)
        and check if all of the flags at those indices are True (pieces are placed there)
        :param indices:
        :return: True if all the indices are played, False if any are not
        '''
        return False

    def has_a_win(self):
        '''
        Check through the possible winning index triplets, if a win is found, return
        that tuple and stop searching. Otherwise return False
        :return: the 3-tuple of winning indices, or False
        '''
        return False

    def all_wins(self):
        '''
        Return a list of all winning triplets that are present in this Player's
        pieces, not just the first one found
        :return: list of winning 3-tuples (empty list if not a winning position)
        '''
        return []



if __name__ == '__main__':
    p = Player(RED)
    p.place(SMA, 4)
    p.place(SMA, 8)
    should_be_false = p.has_a_win()
    p.place(SMA, 2)
    p.place(SMA, 0)
    winner = p.has_a_win()
    winners = p.all_wins()
    should_be_one = len(winners)
    p.place(SMA, 1)
    winner = p.has_a_win()
    winners = p.all_wins()
    should_be_two = len(winners)

    board = OtrioArtist()
    p.draw(board)
    #cv2.imwrite('p1_win.png', board.img)
