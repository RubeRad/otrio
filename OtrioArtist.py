import cv2  # Open Computer Vision
import numpy as np

# some standard colors
BLK=(0,0,0)
WHT=(255,255,255)
GRY=(100,100,100) # a little toward the darker side
# player colors
BLU=(255,0,0)     # Note OpenCV uses BGR not RGB
GRN=(0,255,0)
RED=(0,0,255)
YLW=(0,255,255)
BLUl=(255,128,128) # light versions (towards white)
GRNl=(128,255,128)
REDl=(128,128,255)
YLWl=(128,255,255)

# labels for piece sizes
SMA=1
MED=2
BIG=3


# The board has these positions
#     0   1   2
#     3   4   5
#     6   7   8
# Each position has concentric spots for SMA, MED, BIG pieces of any color
class OtrioArtist:
    def __init__(self, hw=500):
        self.nrows = hw # size of the board
        self.ncols = hw
        # start with an array of (0,0,0)=BLK
        self.img = np.zeros( (hw,hw,3), np.uint8)
        # math out from the board size what is the right placement
        # of the positions and the sizes of the donuts
        self.centers = []
        for ynum in (1,3,5):
            for xnum in (1,3,5):
                xc = int(xnum * (hw/6))
                yc = int(ynum * (hw/6))
                self.centers.append((xc, yc))
        # leave position [0] as a placeholder so you can index
        # like self.radii[MED] or whatever
        self.radii = [0,int(hw/3 * .09),int(hw/3 * .245), int(hw/3 * .40)]
        self.thick = [0,-5,7,7]

    def draw_donut(self, xy, r, t, c):
        '''
        Draw a playing piece on the board as a donut (thicc circle)
        :param xy: Center coordinate, 2-tuple of integers
        :param r: Radius of center of donut thickness
        :param t: Thickness of drawing stroke (negative for filled)
        :param c: GRY, RED, GRN, RED, YLW, etc
        :return: None
        '''
        cv2.circle(self.img, xy, r, c, t) # note c/t switched order

    def place_piece(self, which, color, where):
        '''
        Draw a donut to indicate a piece being played
        :param which: Which size of piece? SMA,MED,BIG
        :param color: One of the player colors
        :param where: Position 0-8
        :return: None
        '''
        self.draw_donut(self.centers[where], self.radii[which],
                        self.thick[which], color)


    def new_board(self):
        '''
        Starting with the black board, use place_piece to draw
        grey donuts indicating all the empty spaces for pieces
        :return:
        '''
        for item in (SMA, MED, BIG):
            for i in range(9):
                self.place_piece(item, GRY, i)

    def im_save(self):
        '''
        Save image at each game state for visual aid for player
        :return:
        '''
        cv2.imwrite('Player_Gamestate.png', self.img)


if __name__ == '__main__':
    colors = [RED, GRN, BLU, YLW, REDl, GRNl, BLUl, YLWl]
    board = OtrioArtist()

    board.new_board()
    board.place_piece(MED, RED, 4)
    board.place_piece(SMA, BLU, 0)
    board.place_piece(BIG, YLW, 7)
    board.place_piece(SMA, GRN, 4)
    cv2.imwrite('donuts.png', board.img)
    board.im_save()



